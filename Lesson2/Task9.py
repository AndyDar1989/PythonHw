#n = int(input('Enter number N: '))
def factorial(x):
    if x==0:
        return 1
    else:
        i = 1
        mult = 1
        while i<=x:
            mult *= i
            i+=1
        return mult

my_res = factorial(0)
print(my_res)        