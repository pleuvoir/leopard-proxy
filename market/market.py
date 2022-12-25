#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from concurrent.futures import ThreadPoolExecutor

from cryptofeed import FeedHandler
from cryptofeed.exchanges import OKX, Gateio

from utils import logger

MARKET_TYPE_KLINE = "kline"
MARKET_TYPE_KLINE_3M = "kline_3m"
MARKET_TYPE_KLINE_5M = "kline_5m"
MARKET_TYPE_KLINE_15M = "kline_15m"
MARKET_TYPE_KLINE_30M = "kline_30m"
MARKET_TYPE_KLINE_1H = "kline_1h"
MARKET_TYPE_KLINE_3H = "kline_3h"
MARKET_TYPE_KLINE_6H = "kline_6h"
MARKET_TYPE_KLINE_12H = "kline_12h"
MARKET_TYPE_KLINE_1D = "kline_1d"
MARKET_TYPE_KLINE_3D = "kline_3d"
MARKET_TYPE_KLINE_1W = "kline_1w"
MARKET_TYPE_KLINE_15D = "kline_15d"
MARKET_TYPE_KLINE_1MON = "kline_1mon"
MARKET_TYPE_KLINE_1Y = "kline_1y"

feed = FeedHandler()
pool_executor = ThreadPoolExecutor(max_workers=15, thread_name_prefix='market-')

SUBSCRIBE_MAP = {}


def Subscribe(market_type, exchange, symbol, callback):
    if SUBSCRIBE_MAP.get(f'{market_type}_{exchange}_{symbol}'):
        logger.warn(f'feed已订阅过，跳过 -> {exchange} - {symbol}。')
        return

    f = pool_executor.submit(_subscribe, market_type=market_type, exchange=exchange, symbol=symbol,
                             callback=callback)
    # exception = f.exception(timeout=3)  这个方法会阻塞
    # if exception:
    #     logger.error(f'feed订阅失败 -> {exchange} - {symbol}。{exception}')
    #     return
    SUBSCRIBE_MAP[f'{market_type}_{exchange}_{symbol}'] = True


def UnSubscribe(market_type, exchange, symbol):
    pass


def _subscribe(market_type, exchange, symbol, callback):
    if market_type in [
        MARKET_TYPE_KLINE, MARKET_TYPE_KLINE_3M, MARKET_TYPE_KLINE_5M,
        MARKET_TYPE_KLINE_15M, MARKET_TYPE_KLINE_30M, MARKET_TYPE_KLINE_1H,
        MARKET_TYPE_KLINE_3H, MARKET_TYPE_KLINE_6H, MARKET_TYPE_KLINE_12H,
        MARKET_TYPE_KLINE_1D, MARKET_TYPE_KLINE_3D, MARKET_TYPE_KLINE_1W,
        MARKET_TYPE_KLINE_15D, MARKET_TYPE_KLINE_1MON, MARKET_TYPE_KLINE_1Y]:

        from cryptofeed.defines import TRADES, TICKER, CANDLES
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        if exchange == 'okx':
            feed.add_feed(OKX(symbols=[symbol], channels=[CANDLES],
                              callbacks={CANDLES: callback}))
            logger.info(f'feed已订阅 -> {exchange} - {symbol}。')
        elif exchange == "gateio":
            feed.add_feed(Gateio(symbols=[symbol], channels=[CANDLES],
                                 callbacks={CANDLES: callback}))
            logger.info(f'feed已订阅 -> {exchange} - {symbol}。')
        feed.run(start_loop=True, install_signal_handlers=False)
    else:
        logger.error(f'feed未找到市场忽略 -> {exchange} - {symbol}。')
