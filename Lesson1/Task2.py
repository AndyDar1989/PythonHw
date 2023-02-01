# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input('Enter number: '))
sum_digits = 0
while a > 0:
    sum_digits += a % 10
    a = a//10
print(sum_digits)
