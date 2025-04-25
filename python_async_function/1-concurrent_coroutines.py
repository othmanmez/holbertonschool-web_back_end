#!/usr/bin/env python3
"""Concurrent coroutines example."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay in seconds

    Returns:
        List[float]: List of delays in ascending order
    """
    delays = []
    coroutines = []
    for number_coroutines in range(n):
        coroutines.append(wait_random(max_delay))

    for coroutine in asyncio.as_completed(coroutines):
        # Get results in order of completion
        delay = await coroutine
        delays.append(delay)

    return delays
