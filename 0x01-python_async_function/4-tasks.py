#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks = []
    delays = []

    for m in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for i in asyncio.as_completed((tasks)):
        delay = await i
        delays.append(delay)

    return delays
