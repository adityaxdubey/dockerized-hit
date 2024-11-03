import os
import time
import redis
from flask import Flask
app = Flask(__name__)

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_RETRY_DELAY = float(os.getenv('REDIS_RETRY_DELAY', 0.5))  
REDIS_MAX_RETRIES = int(os.getenv('REDIS_MAX_RETRIES', 5))  \

cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

def get_hit_count():
    #this is retry logic
    retries = REDIS_MAX_RETRIES
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(REDIS_RETRY_DELAY)

@app.route('/')
def hello():
    #this is interface
    count = get_hit_count()
    return f'Hello, repeat offender! You have graced us with your presence {count} times - we must be doing something right! Thanks for coming back for more! \n'