from app.jobs.auditory_cortex import auditory_cortex
from app.jobs.cerebrum import cerebrum
from flask import Flask, request, jsonify
from redis import Redis
from rq import Queue
import json

app = Flask(__name__)
q = Queue("corpus-callosum", connection=Redis("queue"))

@app.route('/', methods=['POST'])
def run():
    if not request.json or not 'action' in request.json:
        return jsonify({'error': 'Missing action'}), 400

    if not request.json or not 'origin' in request.json:
        return jsonify({'error': 'Missing origin'}), 400
    
    triage_result = runTriage(request.json)

    if triage_result == True:
        return jsonify({'success': 'action queued'});
    else:
        return jsonify({'error': 'action not identified or lacks sufficient data'}), 400;

# The triage finds meaning out of the request received and queues the appropriate job
def runTriage(request_data):
    # Commands
    if request_data['action'] == "command":
        queueCommand(request_data['origin'], request_data['parameters'])
        return True
    else:
        return False

def queueCommand(origin, parameters):
    if 'audio' in parameters:
        q.enqueue(auditory_cortex, parameters['audio'], origin)
    elif 'text' in parameters:
        q.enqueue(cerebrum, parameters['text'], origin)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)