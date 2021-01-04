"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""

import timeit

def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))

n = i

def eratosthenes(n):     # n - число, до которого хотим найти простые числа 
    sieve = list(range(n + 1))
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve



print ("time for eratosthenes")
print(timeit.timeit("eratosthenes(n)","from __main__ import (eratosthenes,n)"))
#print("time for simple")
#print(timeit.timeit("simple(i)","from __main__ import (simple,i)"))

print ("time for eratosthenes 10")
print(timeit.timeit("eratosthenes(10)","from __main__ import (eratosthenes,n)"))
print ("time for eratosthenes 100")
print(timeit.timeit("eratosthenes(100)","from __main__ import (eratosthenes,n)"))
print ("time for eratosthenes 1000")
print(timeit.timeit("eratosthenes(1000)","from __main__ import (eratosthenes,n)"))

"""
Введите порядковый номер искомого простого числа: 3
5
time for eratosthenes
1.8120533000000005
time for eratosthenes 10
4.0925241
time for eratosthenes 100
29.5251326
time for eratosthenes 1000
334.4546802
"""

"""
по результатам выше можно предположить, что сложность алгоритма чуть больше линейной
сложность простого алгоритма - квадратичная
"""



