#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from market.market import Subscribe, UnSubscribe, MARKET_TYPE_KLINE_5M
from rpc.proto import agent_pb2 as agent_model, agent_pb2_grpc as agent_grpc
from utils import logger


class Agent(agent_grpc.AgentServicer):

    def __init__(self):
        pass

    def Subscribe(self, request, context):
        logger.info("接收到订阅请求，", request)
        Subscribe(MARKET_TYPE_KLINE_5M, request.exchange, request.symbol, candles)
        return agent_model.RpcResult(success=True)

    def UnSubscribe(self, request, context):
        logger.info("接收到取消订阅请求，", request)
        UnSubscribe(MARKET_TYPE_KLINE_5M, request.exchange, request.symbol)
        return agent_model.RpcResult(success=True)


async def candles(t, receipt_timestamp):
    print(t)
