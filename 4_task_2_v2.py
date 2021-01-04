"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""


import timeit

def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g

def recursive_reverse(number):
    if number == 0:
        return ""
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'
@memorize
def recursive_reverse_mem(number):
    if number == 0:
        return ""
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

for number in (1234,12345,123456):
    print(f"1000000 reverses {number} -> {recursive_reverse_mem(number)}  ")
    print(f"by recursive_reverse({number}) takes ",end="\t")
    print(timeit.timeit("recursive_reverse(number)","from __main__ import (recursive_reverse,number)"))
    print(f"by recursive_reverse_mem({number}) takes ",end="\t")
    print(timeit.timeit("recursive_reverse_mem(number)","from __main__ import (recursive_reverse_mem,number)"))

 """
добавление декоратора @memorize, сохраняющего значения рекурсивной функции, позволяет ускорить
выполнение программы, избежав повторных вычислений
"""

 
