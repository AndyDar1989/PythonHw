# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

def shift(user_list, k):
    for _ in range(k):
        x=user_list.pop(0)
        user_list.append(x)
    return user_list



my_list = [1, 2, 3, 4, 5]
print(my_list[::-1])#-1 разворачивает список при выведении
print(my_list[::2])#2 указывается шаг, в данном случае будет выводить через один
k=3
my_list = my_list[k:]+my_list[:k]
#print(shift(my_list, 3))
print(my_list)

        
    
    