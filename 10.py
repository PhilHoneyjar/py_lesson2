# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.


from random import randint


def get_coin_toss_list():
    list_length = randint(1, 10)
    coin_toss_list = []
    for i in range(list_length):
        coin_toss_list.append(randint(0, 1))
    print(coin_toss_list)
    return coin_toss_list


def count_heads(coin_toss_list):
    heads_counter = 0
    for x in coin_toss_list:
        heads_counter += x
    return heads_counter if heads_counter <= len(coin_toss_list)/2 else len(coin_toss_list) - heads_counter


print(count_heads(get_coin_toss_list()))
