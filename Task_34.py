# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод: Парам пам-пам  

def counting_glasn (elem):
    count = 0
    glasn ='аоеизуяьюё'
    for i in range (len(elem)):
        if elem[i] in glasn:
            count += 1
    return count

text = list(map(str, input ( 'Введите текст: ') .split ()))
number_v = list(map(counting_glasn, text))
rythm = list(filter (lambda x: x == number_v[0], number_v) )
if len (number_v) == len (rythm) :
    print ('Парам пам-пам')
else:
    print ('Пам парам')
