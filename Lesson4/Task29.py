#Ваня:
n = int(input('Enter number: '))
max_number = n
while n != 0:
    n = int(input())
    if max_number < n:
        max_number = n
print(f' Max number is: {max_number}')

#Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)