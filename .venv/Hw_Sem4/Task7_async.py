import asyncio
from random import randint
import aiohttp
import time


def fill_array():
    """Заполняем список случайными числами от 1 до 100
    Returns:
        _type_: array[]
    """
    arr = []
    for _ in range(1, 1000000):
        num = randint(1, 100)
        arr.append(num)
    return arr


async def sum_array(arr, slice):
    """Суммируем элементы из списка по указанному срезу.
    Args:
        arr (_type_): array[]
        slice (_type_): int
    """
    sum = 0
    for num in arr[:slice]:
        sum += num
    print(f"Посчитано за {time.time() - start_time:.2f} сек.")
    print(sum)

array = fill_array()


async def main():
    tasks = []
    for slice in range(333333, 999999, 333333):
        task = asyncio.ensure_future(sum_array(array, slice))
        tasks.append(task)
    await asyncio.gather(*tasks)
    
    
start_time = time.time()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())