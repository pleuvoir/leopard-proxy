#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from concurrent import futures

import grpc

from proxy import Proxy
from rpc.agent import Agent

from rpc.proto import agent_pb2_grpc as agent_grpc


def start_grpc() -> None:
    # 1.实例化server
    thread = futures.ThreadPoolExecutor(max_workers=10)
    server = grpc.server(thread)
    # 2.注册实现类到server中
    agent_grpc.add_HelloServicer_to_server(Agent(), server)
    # 3.启动server
    server.add_insecure_port("127.0.0.1:8888")
    server.start()
    server.wait_for_termination()


def start_market() -> None:
    proxy = Proxy()
    proxy.start("/Users/pleuvoir/dev/space/git/leopard-proxy/config.json")
    proxy.subscribe_market("okx", "BTC-USDT")
    proxy.mq_center.send("CANDLES", "routing_key", "i am message")


if __name__ == '__main__':
    start_grpc()
