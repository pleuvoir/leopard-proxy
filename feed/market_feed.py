from cryptofeed import FeedHandler
from cryptofeed.exchanges import OKX
from cryptofeed.defines import TRADES, TICKER, CANDLES


async def ticker(t, receipt_timestamp):
    print(t)


async def trade(t, receipt_timestamp):
    print(t)


async def candles(t, receipt_timestamp):
    print(t)


def main():
    f = FeedHandler()

    f.add_feed(OKX(symbols=['STARL-USDT'], channels=[CANDLES],
                   callbacks={TICKER: ticker, TRADES: trade, CANDLES: candles}))

    f.run()


if __name__ == '__main__':
    main()
