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
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Create a sorted list without using sort()
    sorted_delays = []
    remaining = delays.copy()

    while remaining:
        min_delay = min(remaining)
        sorted_delays.append(min_delay)
        remaining.remove(min_delay)

    return sorted_delays