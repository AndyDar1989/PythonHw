# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

def pow_of_two(n):
    i=1
    p=1
    while p<=n:
        print(p, end=' ')
        p=2**i
        i+=1
        
        
pow_of_two(128)        
        