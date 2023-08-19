from random import randint
from multiprocessing import Process, Pool
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
processes = []
start_time = time.time()

if __name__ == '__main__':
    for slice in range(333333, 999999, 333333):
        process = Process(target=sum_array, args=(array, slice))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()