from random import randint

def random_list(list_size):
    new_list=[]
    for i in range(list_size):
        new_number = randint(1,list_size)
        new_list.append(new_number)
    return new_list