from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/jobs')
def jobs():
    url = 'https://my-json-server.typicode.com/jjjosephhh/test-db-002/people'
    r = requests.get(url)
    response = r.json()
    rows = response
    return render_template('jobs.html', rows = rows)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)