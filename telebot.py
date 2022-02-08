import json
import random
import urllib.parse
import urllib.request

token = '1326070328:AAFiJLIu-o-Z7vCNxw8Tf6vd95xv2Li7u78'

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
        {"first_name": "Andrea", "last_name": "Fabretto"},
        {"first_name": "Donato", "last_name": "Grieco"},
        {"first_name": "Alessandro", "last_name": "Bordini"},
        {"first_name": "Giordano", "last_name": "Sala"},
        {"first_name": "Ronald", "last_name": "Tischler"},
        {"first_name": "Lukas", "last_name": "Marcincin"},
        {"first_name": "Karol", "last_name": "Hajdu"},
        {"first_name": "Dusan", "last_name": "Herich"}
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
