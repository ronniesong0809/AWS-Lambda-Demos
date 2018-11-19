import json
import datetime

def lambda_handler(event, context):
    current_time = datetime.datetime.now()
    body = { 'currentTime' : str(current_time) }
    
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type' : 'application/json'
        },
        'body': json.dumps(body)
    }
    
    return response