#!/usr/bin/env python3
'''Change wait_n'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Change wait_n to task_wait_n'''
    values = []
    for _ in range(n):
        values.append(task_wait_random(max_delay))
    res = await asyncio.gather(*values)
    return sorted(res)
