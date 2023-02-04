# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

def bigger_before(user_list):
    counter = 0
    for i in range(1,len(user_list)):
        if user_list[i]>user_list[i-1]:
            counter+=1
    return counter

my_list =  [0, -1, 5, 2, 3]
print(bigger_before(my_list))       