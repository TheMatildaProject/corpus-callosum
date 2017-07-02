from app.jobs.cerebrum import cerebrum
from config.services import Services
from redis import Redis
from rq import Queue
import json
import requests

def auditory_cortex(audio, origin):
    auditoryCortexUrl = Services.getAuditoryCortex();
    payload = {"audio": audio}
        
    response = requests.post(auditoryCortexUrl, json=payload)

    # If the response isn't 200, this likely means it detected room noise only
    # ignoring it for now
    try:
        responseBody = json.loads(response.text)
        
        # Forwards to cerebrum
        q = Queue("corpus-callosum", connection=Redis("queue"))
        q.enqueue(cerebrum, responseBody, origin)
    except requests.exceptions.RequestException:
        return False
       