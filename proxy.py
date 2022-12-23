#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Type

from configure import config
from market.market import MARKET_TYPE_KLINE_5M, Market
from utils import logger


class Proxy:

    def __init__(self):
        super()

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

    def subscribe_market(self, exchange, symbol: str):
        Market(MARKET_TYPE_KLINE_5M, exchange, symbol, candles)


async def candles(t, receipt_timestamp):
    print(t)
