
# python code for lambda to return a static web page - especially nice when the Lambda function has a public URL
# ! BE CAREFUL WITH PUBLIC URLs FOR LAMBDA !

import json
import boto3 

def lambda_handler(event, context):

    myWebsite = "<html><body bgcolor=\"orange\"><h1>This is WebServer 01 </h1></body></html>"
    
    return {
        'statusCode': 200,
        "headers": {'Content-Type': 'text/html'},
        'body': myWebsite
    }
