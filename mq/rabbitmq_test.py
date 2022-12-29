#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mq.rabbitmq import mqCenter
from utils import asynco
from utils import logger

if __name__ == '__main__':
    from config.config import config

    config.loads("/Users/pleuvoir/dev/space/git/leopard-proxy/config/config.json")
    logger.initLogger(**config.log)

    exchange_name = "test-exchange"
    queue_name = "test-queue"
    routing_key = "test-routing-key"

    asynco.run(mqCenter.connect)
    asynco.run(mqCenter.exchange_declare, **{"exchange_name": exchange_name, "type_name": "topic"})
    asynco.run(mqCenter.queue_declare, **{"queue_name": queue_name})
    asynco.run(
        mqCenter.queue_bind_exchange,
        **{"queue_name": queue_name, "exchange_name": exchange_name, "routing_key": routing_key})

    asynco.run(mqCenter.send, **{
        "exchange_name": exchange_name,
        "routing_key": routing_key,
        "data": "hehe"
    })
