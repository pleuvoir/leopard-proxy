#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

import aioamqp

from utils import logger


class MqCenter():

    def __init__(self):
        self._connected = False

    async def connect(self, host="localhost", port=5672, username="guest", password="guest") -> bool:

        logger.info("host:", host, "port:", port, caller=self)
        if self._connected:
            return True

        try:
            transport, protocol = await aioamqp.connect(host=host, port=port, login=username,
                                                        password=password, login_method="PLAIN")
        except Exception as e:
            logger.error("connection error:", e, caller=self)
            return False

        channel = await protocol.channel()
        self._protocol = protocol
        self._channel = channel
        self._connected = True
        logger.info("RabbitMQ 连接成功。", caller=self)

    async def send(self, exchange_name, routing_key, data: str):
        if not self._connected:
            logger.error("RabbitMQ 未连接", caller=self)
            return
        await self._channel.basic_publish(payload=bytes(data, encoding="utf-8"), exchange_name=exchange_name,
                                          routing_key=routing_key)
        logger.info(f'RabbitMQ 消息发送成功。{data}，{exchange_name}，{routing_key}', caller=self)


mqCenter = MqCenter()
