import boto3
import json
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

body = json.dumps({
    "inputText": "Who was the last american president?",
    "textGenerationConfig": {
        "maxTokenCount": 4096,
        "stopSequences": [],
        "temperature": 0,
        "topP": 1
    }})

modelId = 'amazon.titan-text-express-v1'
accept = 'application/json'
contentType = 'application/json'

response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)

# print out answer
response_body = json.loads(response.get('body').read())
for result in response_body['results']:
            print(f"Output text: {result['outputText']}")
            