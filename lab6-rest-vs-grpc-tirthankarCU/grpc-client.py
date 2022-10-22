# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide client."""

import sys
import time
import logging
import random
import grpc
import lab6_pb2
import lab6_pb2_grpc
import base64

def doRawImage(stub,debug=False):
    image = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    data=lab6_pb2.rawImage_m(img=image)
    response=stub.rawImage(data)
    if debug:
        print("Response is",response)

def doAdd(stub,debug=False):
    data=lab6_pb2.add_m(a=5,b=10)
    response=stub.add(data)
    if debug:
        print("Response is",response)

def doDotProduct(stub,debug=False):
    ax=[random.random() for i in range(100)]
    bx=[random.random() for i in range(100)]
    data=lab6_pb2.dotProduct_m(a=ax,b=bx)
    response=stub.dotProduct(data)
    if debug:
        print("Response is",response)

def doJsonImage(stub,debug=False):
    image = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
    image64=base64.b64encode(image).decode('utf-8')
    data=lab6_pb2.jsonImage_m(img=image64)
    response=stub.jsonImage(data)
    if debug:
        print("Response is",response)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <server ip> <cmd> <reps>")
        print(f"where <cmd> is one of add, rawImage, sum or jsonImage")
        print(f"and <reps> is the integer number of repititions for measurement")
    
    host = sys.argv[1]
    cmd = sys.argv[2]
    reps = int(sys.argv[3])

    addr = f"http://{host}:5000"
    print(f"Running {reps} reps against {addr}")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = lab6_pb2_grpc.RouteGuideStub(channel)
        if cmd == 'rawImage':
            start = time.perf_counter()
            for x in range(reps):
                doRawImage(stub)
            delta = ((time.perf_counter() - start)/reps)*1000
            print("Took", delta, "ms per operation")
        elif cmd == 'add':
            start = time.perf_counter()
            for x in range(reps):
                doAdd(stub)
            delta = ((time.perf_counter() - start)/reps)*1000
            print("Took", delta, "ms per operation")
        elif cmd == 'jsonImage':
            start = time.perf_counter()
            for x in range(reps):
                doJsonImage(stub)
            delta = ((time.perf_counter() - start)/reps)*1000
            print("Took", delta, "ms per operation")
        elif cmd == 'dotProduct':
            start = time.perf_counter()
            for x in range(reps):
                doDotProduct(stub)
            delta = ((time.perf_counter() - start)/reps)*1000
            print("Took", delta, "ms per operation")
        else:
            print("Unknown option", cmd)