#!/bin/bash
sudo docker ps -aq | sudo xargs docker stop | sudo xargs docker rm
