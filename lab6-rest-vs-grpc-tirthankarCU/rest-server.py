#!/usr/bin/env python3

##
## Sample Flask REST server implementing two methods
##
## Endpoint /api/image is a POST method taking a body containing an image
## It returns a JSON document providing the 'width' and 'height' of the
## image that was provided. The Python Image Library (pillow) is used to
## proce#ss the image
##
## Endpoint /api/add/X/Y is a post or get method returns a JSON body
## containing the sum of 'X' and 'Y'. The body of the request is ignored
##
##
from flask import Flask, request, Response
import jsonpickle
from PIL import Image
import numpy as np
import base64
import io

# Initialize the Flask application
app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

@app.route('/api/add/<int:a>/<int:b>', methods=['GET', 'POST'])
def add(a,b):
    response = {'sum' : str( a + b)}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

# route http posts to this method
@app.route('/api/rawimage', methods=['POST'])
def rawimage():
    r = request
    # convert the data to a PIL image type so we can extract dimensions
    try:
        ioBuffer = io.BytesIO(r.data)
        img = Image.open(ioBuffer)
    # build a response dict to send back to client
        response = {
            'width' : img.size[0],
            'height' : img.size[1]
            }
    except:
        response = { 'width' : 0, 'height' : 0}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/api/dotproduct', methods=['POST'])
def dotproduct():
    r=request
    json=jsonpickle.decode(r.data)
    a=json['a']
    b=json['b']
    a_sz=len(a)
    b_sz=len(b)
    padding=max(a_sz,b_sz)-min(a_sz,b_sz)
    if a_sz>b_sz:
        b=np.array(b+[0 for i in range(padding)])
        a=np.array(a)
    elif b_sz>a_sz:
        a=np.array(a+[0 for i in range(padding)])
        b=np.array(b)
    else:
        a=np.array(a)
        b=np.array(b)
    c=(np.sum(a*b)).tolist()
    response={'dotproduct':c}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

# route http posts to this method
@app.route('/api/jsonimage', methods=['POST'])
def jsonimage():
    r = request
    json=jsonpickle.decode(r.data)
    b64_img=json['image']
    img=base64.b64decode(b64_img)
    try:
        ioBuffer = io.BytesIO(img)
        img = Image.open(ioBuffer)
        response = {
            'width' : img.size[0],
            'height' : img.size[1]
            }
    except:
        response = { 'width' : 0, 'height' : 0}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

# start flask app
app.run(host="0.0.0.0", port=5000)
