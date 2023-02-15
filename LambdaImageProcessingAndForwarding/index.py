import base64
import urllib.parse
import re
import urllib.request
import os
import boto3
import json
import traceback

from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import time
    
def lambda_handler(event, context):
    try: 
        mail_to = "tim@example.com"
        mail_from = "tim@example.com" # make sure to register with the SES service! and at best don't hardcode e-mails
        
        # decode base64 encoded message
        base64_message = event["body"]
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        # decode Windows-1252 encoding according to ASCII Encoding
        # Reference: https://www.w3schools.com/tags/ref_urlencode.ASP
        message = urllib.parse.unquote(str(message))
        
        # Use a regex to find the download URL for the image
        regex = r"&MediaUrl0=([\s\S]*)&ApiVersion"
        matches = re.search(regex, message)
        matches_list = []
        
        if matches:
            for groupNum in range(0, len(matches.groups())):
                groupNum = groupNum + 1
                matches_list.append(matches.group(groupNum))
        # The first match is the URL we are looking for
        url= matches_list[0]
        
        # Opening the first URL redirects us to a second URL that actually contains the image. Here we get the new URL.
        req = urllib.request.Request(url, data=None, 
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        response = urllib.request.urlopen(req)
        # replace old url by new url
        url = response.geturl()
        
        # set up a name to store the image 
        unix_time = str(int(time.time()))
        image_name = "image_"+unix_time+".jpg"

        # request image and store in /tmp/
        os.chdir('/tmp')
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'whatever')
        filename, headers = opener.retrieve(url, image_name)
        
        '''
        # store img in s3
        bucket_name = "bucket_name"
        s3 = boto3.resource("s3")
        s3.meta.client.upload_file(image_name, bucket_name, image_name)
        '''
        
        # forward image via e-mail
        msg = MIMEMultipart()
        msg["Subject"] = "Image Forwarding Rule jWyUi39A4o"
        msg["From"] = mail_from
        msg["To"] = mail_to
    
        # Set message body
        body = MIMEText("", "plain")
        msg.attach(body)

        # Attach image to message
        with open(image_name, "rb") as attachment:
            part = MIMEApplication(attachment.read())
            part.add_header("Content-Disposition", "attachment", filename=image_name)
        msg.attach(part)
    
        # Convert message to string and send
        ses_client = boto3.client("ses", region_name="eu-central-1")
        response = ses_client.send_raw_email(
            Source=mail_from,
            Destinations=[mail_to],
            RawMessage={"Data": msg.as_string()}
        )
        
       # print(response)
       # print(matches)
    
        return {
            'statusCode': 200,
            'body': json.dumps('Thank you! The image was send via mail.')
        }
    except Exception as e :
        traceback.print_exc()
        return {
          'statusCode': 400,
          'body': json.dumps('Oh - that didnt quite work out.')  
        }

