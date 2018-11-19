import json
import random
import urllib.request

def lambda_handler(event, context):
    url = "https://chi-ni.com/motd/{:02}.html".format(random.randint(0,19))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type' : 'text/html'
        },
        'body': response
    }