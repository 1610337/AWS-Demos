## About this repository:
This repository contains a basic layered architecture using nested stacks. It will create an auto-scaling-group, security groups, elastic loadbalancer and an iam role.
The compute resources will be deployed into a vpc of choice (based on the parameters that are set). The overall architecture will host a static website based on the user-data script.

The main purpose of this template is to showcase more advanced functionalities of CloudFormation. **Important:** This template is not ready to be used
in any production scenario!

## How to deploy this template:
1. Replace the bucket urls in global.yaml to a bucket that you own
2. Upload all files into the referenced bucket
3. Deploy the template through CloudFormation by referencing the public s3 url to global.yaml (the bucket can stay private) 

## Good tools: 
**TaskCat:** 
https://github.com/aws-ia/taskcat

TaskCat deploys AWS CloudFormation templates in multiple AWS Regions and generates a report with a pass/fail grade for each region. It also provides reasons for a failed deployment.

```taskcat test run```

Note: Make sure to potentially sync. your working directory with your s3 bucket first if needed.

**CFN-Lint:** https://github.com/aws-cloudformation/cfn-lint

Validate AWS CloudFormation yaml/json templates against the AWS CloudFormation Resource Specification

```cfn-lint global.yaml compute.yaml network.yaml security.yaml```

## Neat commands:
Upload all files of current directory to S3
```aws s3 sync . s3://my-bucket/path```

## Future work:
This template offers a good foundation to showcase cfn-helper scripts
