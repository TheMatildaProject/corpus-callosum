from config.services import Services
import redis
import json
import os
import requests

def cerebrum(text, origin):
    auditoryCortexUrl = Services.getCerebrum();
    payload = {"message": text}
        
    response = requests.post(auditoryCortexUrl, json=payload)

    # If the response isn't 200, this likely means it detected room noise only
    # ignoring it for now
    try:
        responseBody = json.loads(response.text)

        publish(responseBody['message'], origin)
        
        return True
    except requests.exceptions.RequestException:
        return False

def publish(message, origin):
    # Publish message so vocal cords can poll it
    r = redis.StrictRedis(**getRedisConfig())

    if (origin == 'cochlea'):
        channel = 'vocal-cords'
    if (origin == 'slack'):
        channel = 'slack'

    r.publish(channel, message)

def getRedisConfig():
    config = {
        'host': 'queue',
    }

    return config
       