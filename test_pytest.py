

import random

def choice_name(names, length):

    return random.choices(names, k=length)



listnames=['Kate', 'John', 'Nataly', 'Liza', 'John', 'Andrew', 'Olga', 'Mariana', 'Abraham', 'Julia', 'Ornella', 'Liza', 'Maria', 'Alex', 'Peter', 'Julia', 'Andrew', 'Kate', 'Samuil', 'Galina']



new_list = choice_name(listnames, length=100)



print(new_list)

def test1():
    assert len(choice_name(listnames, length=100 ))==100
    # assert len(new_list) == 100

def test2():
    for name in listnames:
        letter = name[0:1]
        assert letter.isupper()

def test3():
    for name in listnames:
        letter = name[1:len(name)]
        assert letter.islower()

def test4():
    for name in listnames:
        if name[0:1] == 'A':
        assert True
        else: assert False