
### Assume a role over the CLI

This is a walkthrough of how to assume a role using the CLI. This can be used to showcase the temporary credentials issued by the sts service.

Note: This walkthrough is intended to run on Amazon Linux 2

Name of role to assume: <br>
`arn:aws:iam::111122223333:role/role_s3_read_only`

Check which role/credentials are currently used:<br>
`aws sts get-caller-identity`

Check if you can list S3 buckets: <br>
`aws s3 ls`

Receive role-based temporary credentials from sts (you have to put them into env variables yourself then): <br>
`aws sts assume-role --role-arn "arn:aws:iam::111122223333:role/role_s3_read_only" --role-session-name AWSCLI-SessionName`

Automatically get role-based temporary credentials from sts  and set them as env variables: <br>
`eval $(aws sts assume-role --role-arn arn:aws:iam::111122223333:role/role_s3_read_only --role-session-name SessionName | jq -r '.Credentials | "export AWS_ACCESS_KEY_ID=\(.AccessKeyId)\nexport AWS_SECRET_ACCESS_KEY=\(.SecretAccessKey)\nexport AWS_SESSION_TOKEN=\(.SessionToken)\n"')`

Unset env variables: <br>
`unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN`

### Interesting/helpful resources:
https://stackoverflow.com/questions/63241009/aws-sts-assume-role-in-one-command <br>
https://aws.amazon.com/premiumsupport/knowledge-center/iam-assume-role-cli/ <br>
https://yum-info.contradodigital.com/view-package/epel/jq/ <br>

