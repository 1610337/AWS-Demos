
import base64
import io
import json
import logging
import boto3
from PIL import Image

# REFERENCE TO BEDROCK SERVICE
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')


# DEFINE PARAMETERS FOR CALLING BEDROCK
model_id = 'amazon.titan-image-generator-v1'
prompt = """A mexican president, cartoon style"""

body = json.dumps({
    "taskType": "TEXT_IMAGE",
    "textToImageParams": {
        "text": prompt
    },
    "imageGenerationConfig": {
        "numberOfImages": 1,
        "height": 1024,
        "width": 1024,
        "cfgScale": 8.0,
        "seed": 0
    }
})
accept = "application/json"
content_type = "application/json"

# CALL BEDROCK SERVICE WITH PARAMETERS
response = bedrock.invoke_model(
    body=body, modelId=model_id, accept=accept, contentType=content_type
)

# IMAGE PROCESSING
response_body = json.loads(response.get("body").read())
base64_image = response_body.get("images")[0]
base64_bytes = base64_image.encode('ascii')
image_bytes = base64.b64decode(base64_bytes)

image = Image.open(io.BytesIO(image_bytes))
image.show()
