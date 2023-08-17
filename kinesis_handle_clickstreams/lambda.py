import json
import boto3
import random
import datetime

kinesis = boto3.client('kinesis')
def getReferrer():
    x = random.randint(1,5)
    x = x*50 
    y = x+30 
    data = {}
    data['user_id'] = random.randint(x,y)
    data['device_id'] = random.choice(['mobile','computer', 'tablet', 'mobile','computer'])
    if data['user_id']=='BE':
        data['client_event'] = random.choices(["add_belgian_beer","add_german_beer","checkout","cancel"], [11,2,3,2])[0]
    elif data['user_id']=='DE':
        data['client_event'] = random.choices(["add_belgian_beer","add_german_beer","checkout","cancel"], [3,10,3,2])[0]
    elif data['user_id']=='FR':
        data['client_event'] = random.choices(["add_belgian_beer","add_german_beer","checkout","cancel"], [6,7,3,2])[0]
    elif data['user_id']=='UK':
        data['client_event'] = random.choices(["add_belgian_beer","add_german_beer","checkout","cancel"], [7,6,3,2])[0]
    elif data['user_id']=='NL':
        data['client_event'] = random.choices(["add_belgian_beer","add_german_beer","checkout","cancel"], [5,8,3,2])[0]
    elif data['user_id']=='ES':
        data['client_event'] = random.choices(["add_belgian_beer","add_german_beer","checkout","cancel"], [8,5,3,2])[0]
    elif data['user_id']=='IT':
        data['client_event'] = random.choices(["add_belgian_beer","add_german_beer","checkout","cancel"], [6,6,3,2])[0]
    else:
        data['client_event'] = random.choices(["add_belgian_beer","add_german_beer","checkout","cancel"], [6,6,3,2])[0]
    now = datetime.datetime.now()
    str_now = now.isoformat()
    data['client_timestamp'] = str_now
    data['countrycode'] = random.choices(["BE", "DE", "FR","UK","NL", "ES", "IT"],[100,130,30,40,59,29,47])[0]


    return data

def lambda_handler(event, context):
   begining = datetime.datetime.now()
   newtime = begining
   while (newtime - begining).total_seconds()<55:
        data = json.dumps(getReferrer())
        payload = str(data)+'\n'
        kinesis.put_record(
                StreamName='NAME_OF_TARGET_STREAM',
                Data=payload,
                PartitionKey='partitionkey')
        newtime = datetime.datetime.now()
   print ('Cleaned end execution.')