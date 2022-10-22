# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import lab6_pb2 as lab6__pb2


class RouteGuideStub(object):
    """Interface exported by the server.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add = channel.unary_unary(
                '/routeguide.RouteGuide/add',
                request_serializer=lab6__pb2.add_m.SerializeToString,
                response_deserializer=lab6__pb2.add_r.FromString,
                )
        self.rawImage = channel.unary_unary(
                '/routeguide.RouteGuide/rawImage',
                request_serializer=lab6__pb2.rawImage_m.SerializeToString,
                response_deserializer=lab6__pb2.rawImage_r.FromString,
                )
        self.dotProduct = channel.unary_unary(
                '/routeguide.RouteGuide/dotProduct',
                request_serializer=lab6__pb2.dotProduct_m.SerializeToString,
                response_deserializer=lab6__pb2.dotProduct_r.FromString,
                )
        self.jsonImage = channel.unary_unary(
                '/routeguide.RouteGuide/jsonImage',
                request_serializer=lab6__pb2.jsonImage_m.SerializeToString,
                response_deserializer=lab6__pb2.jsonImage_r.FromString,
                )


class RouteGuideServicer(object):
    """Interface exported by the server.
    """

    def add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def rawImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dotProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def jsonImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RouteGuideServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'add': grpc.unary_unary_rpc_method_handler(
                    servicer.add,
                    request_deserializer=lab6__pb2.add_m.FromString,
                    response_serializer=lab6__pb2.add_r.SerializeToString,
            ),
            'rawImage': grpc.unary_unary_rpc_method_handler(
                    servicer.rawImage,
                    request_deserializer=lab6__pb2.rawImage_m.FromString,
                    response_serializer=lab6__pb2.rawImage_r.SerializeToString,
            ),
            'dotProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.dotProduct,
                    request_deserializer=lab6__pb2.dotProduct_m.FromString,
                    response_serializer=lab6__pb2.dotProduct_r.SerializeToString,
            ),
            'jsonImage': grpc.unary_unary_rpc_method_handler(
                    servicer.jsonImage,
                    request_deserializer=lab6__pb2.jsonImage_m.FromString,
                    response_serializer=lab6__pb2.jsonImage_r.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'routeguide.RouteGuide', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RouteGuide(object):
    """Interface exported by the server.
    """

    @staticmethod
    def add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.RouteGuide/add',
            lab6__pb2.add_m.SerializeToString,
            lab6__pb2.add_r.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def rawImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.RouteGuide/rawImage',
            lab6__pb2.rawImage_m.SerializeToString,
            lab6__pb2.rawImage_r.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dotProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.RouteGuide/dotProduct',
            lab6__pb2.dotProduct_m.SerializeToString,
            lab6__pb2.dotProduct_r.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def jsonImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/routeguide.RouteGuide/jsonImage',
            lab6__pb2.jsonImage_m.SerializeToString,
            lab6__pb2.jsonImage_r.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
