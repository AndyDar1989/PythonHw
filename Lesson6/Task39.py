def fill_list(n):
    user_list = []
    for _ in range(n):
        user_list.append(int(input('Enter number: ')))
    return user_list

def diff_btw_lists(list_1, list_2):
    diff_list = []
    for i in list_1:
        if i not in list_2:
            diff_list.append(i)
    return diff_list

#def diff_btw_lists(list_1, list_2):
#   return[i for i in list_1 if i not in list_2]


my_list_1 = fill_list(7)
print(my_list_1)
my_list_2 = fill_list(6)
print(my_list_2)
print(diff_btw_lists(my_list_1,my_list_2))        
            
    
        