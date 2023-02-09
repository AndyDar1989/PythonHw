str_input = 'a a a b c a a d c d d'
str_list_input = str_input.split()
temp={}
output_str =' '
for i in str_list_input:
    if temp.get(i)!=None:
        temp[i] = temp.get(i) +  1
        output_str += f'{i}_{temp[i]} '
      
    else:
        temp[i]=0
        output_str+=f'{i} '
print (output_str)            
        
        