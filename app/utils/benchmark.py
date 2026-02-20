import time
import functools
import asyncio

def benchmark(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"🚀 {func.__name__} выполнена за {end_time - start_time:.4f} сек")
        return result
    return wrapper
