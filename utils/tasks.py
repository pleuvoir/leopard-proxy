#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio

__all__ = "AsyncTask"


class AsyncTask:

    @classmethod
    def run(cls, func, *args, **kwargs):
        """Create a coroutine and execute immediately.

        Args:
            func: Asynchronous callback function.
        """
        loop = asyncio.get_event_loop()
        task = loop.create_task(func(*args, **kwargs))
        loop.run_until_complete(task)

    @classmethod
    def run_forever(cls):
        asyncio.get_event_loop().run_forever()
