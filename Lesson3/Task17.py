# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

def diff_num(user_list):
    new_set=set(user_list)
    return new_set,(len(new_set))

my_list = [1, 1, 2, 0, -1, 3, 4, 4]
print(diff_num(my_list))

