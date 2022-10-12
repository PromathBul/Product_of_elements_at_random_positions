import os
from Create_lists import create_list_from_minusN_to_N as original
from Create_lists import input_num
from Create_lists import create_random_list as random_l

os.system('cls')

number = input_num('Введите чило: ')
print('Исходный массив:')
my_list = original(number)
print(my_list)

print('Массив индексов')
indexes_list = random_l(len(my_list))
print(indexes_list)

print('Результат произведения элементов изначального массива с индексами, находящимися в массиве индексов:')
product = 1
for i in indexes_list:
    print(my_list[i], end='')
    if indexes_list.index(i) < len(indexes_list) - 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    product *= my_list[i]

print(product)