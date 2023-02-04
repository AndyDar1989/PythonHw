# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random_list import random_list


def closest_number(user_list, user_number):
    min_diff = user_number
    for i in user_list:
        diff = user_number-i
        if diff < 0:
            diff *= -1
        if diff < min_diff:
            min_diff = diff
    cl_num = set()
    for i in user_list:
        if user_number-i == min_diff or user_number-i == -min_diff:
            cl_num.add(i)
    return cl_num


my_list = random_list(int(input('Enter size of the list: ')))
print(my_list)
my_number = int(input('Enter the number: '))
print('The closest number for {}: {}'.format(
    my_number, closest_number(my_list, my_number)))
