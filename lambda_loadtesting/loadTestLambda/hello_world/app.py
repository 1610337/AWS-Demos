import json
import time


def lambda_handler(event, context):

    seconds_to_wait = 10
    
    time.sleep(seconds_to_wait)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Short enough for HTTP to succeed - 10 seconds",
        }),
    }
