def same_by(charact, objects):
    if objects==0:
        return True
    else:
        result = [charact(obj) for obj in objects]
        for i in result:
            if i!=0:
                return 'different'
        return 'same'
    
    
my_obj=[0,10,2,6]
print(list(map(lambda x: x%2, my_obj)))
    
print(same_by(lambda x: x%2, my_obj))    