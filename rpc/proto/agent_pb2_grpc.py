# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from rpc.proto import agent_pb2 as agent__pb2


class AgentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.unary_unary(
                '/services.Agent/Subscribe',
                request_serializer=agent__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=agent__pb2.RpcResult.FromString,
                )
        self.UnSubscribe = channel.unary_unary(
                '/services.Agent/UnSubscribe',
                request_serializer=agent__pb2.UnSubscribeRequest.SerializeToString,
                response_deserializer=agent__pb2.RpcResult.FromString,
                )


class AgentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnSubscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=agent__pb2.SubscribeRequest.FromString,
                    response_serializer=agent__pb2.RpcResult.SerializeToString,
            ),
            'UnSubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.UnSubscribe,
                    request_deserializer=agent__pb2.UnSubscribeRequest.FromString,
                    response_serializer=agent__pb2.RpcResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'services.Agent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Agent(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.Agent/Subscribe',
            agent__pb2.SubscribeRequest.SerializeToString,
            agent__pb2.RpcResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnSubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/services.Agent/UnSubscribe',
            agent__pb2.UnSubscribeRequest.SerializeToString,
            agent__pb2.RpcResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
