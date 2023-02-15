#!/bin/bash
yum -y update 
yum -y install docker
service docker start
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin ACCOUNT_ID_TO_BE_REPLACED.dkr.ecr.eu-central-1.amazonaws.com
docker pull ACCOUNT_ID_TO_BE_REPLACED.dkr.ecr.eu-central-1.amazonaws.com/flaskwebserver:latest

