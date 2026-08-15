from flask import Flask
import redis
import os

app = Flask(__name__)

#connect to redis server
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    #count logs/refresh to the website
    count = cache.incr('hits')
    return f'hello from Flask..This Page has been viewed {count} times.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)                       


