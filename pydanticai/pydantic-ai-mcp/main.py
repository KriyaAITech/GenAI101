import os
from dotenv import load_dotenv
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from pydantic_ai import Agent

import mcp_tools
from get_language_model import get_openai_model, get_gemini_model

# Load environment variables from .env file
load_dotenv()

async def chat_loop(agent: Agent) -> None:
    """Run an interactive chat loop with the agent until the user enters 'q' to quit."""
    print("Starting chat with AI agent. Type 'q' to quit.")
    print("-" * 50)
    
    # Keep track of conversation history
    conversation_history = []
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        
        # Check if user wants to quit
        if user_input.lower() == 'q':
            print("Exiting chat. Goodbye!")
            break
        
        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})
        
        try:
            # Format the conversation history for the agent
            prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_history])
            
            # Run the agent with the prompt
            result = await agent.run(prompt)
            response = result.data
            
            # Add agent response to history
            conversation_history.append({"role": "assistant", "content": response})
            
            # Print the agent's response
            print(f"\nAI: {response}")
            
        except Exception as e:
            print(f"\nError: {str(e)}")


#we want to connect three wo mcp-servers
# 1. mcp/github
# 2. mcp/brave-search
# 3. mcp/sequential-thinking
# we are integrating mcp-server using the docker method. Not the npx method.
async def main() -> None:
    # Create server parameters for all servers
    github_params = StdioServerParameters(
        command=os.getenv("DOCKER_COMMAND", "docker"),
        args = [
        "run",
        "-i",
        "--rm",
        "-e",
        "GITHUB_PERSONAL_ACCESS_TOKEN",
        "mcp/github"
      ],
        env={"GITHUB_PERSONAL_ACCESS_TOKEN": os.getenv("GITHUB_TOKEN")}
    )

    brave_params = StdioServerParameters(
        command=os.getenv("DOCKER_COMMAND", "docker"),
        args = [
        "run",
        "-i",
        "--rm",
        "-e",
        "BRAVE_API_KEY",
        "mcp/brave-search"
      ],
        env={"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
    )

    # new mcp_server for sequential thinking
    seq_params = StdioServerParameters(
        command=os.getenv("DOCKER_COMMAND", "docker"),
        args = [
        "run",
        "--rm",
        "-i",
        "mcp/sequentialthinking"
      ],
    )

    # read environment variable MODEL_NAME from .env file. 
    # choose model based on MODEL_NAME
    model_name = os.getenv("MODEL_NAME")
    print('model_name is: ', model_name, type(model_name))
    if model_name == "OPENAI_MODEL":
        model = get_openai_model()
    elif model_name == "GEMINI_MODEL":
        model = get_gemini_model()
        
    # Use all servers in nested context managers
    async with stdio_client(github_params) as (github_read, github_write):
        async with stdio_client(brave_params) as (brave_read, brave_write):
            async with stdio_client(seq_params) as (seq_read, seq_write):

                async with (
                    ClientSession(github_read, github_write) as github_session,
                    ClientSession(brave_read, brave_write) as brave_session,
                    ClientSession(seq_read, seq_write) as seq_session
                ):
                    # Get tools from both sessions
                    github_tools = await mcp_tools.mcp_tools(github_session)
                    brave_tools = await mcp_tools.mcp_tools(brave_session)
                    seq_tools = await mcp_tools.mcp_tools(seq_session)
                    
                    # Combine tools from both servers
                    combined_tools = github_tools + brave_tools + seq_tools
                    
                    agent = Agent(model, tools=combined_tools)
                    
                    # Start the interactive chat loop
                    await chat_loop(agent)


if __name__ == "__main__":
    asyncio.run(main())

