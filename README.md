# Simple Crud Application Flask Dockerized

This is a simple API build using Flask and then has been converted to a Docker Container. Also, this is my first attempt to make a Dockerfile for an app.

### How to run the app?

This is a basic API which just returns a number.
To run the API follow the following steps:-
1. Make a virtualenv 
```
virtualenv venv --python=python3 
```
2. Shift to virtualenv
```
source venv/bin/activate
```
3. Install the dependencies
```
pip --no-cache-dir --user install -r requirements.txt
```
4. Run the app
```
python app.py
```

### How to run the Docker Container
This application has been converted to a docker container.
1. Install docker
2. To make image for the application
```
docker build -t flaskapp:latest .
```
This command will automaticaly make a docker image from the `Dockerfile` which we have.
3. To build a container out of the docker image
```
docker run -d -p 9000:5000 flaskapp
```
This will provide the service at port 9000 on the localhost.
The Sevice form port 9000 would be mapped to port 5000 of the continer.
