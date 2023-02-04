# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

from random_list import random_list


def find_repeat_number(user_list, user_number):
    counter = 0
    for i in user_list:
        if i == user_number:
            counter += 1
    return counter


my_list = random_list(int(input('Enter size of the list: ')))
print(my_list)
my_number = int(input('Enter the number: '))
print('Number of repeats {}: {}'.format(
    my_number, find_repeat_number(my_list, my_number)))
