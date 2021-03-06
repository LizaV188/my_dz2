#Задачи на циклы и оператор условия------
#----------------------------------------
'''
(!!!Подсказка на следующие 5 задач - превратите число в строку, а потом работайте с строкой)
Задача 6
Найти сумму цифр числа.
    Пример:
    254314
    Сумма цифр числа - 19(2+5+4+3+1+4)
'''
print('Задача 6')
nnn=900
list_str = list(str(nnn))               # список строковых символов
list_nnn = [int(i) for i in list_str]   # список цифр в числе
sum_nnn = 0
for j in list_nnn:
    sum_nnn+=j

print('Сумма цифр числа {} = {} ({})'.format(nnn, sum_nnn, "+".join(list_str)))



'''
Задача 7
Найти произведение цифр числа.
    Пример:
    254314
    Произведение цифр числа - 480(2*5*4*3*1*4)
'''
print('\nЗадача 7')         # используем код и исх.данные предыдущей задачи
pr_nnn = 1
for j in list_nnn:
    pr_nnn*=j

print('Произведение цифр числа {} = {} ({})'.format(nnn, pr_nnn, "*".join(list_str)))

'''
Задача 8
Пользователь должен ввести число. Ваш код должен дать ответ на вопрос: есть ли среди цифр числа 5?
Если есть, код должен вывексти "Цифра 5 есть в числе", в противном случае вывести: "Цифры 5 нет в числе".
'''

print('\nЗадача 8')
while True:
    n = input('Введите число: ')
    if n.isnumeric():
        if '5' in n:
            print('Цифра 5 есть в числе')
        else:
            print('Цифры 5 нет в числе')
        break
    else:
        print('это не целое положительное число, еще попытка...')



'''
Задача 9
Найти максимальную цифру в числе
Пример:
    354359688
    'Цифра - 9 максимальная в числе 354359688'
'''

print('\nЗадача 9')
nnn=67481
n_list=list(str(nnn))
print('Цифра ', max(n_list), 'максимальная в числе', nnn)    # для строк также max сработал


'''
Задача 10
Найти количество цифр 5 в числе
    Пример:
        543231235643
        'В числе 2 5-ки.'
'''

print('\nЗадача 10')
nnn=543231235643
sum_5=0
n_list=list(str(nnn))
for i in n_list:
    if i == '5':
        sum_5+=1

print('В числе', nnn, sum_5, 'цифры 5')