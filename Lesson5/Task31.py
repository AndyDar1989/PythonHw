def fib(n,fib_list=[0,1]):
    if len(fib_list)==n:
        return fib_list[-1]
    else:
        fib_list.append(fib_list[-2]+fib_list[-1])
        return fib(n,fib_list)
        
        
        
x= int(input('Enter number: '))
print(fib(x))    
    