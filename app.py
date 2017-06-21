from redis import Redis
from rq import Queue
from flask import Flask, request, jsonify
from app.jobs.auditory_cortex import auditory_cortex
from app.jobs.cerebrum import cerebrum
import json

app = Flask(__name__)
q = Queue("corpus-callosum", connection=Redis("queue"))

@app.route('/', methods=['POST'])
def run():
    if not request.json or not 'action' in request.json:
        return jsonify({'error': 'Missing action'}), 400
    
    triage_result = runTriage(request.json)

    if triage_result == True:
        return jsonify({'success': 'action queued'});
    else:
        return jsonify({'error': 'action not identified or lacks sufficient data'}), 400;

# The triage finds meaning out of the request received and queues the appropriate job
def runTriage(request_data):
    # Commands
    if request_data['action'] == "command":
        if 'audio' in request_data['parameters']:
            q.enqueue(auditory_cortex, request_data['parameters']['audio'])
        elif 'text' in request_data.paramters:
            q.enqueue(cerebrum, request_data['parameters']['text'])
        else:
            return False

    return True


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)