This project is to demonstrate the use of mcp-servers with AI Agents. 
We will be using PydanticAI to instantiate our Agent
The mcp-servers used are
1. mcp/brave-search  - https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search
2. mcp/github - https://github.com/modelcontextprotocol/servers/tree/main/src/github

The mcp-servers can be run using docker or npx. We have chosen to use docker.
To run this repo as is, you will need to have docker installed. 

# Steps to get this repo running:
1. Clone this repo. (Consider giving it a star if you find it useful.)
2. [Get mcp-servers up and running by installing docker and create mcp/brave-search and mcp/github docker images](/pydanticai/pydantic-ai-mcp#step2-get-mcp-servers-up-and-running)
3. Create a virtual environment and install project dependencies.
4. Rename .env.example to .env and update your api keys. 
Note: To use mcp/github, you will need a github key. And to use mcp/brave-search you will need brave-api-key
Steps to generate a github key can be found at: https://www.geeksforgeeks.org/how-to-generate-personal-access-token-in-github/
Generate a Brave api key at https://brave.com/search/api/
5. Run main.py

Let's go through these steps in detail.
## Step1: Clone the repo

## Step2: Get mcp-servers up and running
Steps to get mcp-servers running
1. Install docker
2. Install docker-desktop (optional step, just makes it easier to visualize)
3. Follow the 'docker build' commands found in the github repo for mcp-servers mentioned above. This should create the docker image based on latest udpates. 
Note: The mcp/brave-search and mcp/github docker images are also found on DockerHub.
However, they are not up to date. Installing and using the images from DockerHub has not worked for me. 
The better option is to build your own image from the repo by using the 'docker build' command.

4. Launch docker desktop and check the images you have built. The container will get instantiated only when you run python code.
Note: Docker desktop application has to be launched. Only then docker containers will get instantiated when you run python code.

## Step3: Create a virtual environment and install project dependencies
I have used uv by astral-sh (https://github.com/astral-sh/uv), an efficient python project manager.
I suggest you also use uv to install dependencies and maintain this project. However, you can still make do with pip and python virtual environments.

1. First, make sure you have uv installed in your system.
2. navigate into the project directory (pydantic-ai-mcp/) and run the command 'uv sync'.
This should create a local .venv and install all dependencies in it automatically.

## Step4: Rename .env.example to .env and update your api keys
There is an .env.example file in the repo. First, rename the file to .env
Then, add your api keys to this .env file.
If you are using an OpenAI Model, the MODEL_NAME variable has to be set to "OPENAI_MODEL"
If you are using an Google Gemini Model, the MODEL_NAME variable has to be set to "GEMINI_MODEL"
The GEMINI_API_KEY or sometimes called as GOOGLE_API_KEY allows your to use llms from google ai studio.
The OPENAI_API_KEY allows you to use llms from openai.

## Step5: Run main.py
Run the command using 'uv run main.py'. You will now have access to a chat loop in the terminal.
You can converse with the agent as you normally would. Or you can give prompts which require the usage of tools (either from mcp/github or mcp/brave-search)

Example prompt: 







