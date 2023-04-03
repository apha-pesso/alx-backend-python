#!/usr/bin/env python3
"""Multiple coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Multiple coroutine'''
    """tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
    value = []
    for i in range(n):
        a = await wait_random(max_delay)
        value.append(a)
    return value
    """
    values = []
    for _ in range(n):
        values.append(wait_random(max_delay))
    res = await asyncio.gather(*values)
    return sorted(res)
