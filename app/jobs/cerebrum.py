from config.services import Services
import redis
import json
import os
import requests

def cerebrum(request, origin):
    cerebrumUrl = Services.getCerebrum();

    payload = {"message": request['text']}
        
    response = requests.post(cerebrumUrl, json=payload) 

    # If the response isn't 200, this likely means it detected room noise only
    # ignoring it for now
    try:
        responseBody = json.loads(response.text)

        publish(responseBody['message'], origin, request)
        
        return True
    except requests.exceptions.RequestException:
        return False

def publish(message, origin, extra):
    # Publish message so vocal cords can poll it
    r = redis.StrictRedis(**getRedisConfig())

    if (origin == 'cochlea'):
        channel = 'vocal-cords'
    if (origin == 'slack'):
        # In case of Slack, there's a few extra parameters that need to be sent
        # Save the original question just in case
        # @TODO this is super messy, fix it later
        extra['original'] = extra['text']
        extra['text'] = message
        message = extra
        channel = 'slack'

    r.publish(channel, message)

def getRedisConfig():
    config = {
        'host': 'queue',
    }

    return config
       