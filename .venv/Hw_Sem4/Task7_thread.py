# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

# Task9 async with aiohttp.ClientSession() as session:
# async with session.get(url) as response:
# if response.status == 200:
# content = await response.read()

# filename = os.path.join('images', filename)
# async with aiofiles.open(filename, 'wb') as f:
# await f.write(content)

from random import randint
import threading
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


start_time = time.time()


def sum_array(arr, slice):
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
threads = []

for slice in range(333333, 999999, 333333):
    t = threading.Thread(target=sum_array, args=(array, slice))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()