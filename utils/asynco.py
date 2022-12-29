#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio


def run(func, *args, **kwargs):
    loop = asyncio.get_event_loop()
    task = loop.create_task(func(*args, **kwargs))
    loop.run_until_complete(task)


def run_forever(cs):
    asyncio.get_event_loop().run_forever()
