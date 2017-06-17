from redis import Redis
from rq import Queue
from app.jobs.count_words_at_url import count_words_at_url
from flask import Flask, request, jsonify

app = Flask(__name__)
q = Queue(connection=Redis("queue"))

@app.route('/', methods=['POST'])
def run():
    if not request.json or not 'job' in request.json:
        return jsonify({'error': 'Missing job'}), 400
    
    result = q.enqueue(count_words_at_url, 'http://nvie.com')

    return jsonify({'success': 'action queued'});

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)