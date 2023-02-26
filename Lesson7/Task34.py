# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам


def find_rhytm(user_poem):
    poem = user_poem.split()
    
    counter = sum(1 for f in poem[0] if f in'аеиоуэюя')
    print(counter)
    for frase in range(1, len(poem)):
        if sum(1 for f in poem[frase] if f in 'аеиоуэюя')!=counter:
            return 'Пам парам'
    return 'Парам пам-пам'


def find_rhytm_2(user_poem):
    poem = user_poem.split()
    counter = poem[0].count('а')
    for frase in range(1, len(poem)):
        if poem[frase].count('а')!=counter:
            return 'Пам парам'
    return 'Парам пам-пам'


vinnies_poem = input('Enter your poem: ')

print(find_rhytm(vinnies_poem))