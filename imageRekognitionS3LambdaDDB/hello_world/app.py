import json
import boto3
import os

def lambda_handler(event, context):

    # get filename from event (eg. jeff.JPG)
    photo = event['Records'][0]['s3']['object']['key']

    # get source bucket name and target ddb from environment variables (bucket name is also in input event)
    bucketName = os.environ['bucketName']
    dynamoTable = os.environ['dynamoTable']

    # get boto3 clients for aws services
    rek_client = boto3.client('rekognition')
    ddb_client = boto3.client('dynamodb')
    s3 = boto3.resource('s3')

    # download image from event
    target = "/tmp/"+photo
    s3.meta.client.download_file(bucketName, photo, target)

    # send image to rekognition
    with open(target, 'rb') as image:
        response = rek_client.recognize_celebrities(Image={'Bytes': image.read()})

    # read values from rekognition result (just first celebrity)
    name = response['CelebrityFaces'][0]['Name']
    smile = response['CelebrityFaces'][0]['Face']['Smile']['Value']

    # put result in dynamoDB
    ddb_client.put_item(TableName=dynamoTable, Item={'celebrity_name':{'S':name},'smile':{'BOOL':smile}})

    return {
        'statusCode': 200,
        'body': json.dumps( 'I found: ' + name)
    }
