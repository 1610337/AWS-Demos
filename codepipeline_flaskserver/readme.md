### This code is used as a baseline for a demo in my classes. I am using this public repo just for my own reference.

In this folder you can fine a basic flask server with tests. This server can be containerized and also be build and deployed using AWS CodeBuild and AWS CodeDeploy.
The required appspec and buildspec files are also in this repo.

#### Important commands:
- python -m pytest
- python app.py

#### Run the container locally:
- aws ecr get-login-password --region eu-central-1 | sudo docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.eu-central-1.amazonaws.com
- sudo docker pull ACCOUNT_ID.dkr.ecr.eu-central-1.amazonaws.com/flaskwebserver:latest
    - When pulling code from ECR to EC2 make sure that the role has IAM permissions
- sudo docker run -d -t -p 80:5000 ACCOUNT_ID.dkr.ecr.eu-central-1.amazonaws.com/flaskwebserver

#### Initial push to AWS CodeCommit:
- git config --global user.name "Tim"
- git config --global user.email mail@example.com
- git remote add origin https://git-codecommit.eu-central-1.amazonaws.com/v1/the_specific_clone_url
- git push -u origin master

Other Learnings:
- Pull original code directly from EC2
    - Check for right IAM Permissions (in EC2 role)
    - Run the following commands to set up credentials before cloning
- git config --global credential.helper '!aws codecommit credential-helper $@
- git config --global credential.UseHttpPath true
