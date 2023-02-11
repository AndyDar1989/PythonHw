# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.


def user_enter(x):
    user_list = []
    for _ in range(x):
        user_list.append(int(input('Enter value: ')))
    return user_list


def sort_set(list_1, list_2):
    sort_set = set(list_1).intersection(set(list_2))
    return sort_set


n = int(input('Enter number of the elements for the first set: '))
m = int(input('Enter number of the elements for the first set: '))

my_list_1 = user_enter(n)
print(my_list_1)
my_list_2 = user_enter(m)
print(my_list_2)
print(sort_set(my_list_1, my_list_2))
