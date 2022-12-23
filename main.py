#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from proxy import Proxy




if __name__ == '__main__':
    proxy = Proxy()
    proxy.start("/Users/pleuvoir/dev/space/git/leopard-proxy/config.json")

    proxy.subscribe_market("okx","BTC-USDT")

    proxy.mq_center.send("CANDLES","routing_key","i am message")