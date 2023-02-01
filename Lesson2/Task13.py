import random

def temp(c):
    my_list = []
    plus_temp, max_plus_temp = 0,0
    for _ in range(c):#нижнее подчеркивание можно вместо итератора, если он дальше не используется
        d = random.randint(-50,50)# в randint диапазон включает крайние значения
        my_list.append(d)
        if d>0:
            plus_temp+=1
        else:
            if plus_temp>max_plus_temp:
                max_plus_temp = plus_temp
            plus_temp = 0
    if plus_temp>max_plus_temp:
        max_plus_temp = plus_temp            
    return my_list, max_plus_temp


a = int(input('Enter number from 0 to 100: '))
my_res = temp(a)
print(my_res)
    