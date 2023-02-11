def erverse(n):
    
    x= input('Enter element: ')
    if n==1:
        return x
    return erverse(n-1)+x


print(erverse(int(input('Enter number of elements: '))))