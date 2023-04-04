#!/usr/bin/env python3
'''Async comprehension'''
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Async comprehension"""
    """
    list_n = []
    async for num in async_generator():
        list_n.append(num)
    return list_n
    """

    return [num async for num in async_generator()]
