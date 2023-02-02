# Задача 12: Петя задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

from random import randint


def get_two_numbers():
    return randint(1, 1000), randint(1, 1000)


def give_a_hint(list_of_two_numbers):
     return (f'Подсказка: {list_of_two_numbers[0] + list_of_two_numbers[1]} \
{list_of_two_numbers[0] * list_of_two_numbers[1]}\
     \nЗагаданные числа: {list_of_two_numbers[0]} {list_of_two_numbers[1]}')


print(give_a_hint(get_two_numbers()))
