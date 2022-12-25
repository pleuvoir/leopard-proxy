#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

from config.configure import config
from utils import logger


class Proxy:

    def __init__(self):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)

    def _init_logger(self) -> None:
        logger.initLogger(**config.log)

    def _load_settings(self, config_module) -> None:
        config.loads(config_module)

    def _init_rabbitMQ(self) -> None:
        from utils.rabbitmq import MQCenter
        self.mq_center = MQCenter()

    def start(self, config_file):
        self._load_settings(config_file)
        self._init_logger()
        self._init_rabbitMQ()


async def candles(t, receipt_timestamp):
    print(t)
