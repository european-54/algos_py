"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему
"""


from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

from timeit import Timer
# встроенная функция range
def test_range():
    my_lst = list(range(1000))
t4 = Timer("test_range()", "from __main__ import test_range")
print("list range ", t4.timeit(number=1000), "milliseconds")

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

   def test_range():
       my_lst = list(range(1000))


t4 = Timer("test_range()", "from __main__ import test_range")
print("list range ", t4.timeit(number=1000), "milliseconds")
