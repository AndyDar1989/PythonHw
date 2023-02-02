# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3


def find_numbers(sum_num, mult_num):
    num_1 = 0
    flag = True
    while flag:
        if sum_num*num_1-num_1**2 == mult_num and num_1 <= 1000:
            flag = False
            num_2 = sum_num-num_1
            return num_1, num_2
        elif num_1 > 1000:
            flag = False
            return -1
        else:
            num_1 += 1


print(find_numbers(4, 4))
