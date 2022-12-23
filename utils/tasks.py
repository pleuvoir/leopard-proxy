# -*- coding:utf-8 -*-

"""
Tasks module.
1. Register a loop run task:
    a) assign a asynchronous callback function;
    b) assign a execute interval time(seconds), default is 1s.
    c) assign some input params like `*args, **kwargs`;
2. Register a single task to run:
    a) Create a coroutine and execute immediately.
    b) Create a coroutine and delay execute, delay time is seconds, default delay time is 0s.
"""

import asyncio
import inspect


__all__ = ("SingleTask", )


class SingleTask:
    """Single run task.
    """

    @classmethod
    def run(cls, func, *args, **kwargs):
        """Create a coroutine and execute immediately.

        Args:
            func: Asynchronous callback function.
        """
        asyncio.get_event_loop().create_task(func(*args, **kwargs))

    @classmethod
    def call_later(cls, func, delay=0, *args, **kwargs):
        """Create a coroutine and delay execute, delay time is seconds, default delay time is 0s.

        Args:
            func: Asynchronous callback function.
            delay: Delay time is seconds, default delay time is 0, you can assign a float e.g. 0.5, 2.3, 5.1 ...
        """
        if not inspect.iscoroutinefunction(func):
            asyncio.get_event_loop().call_later(delay, func, *args)
        else:
            def foo(f, *args, **kwargs):
                asyncio.get_event_loop().create_task(f(*args, **kwargs))
            asyncio.get_event_loop().call_later(delay, foo, func, *args)
