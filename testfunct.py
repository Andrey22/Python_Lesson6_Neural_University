
# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.

# Модуль содержит функции:

# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);

import random

def IsPrimeNumber(number):

   divisor = 2

   while number % divisor!= 0:

       divisor += 1

   return divisor == number

# global sequence_num

# диапазон натуральных числе от 1 до 1000

sequence_num =list( range(1, 1001))

# проверка

# print(sequence_num)

# случайное число в диапазоне от 1 до 1000

# global x

x=random.choice(sequence_num)

print("число для анализа:",x)

print(IsPrimeNumber(x))



# 2) выводит список всех делителей числа;

def GetDiv(number):

    """Разложить число на множители"""

    #result = [1]

    listnum = []

    stepnum = 2

    while stepnum*stepnum <= number:

        if number % stepnum == 0:

            number//= stepnum

            listnum.append(stepnum)

        else:

            stepnum += 1

    if number > 1:

        listnum .append(number)

    return listnum

print (GetDiv(x))



# 3) выводит самый большой простой делитель числа.



def PrimeDiv(number):

    numlist = GetDiv(number)

    max = 0

    for index in numlist:

        if index > max:

            max = index

    return (max)

print(PrimeDiv(x))

# LEsson4
You're using code navigation to jump to definitions or references.
Learn more or give us feedback

# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе

# список длины N случайных имен из первого списка (могут повторяться,

# можно взять значения: количество имен 20, N = 100,

# рекомендуется использовать функцию random);

import random

def choice_name(names, length):

    return random.choices(names, k=length)



listnames=['Kate', 'John', 'Nataly', 'Liza', 'John', 'Andrew', 'Olga', 'Mariana', 'Abraham', 'Julia', 'Ornella', 'Liza', 'Maria', 'Alex', 'Peter', 'Julia', 'Andrew', 'Kate', 'Samuil', 'Galina']



new_list = choice_name(listnames, length=100)



print(new_list)



# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

def frequentname(listname):

    dict = {}

    for name in listname:

        dict[name] = dict.get(name,0) + 1

    dict = list(dict.items())

    dict.sort(key=lambda x: x[1], reverse=True)

    # x[1]  означает сортировку по Values, т.е. по количеству повторений имени в словаре (имя, количество повторений)

    # [0][0]  = вывод ключа первого элемента из отсортированного словаре dict,

    # [0][1] = вывод ключа второго элемента из отсортированного словаре dict

    # [1][0] = вывод Value первого элемента из отсортированного словаре dict

    return dict[0][0]



print(frequentname(new_list))



# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.



def rareletter(list2):

    dict2 = {}

    for name in list2:

        for char in name:

            #

            # выявление заглавной буквы в имени

            #

            if char.isupper():

                dict2[char] = dict2.get(char, 0) + 1

            else: continue

    dict2 = list(dict2.items())

    dict2.sort(key=lambda x: x[1])

    return dict2[0][0]

# return dict2[0][0], dict2[1][0], dict2, dict2[0][0].isupper()

print(rareletter(new_list))

# fib_num = lambda n: fib_num(n-1)+ fib_num(n-2) if n > 2 else 1

#

#

# def test_1_fib_num():

#     assert fib_num(6) == 8

#

# def test_2_fib_num():

#     assert fib_num(5) == 8

#

# # f_{2n} = (f_{n+1})^2 - (f_{n-1})^2

# def test_3_fib_num():

#     n = 10

#     assert fib_num(2*n) == fib_num(n+1)**2 - fib_num(n-1)**2