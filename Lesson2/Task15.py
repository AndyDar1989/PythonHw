import random

def weight_choice(c):
    my_list = []
    for _ in range(c):
        w = random.randint(1,10)
        my_list.append(w)
    min_weight, max_weight = my_list[0],1    
    for i in range(c):    
        if my_list[i]>max_weight:
            max_weight=my_list[i]
        if my_list[i]<min_weight:
            min_weight = my_list[i]           
    return my_list, min_weight, max_weight


a = int(input('Enter number from 0 to 10: '))
my_choice = weight_choice(a)
print(my_choice)