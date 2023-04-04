#!/usr/bin/env python3
"""Measure Time"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''Measure runtime'''
    start = time.perf_counter()
    p_list = []
    for _ in range(4):
        task = asyncio.create_task(async_comprehension())
        p_list.append(task)
    await asyncio.gather(*p_list)
    end = time.perf_counter() - start
    return end
