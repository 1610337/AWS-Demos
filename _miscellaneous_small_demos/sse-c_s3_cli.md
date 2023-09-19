### SSE-C Encryption with S3

This walkthrough shows how to create a key on the client-side and use this key for de/encryption on the server-side. With every read/write request
this key has to be provided. This demo is designed to run on Amazon Linux 2


Create own security key and store locally:<br>
`openssl rand 32 -out ssec.key`

Put object in bucket and provide key:<br>
`aws s3 cp test_text.txt s3://security-demo-bucket/test_text.txt --sse-c AES256 --sse-c-key fileb://ssec.key`

Try direct download:<br>
`Download in Managment Console will fail`

Try direct download here in CLI:<br>
`aws s3 cp s3://security-demo-bucket/test_text.txt text-downloaded.txt`

Download object and provide key:<br>
`aws s3 cp s3://security-demo-bucket/test_text.txt text-downloaded.txt --sse-c AES256 --sse-c-key fileb://ssec.key`