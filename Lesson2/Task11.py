def fib_def(x):
    counter = 3
    n1, n2= 1,1
    while n2<x:
        n1,n2=n2,n1+n2
        counter+=1
    if n2==x:    
        return counter
    else: return -1

my_res = fib_def(6765)
print(my_res)    
        
        
    