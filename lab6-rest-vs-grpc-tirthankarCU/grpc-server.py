from concurrent import futures
import logging
import math
import time
import grpc
import lab6_pb2
import lab6_pb2_grpc
import jsonpickle
from PIL import Image
import numpy as np
import base64
import io
import numpy as np

class RouteGuideServicer(lab6_pb2_grpc.RouteGuideServicer):
    def add(self, request, context):
        return lab6_pb2.add_r(a=request.a+request.b)
    
    def rawImage(self,request,context):
        ioBuffer = io.BytesIO(request.img)
        img = Image.open(ioBuffer)
        return lab6_pb2.rawImage_r(a=img.size[0],b=img.size[1])

    def dotProduct(self,request,context):
        a=np.array(request.a)
        b=np.array(request.b)
        return lab6_pb2.dotProduct_r(a=np.sum(a*b))

    def jsonImage(self,request,context):
        image=base64.b64decode(request.img)
        ioBuffer = io.BytesIO(image)
        img = Image.open(ioBuffer)
        return lab6_pb2.jsonImage_r(a=img.size[0],b=img.size[1])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lab6_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
