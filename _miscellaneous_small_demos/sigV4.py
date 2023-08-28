'''
Demo to show how to sign the "DescribeRegions" API call (ec2) using SigV4. 
Reference: https://docs.aws.amazon.com/IAM/latest/UserGuide/create-signed-request.html
Note: boto3 is still used to retrieve the credentials from the AWS CLI to avoid credentials in code.
'''

'''
How to use:
Just execute the code and follow/observe the instructions on the CLI
'''

import datetime, hashlib, hmac 
import requests

# ************* REQUEST VALUES *************
method = 'GET'
service = 'ec2'
host = 'ec2.amazonaws.com'
region = 'us-east-1'
endpoint = 'https://ec2.amazonaws.com'
request_parameters = 'Action=DescribeRegions&Version=2013-10-15'

def main():
    t = datetime.datetime.utcnow()
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d') # Date w/o time
    canonical_uri = '/' 
    canonical_querystring = request_parameters

    # print("++++++ Parameters ++++++")
    # print(canonical_querystring)

    canonical_headers = 'host:' + host + '\n' + 'x-amz-date:' + amzdate + '\n'
    signed_headers = 'host;x-amz-date'
    payload_hash = hashlib.sha256(('').encode('utf-8')).hexdigest()
    canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
    string_to_sign = algorithm + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

    signing_key = getSignatureKey(secret_key, datestamp, region, service)
    signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
    print("++++++ Signature ++++++")
    print("Secret Key:", "****")
    print("Timestamp:", datestamp)
    print("Region:", region)
    print("Service:", service)
    print("")
    print("All together as hash:", signature)
    print("")
    input("Continue?")

    authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

    headers = {'x-amz-date':amzdate, 'Authorization':authorization_header}
    print("++++++ Header ++++++")
    print("")
    print(headers)
    print("")
    input("Continue?")
    # ************* SEND THE REQUEST *************
    request_url = endpoint + '?' + canonical_querystring

    print('\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++')
    print('Method = ' + method)
    print('Request URL = ' + request_url)
    r = requests.get(request_url, headers=headers)
    
    print("")
    input("Continue and run (finally)?")

    print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
    print('Response code: %d\n' % r.status_code)
    print(r.text)

# Key derivation functions. See:
# http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python
def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning

# set credentials (over boto3)
import boto3
session = boto3.Session()
credentials = session.get_credentials()

access_key = credentials.access_key 
secret_key = credentials.secret_key 

main()

