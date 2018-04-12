from flask import Flask

app = Flask(__name__)


@app.route('/')
def pull_requests():
    return 'Hello world'
