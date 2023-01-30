
sum=0
i = 3
while i>0:
        a = int(input('Enter number: '))
        if a%2!=0:
            sum+=a//2+1
        else:
            sum+=a//2
        i-=1         
print(sum)