### 𝙀𝙆𝙎 - 𝘿𝙀𝙈𝙊

##### This file summarizes all relevant documentations/resources/commands I used to built this demo.

This demo sets up a basic node.js server and contains buildspec files to build the countainer in AWS CodeBuild and push it to ECR.
Below you can also find commands to set up an EKS cluster hosting this container. 


###### Node.js controls
- run node locally: `node index.js`
- `curl http://localhost:8080`
- preview Tab (next to Run button --> view running application)
- kill process `npx kill-port 8080`

###### Docker controls:
- build container locally
  - `docker build . -t <your username>/node-web-app`
- list existing docker images `docker images`
- run container
  - `docker run -p 3000:3000 -d <your username>/node-web-app`
  - `curl -i localhost:3000`
- list running containers `docker ps` 
- kill a container `docker kill <container id>`

###### Kubernetes Controls:
```
- eksctl scale nodegroup --cluster eks-demo-cicd --name nodegroup --nodes 0 --nodes-max 1 --nodes-min 0 
- eksctl scale nodegroup --cluster eks-demo-cicd --name nodegroup --nodes 2 --nodes-max 2 --nodes-min 2 
- kubectl get deploy
- kubectl get pods
- Kubectl rollout restart deployment <deployment-name>
- Kubectl rollout restart deployment webapp
- kubectl version --client
- kubectl get svc
- kubectl config view --minify
- kubectl describe configmap -n kube-system aws-auth
- kubectl describe configmap -n kube-system aws-auth
- eksctl create cluster -f eksworkshop.yaml
- kubectl logs webapp-76c9bb44f5-hf5xj --previous
- kubectl create -f manifest.yaml
- kubectl apply -f manifest.yaml
- kubectl describe deploy
- kubectl rollout restart deploy webapp
- kubectl  expose deploy webapp --type=LoadBalancer
- kubectl  delete svc webapp && kubectl  expose deploy webapp --type=LoadBalancer
- Where I allow listed the IAM Role of Code Build
- kubectl edit -n kube-system cm aws-auth
- kubectl apply -f manifest.yaml
```

###### Build and deploy from local:
```
- docker build -t nodeserver .
- docker tag nodeserver:latest YOUR_ACCOUNT_ID.dkr.ecr.eu-central-1.amazonaws.com/nodeserver:latest
- docker push YOUR_ACCOUNT_ID.dkr.ecr.eu-central-1.amazonaws.com/nodeserver:latest
- aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.eu-central-1.amazonaws.com
- docker push YOUR_ACCOUNT_ID.dkr.ecr.eu-central-1.amazonaws.com/nodeserver:latest
- kubectl get deploy
- kubectl rollout restart deploy webapp
```


###### Relevant Documentation:
- https://www.w3schools.com/nodejs/nodejs_get_started.asp
- https://nodejs.org/en/docs/guides/nodejs-docker-webapp/
- https://catalog.us-east-1.prod.workshops.aws/workshops/2175d94a-cd79-4ed2-8e7e-1f0dd1956a3a/en-US/review/codepipeline

###### Troubleshooting guides that helped:
- https://docs.aws.amazon.com/codebuild/latest/userguide/troubleshooting.html#troubleshooting-cannot-connect-to-docker-daemo
- https://stackoverflow.com/questions/56863539/getting-error-an-error-occurred-accessdenied-when-calling-the-assumerole-oper
- https://aws.amazon.com/premiumsupport/knowledge-center/codebuild-eks-unauthorized-errors/
- https://medium.com/@jeff.lee.1990710/deploy-your-project-to-eks-in-codebuild-dddf4c07eb39

###### Commands that I tried but didn't help me
```
- aws eks --region eu-central-1 update-kubeconfig --name eks-demo-cicd
- aws eks update-kubeconfig --region eu-central-1  --name eks-demo-cicd
- kubectl edit configmap aws-auth --namespace kube-system
- aws eks update-kubeconfig --name eks-demo-cicd --region eu-central-1
- ksctl create iamidentitymapping --cluster eks-demo-cicd --arn arn:aws:iam::443549627532:role/SSMDefaultRoleForPVREReporting --group system:masters --username admin
```

###### Eventually interesting:
```
- npx kill-port 8080
- aws kms create-alias --alias-name alias/eksworkshop --target-key-id $(aws kms create-key --query KeyMetadata.Arn --output text)
- export MASTER_ARN=$(aws kms describe-key --key-id alias/eksworkshop --query KeyMetadata.Arn --output text)
- echo "export MASTER_ARN=${MASTER_ARN}" | tee -a ~/.bash_profile
- watch kubectl get pods
- git log -p -- Dockerfile
```
