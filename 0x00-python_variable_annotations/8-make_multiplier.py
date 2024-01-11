#!/usr/bin/env python3
'''Write a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier
