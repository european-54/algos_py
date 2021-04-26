"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75
Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
"""

def recursion(n):
    if n == 1:
        return 1
    return n + recursion(n - 1)
"""

"""

def recursion(a,b): # основное условие задачи


# Базовый случай
    if a == b:
        return str(a)

    if a > b:
# Шаг рекурсии / рекурсивное условие
        return str(a) + " " + str(recursion(a - 1, b))
    else:
# Шаг рекурсии / рекурсивное условие
        return str(a) + " " + str(recursion(a + 1, b))

print(recursion(20,15))
print(recursion(10,15))
"""
"""
n = input("Введите число п, где n - количество элементов:")


def sumList(n):

    def sumL(n,s,i):
        if i < 0:
            return s
        else:
            return sumL(n,s+n[i],i-1)
    return sumL(n,0,len(n)-1)


print(sumList(n))
"""


def get_sum_2(lst_obj):
    """Простая рекурсия"""
    # базовый случай!!!
    if len(lst_obj) == 1:
        return lst_obj[0]
    else:
        # шаг рекурсии
        return lst_obj[0] + get_sum_2(lst_obj[1:])


print(get_sum_2([1, -0.5, 0.25]))

