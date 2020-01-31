# LEsson4
# You're using code navigation to jump to definitions or references.
# Learn more or give us feedback

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

def test():
    # assert len(choice_name(listnames, length ))==100
    assert len(new_list) == 100

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

'''
1. Выберете дз, к функциям которого будете писать тесты (например, вебинар 5);
2. Создайте дополнительную ветку в репозитории GitHub с тестами;
3. Напишите не менее 5ти тестов к функциям выбранного урока;
4. В качестве ответа на дз пришлите ссылку на ветку с тестами или ссылку на PullRequest ветки с тестами с веткой master.
'''

#      for name in listnames:
#          letter = name [0:1]
# assert letter.isupper()

# def func (listnames):
#     for name in listnames:
#         letter = name[1:2]
#         if letter.islower():
#             print (letter)
#         else:
#             print (letter)
# func(listnames)


fib_num = lambda n: fib_num(n-1)+ fib_num(n-2) if n > 2 else 1



def test_1_fib_num():

    assert fib_num(6) == 8



def test_2_fib_num():

    assert fib_num(5) == 8



# f_{2n} = (f_{n+1})^2 - (f_{n-1})^2

def test_3_fib_num():

    n = 10

    assert fib_num(2*n) == fib_num(n+1)**2 - fib_num(n-1)**2

