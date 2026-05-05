# '/api/v1/details'
# '/api/v1/health'

from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'hostname': socket.gethostname(),
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)