#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import time

from mq.rabbitmq import mqCenter
from utils import logger
from utils.tasks import AsyncTask

if __name__ == '__main__':
    from config.config import config

    config.loads("/Users/pleuvoir/dev/space/git/leopard-proxy/config/config.json")
    logger.initLogger(**config.log)

    AsyncTask.run(mqCenter.connect)

    send_param = {
        "exchange_name": "test",
        "routing_key": "roting_key",
        "data": "hehe"
    }

    AsyncTask.run(mqCenter.send, **send_param)

    # loop.run_until_complete(mqCenter.send("test","hehe","hh"))
