# SCA-Cloud-School-Application

##  SCA Cloud School Technical Assessment
This project implements an application in python using flask and redis which displays a text on the webpage.”Welcome to SCA Cloud School Application , this is my first assessment” 
## Requirement
Flask,
Redis
## Test Process
I created a docker file and defined services in a docker-compose file, specifying the version, redis, ports, volumes and environment. With this system, I can write my Dockerfile once and use it several times without having to rebuild the image. 
Run docker-compose up 
You should be able to access the webpage at localhost:5000. I have attached a screenshot of my webpage. It is located in the docker folder
## Deployment
Tagged my docker image using docker tag chetachi/application_web:sca
Pushed into Docker hub using docker push chetachi/application_web:sca
## Dockerhub Link
https://hub.docker.com/repository/docker/chetachi/application_web
