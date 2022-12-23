#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cryptofeed import FeedHandler
from cryptofeed.exchanges import OKX, Gateio

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


class Market:

    def __init__(self, market_type, exchange, symbol, callback):
        if market_type in [
            MARKET_TYPE_KLINE, MARKET_TYPE_KLINE_3M, MARKET_TYPE_KLINE_5M,
            MARKET_TYPE_KLINE_15M, MARKET_TYPE_KLINE_30M, MARKET_TYPE_KLINE_1H,
            MARKET_TYPE_KLINE_3H, MARKET_TYPE_KLINE_6H, MARKET_TYPE_KLINE_12H,
            MARKET_TYPE_KLINE_1D, MARKET_TYPE_KLINE_3D, MARKET_TYPE_KLINE_1W,
            MARKET_TYPE_KLINE_15D, MARKET_TYPE_KLINE_1MON, MARKET_TYPE_KLINE_1Y]:

            from cryptofeed.defines import TRADES, TICKER, CANDLES

            f = FeedHandler()

            if exchange == 'okx':
                f.add_feed(OKX(symbols=[symbol], channels=[CANDLES],
                               callbacks={CANDLES: callback}))
            elif exchange == "gateio":
                f.add_feed(Gateio(symbols=[symbol], channels=[CANDLES],
                               callbacks={CANDLES: callback}))
            f.run()
        else:
            print("未找到")
