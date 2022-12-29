#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import os

import grpc

from config.config import config
from mq.rabbitmq import mqCenter
from rpc import grpc
from utils import logger
from utils.tasks import Async


def run(config_path: str):
    # 加载配置文件
    config.loads(config_path)
    # 初始化日志
    logger.initLogger(**config.log)
    # 连接MQ
    Async.run(mqCenter.connect)
    # 启动grpc
    Async.run(grpc.start_grpc, **config.grpc)
    logger.info("启动完成。")


if __name__ == '__main__':
    run(os.path.join(os.getcwd(), "config/config.json"))
    Async.run_forever()
