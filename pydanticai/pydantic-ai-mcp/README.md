This project is to demonstrate the use of mcp-servers with AI Agents. 
We will be using PydanticAI to instantiate our Agent
The mcp-servers used are
1. mcp/brave-search  - https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search
2. mcp/github - https://github.com/modelcontextprotocol/servers/tree/main/src/github

The mcp-servers can be run using docker or npx. We have chosen to use docker.
To run this repo as is, you will need to have docker installed. 

Steps to get mcp-servers running
1. Install docker
2. Install docker-desktop (optional step, just makes it easier to visualize)
3. Follow the 'docker build' commands found in the github repo for mcp-servers mentioned above. This should create the docker image based on latest udpates. 

Note: The mcp/brave-search and mcp/github docker images are also found on DockerHub.
However, they are not up to date. Installing and using the images from DockerHub has not worked for me. 
The better option is to build your own image from the repo by using the 'docker build' command.

4. Launch docker desktop and check the images you have built. The container will get instantiated only when you run python code.

Note: Docker desktop application has to be launched. Only then docker containers will get instantiated when you run python code.




