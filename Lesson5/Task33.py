def change_marks(marks_list):
    max_mark = max(marks_list)
    min_mark = min(marks_list)
    marks_list = [i if i!=max_mark else min_mark for i in marks_list]
    return(marks_list)


my_marks = [3,5,4,1,2,5,4,3,5,4,2,3]
print(change_marks(my_marks))