from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message":"Hello from inside a container"}
# If you run the docker build without any requirements.txt the pipinstallstep does nothing useful or fails then when the container tries to run the modules it will crash with ModuleNotFoundError
# Docker build reads your file from top to bottom and executes each line as a separate step pull the base image then set the working directory copy the files and register the final cmd  each step is cached layer so in future when you change the code docker is smart enough to skipping installing packages again and rebuilds faster.
# The container is its own sealed box even though your fastapi app inside it is listening on port 8000 that port is trapped inside the box by default invisible from your laptop.