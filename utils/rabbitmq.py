# -*— coding:utf-8 -*-


import asyncio
import sys

import aioamqp

from config.configure import config
from utils import logger


class MQCenter:
    def __init__(self):
        self._host = config.rabbitmq.get("host", "localhost")
        self._port = config.rabbitmq.get("port", 5672)
        self._username = config.rabbitmq.get("username", "guest")
        self._password = config.rabbitmq.get("password", "guest")
        self._protocol = None
        self._channel = None  # Connection channel.
        self._connected = False  # If connect success.

        # Create MQ connection.
        complete = asyncio.get_event_loop().run_until_complete(self.connect())
        if complete:
            logger.info("RabbitMQ connect success..")
        else:
            logger.error("RabbitMQ 连接失败，程序不启动。")
            sys.exit(-1)

    async def send(self, exchange_name, routing_key, data: str):
        if not self._connected:
            logger.warn("RabbitMQ not ready right now!", caller=self)
            return
        await self._channel.basic_publish(payload=data, exchange_name=exchange_name, routing_key=routing_key)

    async def connect(self) -> bool:
        logger.info("host:", self._host, "port:", self._port, caller=self)
        if self._connected:
            return True

        try:
            transport, protocol = await aioamqp.connect(host=self._host, port=self._port, login=self._username,
                                                        password=self._password, login_method="PLAIN")
        except Exception as e:
            logger.error("connection error:", e, caller=self)
            return False

        channel = await protocol.channel()
        self._protocol = protocol
        self._channel = channel
        self._connected = True
        logger.info("Rabbitmq initialize success!", caller=self)

        # Create default exchanges.
        exchanges = ["CANDLES"]
        for name in exchanges:
            await self._channel.exchange_declare(exchange_name=name, type_name="topic")
        logger.info("create default exchanges success!", caller=self)
        return True

    async def _initialize(self, queue_name, exchange_name, routing_key: str):
        await self._channel.queue_declare(queue_name=queue_name, auto_delete=True)
        await self._channel.queue_bind(queue_name=queue_name, exchange_name=exchange_name,
                                       routing_key=routing_key)



mqCenter = MQCenter()