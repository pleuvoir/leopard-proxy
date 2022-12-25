#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from concurrent import futures

import grpc

from rpc.agent import Agent
from rpc.proto import agent_pb2_grpc as agent_grpc
from utils import logger


async def start_grpc(addr="127.0.0.1:8888", max_workers=10) -> None:
    # 1.实例化server
    thread = futures.ThreadPoolExecutor(max_workers=max_workers)
    server = grpc.server(thread)
    # 2.注册实现类到server中
    agent_grpc.add_AgentServicer_to_server(Agent(), server)
    # 3.启动server
    server.add_insecure_port(addr)
    server.start()
    #server.wait_for_termination()
    logger.info("GRPC 已启动。")
