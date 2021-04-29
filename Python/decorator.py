# -*- coding: utf-8 -*-
# Author    ：Yang Ming
# Create at ：2021/4/26
# tool      ：PyCharm
import functools
import time
from collections import defaultdict


## decorator for method

def time_cost(func):
    @functools.wraps(func)
    # to let time_cost(func).__name__ = func.__name__ instead of wrapper
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"result={result},time={end - begin}/s")
    #
    return wrapper

@time_cost
def my_func(sleep_time):
    time.sleep(sleep_time)
    return 'done'

my_func(0.5)
print("name = ",my_func.__name__)

## decorator with args
# I wrote a time cost decorator which is capable of customizing the time unit as requirements
def time_cost_a(unit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            begin = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            if unit == 's':
                print(f"result={result},time={end - begin}/s")
            elif unit == 'min':
                print(f"result={result},time={(end - begin)//60}/min")
        return wrapper
    return decorator

@time_cost_a(unit='min')
def my_func(sleep_time):
    time.sleep(sleep_time)
    return 'done'

# my_func(60)


## class decorator

class TimeCost:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        begin = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"result={result},time={end - begin}/s")

@TimeCost
def my_func(sleep_time):
    time.sleep(sleep_time)
    return 'done'


# decorator for class
## Singleton Implementation

class SingletonDecorator:
    _instance = defaultdict(None)

    def __new__(cls, *args, **kwargs):
        if not cls._instance[cls.__name__]:
            cls._instance[cls.__name__] = type(cls.__name__, cls.__base__)
        return cls._instance[cls.__name__]

@SingletonDecorator
class MyObject:
    a = 1

class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)

@Singleton
class DBConnection(object):

    def __init__(self):
        """Initialize your database connection here."""
        pass

    def __str__(self):
        return 'Database connection object'

c1 = DBConnection.Instance()
c2 = DBConnection

print("Id of c1 : {}".format(str(id(c1))))
print("Id of c2 : {}".format(str(id(c1))))

print("c1 is c2 ? " + str(c1 is c2))


## async decorator

import time
from loguru import logger
import functools
import asyncio

def time_cost(func):
    if asyncio.iscoroutinefunction(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            out = await func(*args, **kwargs)
            duration = time.time() - start_time
            logger.info(f'{func.__name__} executed in {duration:.4f} s')
            return out
    else:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            out = func(*args, **kwargs)
            duration = time.time() - start_time
            logger.info(f'{func.__name__} executed in {duration:.4f} s')
            return out

    return wrapper