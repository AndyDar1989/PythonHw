# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint

def eagle_tails(n):
    zero_count, one_count = 0,0
    for _ in range(n):
        val = randint(0,1)
        print(val, end=' ')
        if val==0:
            zero_count+=1
        if val==1:
            one_count +=1
    print()        
    if zero_count>one_count:
        print(one_count)
    else:
        print(zero_count)
        
        
eagle_tails(6)                        
            
        