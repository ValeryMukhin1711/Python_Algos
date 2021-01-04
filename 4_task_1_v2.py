"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import timeit
import array
import cProfile

def func_1(nums): 
    new_arr = [] 
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_1_int_arr(nums): # попытка ускорить за счет предварительного определения типа массива
    new_arr = array.array('i',) # принудительно задаётся массив типа int
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1_check_last_bit(nums): # попытка ускорить за счёт отказа от деления и проверки значения последнего бита.
    new_arr = [] # поскольку битовые операции выполняются быстрее
    for i in range(len(nums)):
        if nums[i]&1 == 0:
            new_arr.append(i)
    return new_arr

def func_dict_keys(nums): # так как обращение к словарю быстрее, чем к списку,
    new_arr = [] # попытка использовать словарь
    new_dict ={}
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_dict[i] = ""
    #new_arr = array.array('i',new_dict.keys())        
    return new_dict.keys()

def func_allocate_memory(nums): # попытка сэкономить время за счёт предварительного выделения места для массива
    new_arr = [0]*len(nums)
    k = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr[k]=i
            k +=1
    return new_arr[0:k]
def func__iter(nums): # формирование массива в одну строчку с помощью итератора
    new_arr = [i for i  in range(len(nums)) if  nums[i] % 2 == 0]
    return new_arr
def func__iter_1(nums): # формирование итератора в return
    return [i for i  in range(len(nums)) if  nums[i] % 2 == 0]


def func_list (nums): # попытка использования функции list
        return list(i for i  in range(len(nums)) if  nums[i] % 2 == 0)


int_array = array.array('i', range(1,5))
print(int_array)
res ={}

print (f"new_array_1 {func_1(int_array)}")
print (f"func_1_check_last_bit {func_1_check_last_bit(int_array)}")
print (f"new_array_2 {func_dict_keys(int_array)}")
print (f"new_array_0 {func_1_int_arr(int_array)}")
print (f"new_array_3 {func_allocate_memory(int_array)}")
print (f"new_array_4 {func__iter(int_array)}")
print (f"new_array_4_1 {func__iter_1(int_array)}")
print (f"new_array_5 {func_list(int_array)}")

# запись названий функций и времени их выполнения в словарь
print("Calculate time using timeit and sort results")
res['func_1']= round(timeit.timeit("func_1(int_array)", setup="from __main__ import (func_1,   int_array)"),9)
res['func_dict_keys']= round(timeit.timeit("func_dict_keys(int_array)", setup="from __main__ import (func_dict_keys,   int_array)"),9)
res['func_1_int_arr']= round(timeit.timeit("func_1_int_arr(int_array)", setup="from __main__ import (func_1_int_arr,   int_array)"),9)
res['func__iter']= round(timeit.timeit("func__iter(int_array)", setup="from __main__ import (func__iter,   int_array)"),9)
res['func__iter_1']= round(timeit.timeit("func__iter_1(int_array)", setup="from __main__ import (func__iter_1,   int_array)"),9)
res['func_1_check_last_bit']= round(timeit.timeit("func_1_check_last_bit(int_array)", setup="from __main__ import (func_1_check_last_bit,   int_array)"),9)
res['func_list']= round(timeit.timeit("func_list(int_array)", setup="from __main__ import (func_list,   int_array)"),9)

#вывод словаря в отсортированном виде
list_res = list(res.items())
list_res.sort(key=lambda i: i[1])
for i in list_res:
    print(i[1], '\t:', i[0])

# ни за счёт способа формирования массива, ни за счёт определения чётности ускорить не удалось
    
