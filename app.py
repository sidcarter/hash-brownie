#!/usr/bin/env python

"""
A simple example of a message hasher
bottled in a docker image

Author: Sid Carter
"""

from hashlib import sha256
import redis
from flask import (
    Flask,
    request,
    jsonify,
    abort
)

app = Flask(__name__)

# we set charset here, so redis response doesn't byte back ;)
# see: python 3.x
redis = redis.StrictRedis(host='redis', charset="utf-8", decode_responses=True)

@app.route("/")
def welcome():
    """ We soft redirect using soft language on accessing root """
    return "You should try {}messages. Fun stuff happens there. ;)".format(request.url)

@app.route("/messages", methods=['POST'])
def digester():
    """
    here, we get the message,
    calculate the hash,
    then store it
    in the cache
    """
    data = request.get_json()

    try:
        message = data['message']
        sha256_sum = sha256(message.encode('utf-8')).hexdigest()
    except (KeyError, AttributeError):
        # for when data is empty or when message is not a string
        abort(400)

    # store in redis to retrieve later
    redis.set(sha256_sum, message)
    return (jsonify(digest=sha256_sum), 201)

@app.route("/messages/<sha256_sum>", methods=['GET'])
def messager(sha256_sum):
    """
    we try and get
    our hash
    from the cache

    on failure,
    we go 404
    """
    message = redis.get(sha256_sum)

    if message != None:
        return jsonify(message=message)
    else:
        # for when we get an nil response from redis
        return (jsonify(err_msg="Message not found"), 404)

if __name__ == "__main__":
    context = ('localhost.crt', 'sslkey/localhost.key')
    app.run(host='0.0.0.0', ssl_context=context, threaded=True, debug=True, port=4000)
