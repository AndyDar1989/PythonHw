# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint


def min_move_numbers(n):
    zero_counter, one_counter = 0, 0
    for _ in range(n):
        val = randint(0, 1)
        print(val, end=' ')
        if val == 0:
            zero_counter += 1
        if val == 1:
            one_counter += 1
    print()
    if zero_counter > one_counter:
        print(one_counter)
    else:
        print(zero_counter)


min_move_numbers(2)
