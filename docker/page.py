import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/')

def hello():
    return 'Welcome to SCA Cloud School Application, this is my first assessment'
