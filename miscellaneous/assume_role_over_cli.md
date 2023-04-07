
All API calls needed to assume a role over the CLI (Amazon Linux 2)

Verify current/future identity:
```bash
aws sts get-caller-identity
```

Manually setting credentials:
```bash
aws sts assume-role --role-arn "arn:aws:iam::111222333444:role/ROLENAME" --role-session-name AWSCLI-SessionName
```

Automatically setting credentials (env variables):
```bash
eval $(aws sts assume-role --role-arn "arn:aws:iam::111222333444:role/ROLENAME" --role-session-name SessionName | jq -r '.Credentials | "export AWS_ACCESS_KEY_ID=\(.AccessKeyId)\nexport AWS_SECRET_ACCESS_KEY=\(.SecretAccessKey)\nexport AWS_SESSION_TOKEN=\(.SessionToken)\n"')
```

Unset credentials (env variables):
```bash
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
```