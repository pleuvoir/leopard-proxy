#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rpc.proto import agent_pb2 as agent_model, agent_pb2_grpc as agent_grpc


class Agent(agent_grpc.HelloServicer):

    def __init__(self):
        pass

    def SayHello(self, request, context):
        return agent_model.HelloReply(message=request.name)
