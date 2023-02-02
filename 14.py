# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.


def get_number():
    return int(input('Input N: '))


def get_sequence(number):
    power = 0
    while 2 ** power <= number:
        print(2 ** power)
        power += 1


get_sequence(get_number())
