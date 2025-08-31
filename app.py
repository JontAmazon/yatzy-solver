import os
import time
from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

# store last run time globally
last_run_time = 0
RATE_LIMIT_SECONDS = 0.7

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_game():
    global last_run_time
    now = time.time()
    if now - last_run_time < RATE_LIMIT_SECONDS:
        return jsonify({'output': 'Error: Please wait before running again.'})

    last_run_time = now
    try:
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = e.stderr
    return jsonify({'output': output})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
