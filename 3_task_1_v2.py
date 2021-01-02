"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


import timeit
def fill_list(n):
    my_list = []
    for i in range(n): 
        my_list.append(i)
        my_list.append(i)
    return my_list

def fill_dict(n):
    my_dict = {}
    for i in range(n): 
        my_dict[i] = i
    return my_dict
k = int(input("Input numbers elements for compare time filling  list and dict: "))
print (f" fill_list({k}) {fill_list(k)}")
print(f" fill_dict({k}){fill_dict(k)}")
print(f"test time for fill_list({k}) ",end="")
print(timeit.timeit("fill_list(10)", setup="from __main__ import fill_list"))
print(f"test time for fill_dict({k}) ",end="")
print(timeit.timeit("fill_dict(10)", setup="from __main__ import fill_dict"))

