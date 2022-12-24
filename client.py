#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import grpc
from rpc.proto import agent_pb2, agent_pb2_grpc


# rpc调用
def main():
    # 这里使用with，调用完会自动关闭。优雅写法
    with grpc.insecure_channel("127.0.0.1:8888") as channel:
        stub = agent_pb2_grpc.GreeterStub(channel)
        # 调用定义的SayHello方法
        rep = stub.SayHello(
            agent_pb2.HelloRequest(name="jeff")  # 传递定义的HelloRequest类型参数
        )
        return rep


# 业务代码
def start():
    rep = main()
    print(rep.message)  # 你好，jeff


if __name__ == '__main__':
    start()