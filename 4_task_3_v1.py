"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import timeit
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

number = int(input("Input number "))

print(f"1000000 revers() {number} -> {revers_3((number))}  ")
print(f"by revers({number})   takes ",end="\t")
print(timeit.timeit("revers(number,revers_num=0)","from __main__ import (revers,number)"))
print(f"by revers_1({number}) takes ",end="\t")
print(timeit.timeit("revers_2(number,revers_num=0)","from __main__ import (revers_2,number)"))   
print(f"by revers_3({number}) takes ",end="\t")
print(timeit.timeit("revers_3(number)","from __main__ import (revers_3,number)"))
print()
cProfile.run("revers(number,revers_num=0)")
cProfile.run("revers_2(number,revers_num=0)")
cProfile.run("revers_3(number)")


"""
Профилировка с помощью timeit показывает, что функция номер 3 работает быстрее
cProfile показывает, что рекурсивная функция вызывается 4 раза при обработке (123). Этим обусловлена её
медленная работа.
Встроенная функция работает быстрее всего.
"""


