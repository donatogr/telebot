import json
import random
import urllib.parse
import urllib.request

token = ''

def lambda_handler(event, context):
    body = json.loads(event['body'])
    message = body['message']
    text = message['text']
    chat_id = message['chat']['id']

    response_text = joke()

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    
    data = {
        'chat_id': chat_id,
        'text': response_text
    }

    req = urllib.request.Request(
        url, 
        data=json.dumps(data).encode(),
        headers={'Content-type': 'application/json'}
    )
    response = urllib.request.urlopen(req)
    content = response.read()
    
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
    

def joke():
    names = [
        {"first_name": "Chuck", "last_name": "Norris"}
    ]

    url = 'http://api.icndb.com/jokes/random?escape=javascript&limitTo=[nerdy]&firstName={first_name}&lastName={last_name}'

    name = random.choice(names)

    req = urllib.request.Request(
        url.format(**name)
    )
    response = urllib.request.urlopen(req)
    json_content = response.read().decode()
    content = json.loads(json_content)
    return content['value']['joke']
