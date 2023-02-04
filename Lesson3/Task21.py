# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
# ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

def unic_val(user_dict):
    new_set = set()
    for i in user_dict:
        for val in i.values():
            new_set.add(val.replace(' ',''))# для replace нужны два аргумента что/на что нужно заменить, лучше использовать .strip() 
    return new_set


my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": " S005 "}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
print(unic_val(my_dict)) 
   