def fill_list(n):
    user_list = []
    for _ in range(n):
        user_list.append(int(input('Enter number: ')))
    return user_list

def count_pairs(user_list):
    counter = 0
    for i in range(1, len(user_list)-1):
        if user_list[i-1]+user_list[i]==user_list[i]+user_list[i+1]:
            counter+=1
    return counter

my_list_1 = fill_list(5)
print(my_list_1)

print(count_pairs(my_list_1))        