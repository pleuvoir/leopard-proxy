import asyncio
import time

from cryptofeed import FeedHandler
from cryptofeed.exchanges import OKX
from cryptofeed.defines import TRADES, TICKER, CANDLES

from utils.decorator import async_method_locker
from utils.tasks import AsyncTask


async def ticker(t, receipt_timestamp):
    print(t)


async def trade(t, receipt_timestamp):
    print(t)


async def candles(t, receipt_timestamp):
    print(t)


@async_method_locker("feed")
async def feed():
    print("feed进来可")
    f = FeedHandler()

    f.add_feed(OKX(symbols=['BTC-USDT'], channels=[CANDLES],
               callbacks={TICKER: ticker, TRADES: trade, CANDLES: candles}))
    f.run()
    print("run")

@async_method_locker(name="test")
async def test():
    await test2()

async def test2():
    print(111)

def main():
    # f = FeedHandler()
    #
    # f.add_feed(OKX(symbols=['BTC-USDT'], channels=[CANDLES],
    #                callbacks={TICKER: ticker, TRADES: trade, CANDLES: candles}))

    AsyncTask.run(func= test)

    # loop = asyncio.get_event_loop()
    # task = loop.create_task(test)
    # print(task)
    # loop.run_until_complete(task)
    print(1)

    time.sleep(111)

if __name__ == '__main__':
    main()
