

import random

def choice_name(names, length):

    return random.choices(names, k=length)



listnames=['Kate', 'John', 'Nataly', 'Liza', 'John', 'Andrew', 'Olga', 'Mariana', 'Abraham', 'Julia', 'Ornella', 'Liza', 'Maria', 'Alex', 'Peter', 'Julia', 'Andrew', 'Kate', 'Samuil', 'Galina']



new_list = choice_name(listnames, length=100)



print(new_list)

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

# Проведение тестов в Pytest

def test1():
    assert len(choice_name(listnames, length=100 ))==100
    # assert len(new_list) == 100

def test2():
    assert rareletter(new_list)!= 'X'
    # assert len(new_list) == 100


def test3():
    assert len(frequentname(new_list))> 3

def test4():
    assert rareletter(new_list).isupper()

def test5():
    assert rareletter(new_list).islower()

def test6():
    for name in listnames:

        letter = name[1:len(name)]

        assert letter.islower()

def test7():
    assert rareletter(new_list).isdigit()


# def test2():

#     for name in listnames:

#         letter = name[0:1]

#         assert letter.isupper()

#

# def test3():

#     for name in listnames:

#         letter = name[1:len(name)]

#         assert letter.islower()

#

# def test4():

#     for name in listnames:

#         if name[0:1] == 'A':

#         assert True

#         else: assert False



