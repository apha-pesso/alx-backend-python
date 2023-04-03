#!/usr/bin/env python3
'''Measure RUntime'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure runtime"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() - start
    return (total / n)
