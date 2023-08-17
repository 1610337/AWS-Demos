#!/bin/bash
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin ACCOUNT_ID_TO_BE_REPLACED.dkr.ecr.eu-central-1.amazonaws.com
docker pull ACCOUNT_ID_TO_BE_REPLACED.dkr.ecr.eu-central-1.amazonaws.com/flaskwebserver:latest
docker run -d -t -p 80:5000 ACCOUNT_ID_TO_BE_REPLACED.dkr.ecr.eu-central-1.amazonaws.com/flaskwebserver
