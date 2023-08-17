
## About this project

This is a project that demonstrates how to create a new VPC, EC2 Auto Scaling group + ALB, and RDS instance with the CDK.
**Note:** This is a private fork from [1]. The code has been partially refactored to fix errors, suit demos and implement other best practises.
**Important:** This template is far from being ready for use in any production system

## Relevant Commands
```python3 -m venv .venv```
```pip install -r requirements.txt```
```cdk synth```
```cdk deploy --all```
```cdk destroy --all```
```cdk diff```

[1] https://github.com/aws-samples/aws-cdk-examples/tree/master/python/new-vpc-alb-asg-mysql

