# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в N-мерном пространстве.
# Сначала задается N с клавиатуры, потом задаются координаты точек.

from math import sqrt, pow


def get_number_of_dimensions():
    return int(input('Введите размерность N: '))


def get_coordinates(number_of_dimensions):
    coordinates1 = []
    coordinates2 = []

    print('Введите координаты первой точки')
    for i in range(number_of_dimensions):
        coordinates1.append(float(input(f'\t{i + 1}: ')))

    print('Введите координаты второй точки')
    for i in range(number_of_dimensions):
        coordinates2.append(float(input(f'\t{i + 1}: ')))

    return coordinates1, coordinates2


def get_distance(both_point_coords):
    distance_to_second_power = 0
    for i in range(len(both_point_coords[0])):
        distance_to_second_power += pow((both_point_coords[0][i] - both_point_coords[1][i]), 2)
    return round(sqrt(distance_to_second_power), 2)


print(get_distance(get_coordinates(get_number_of_dimensions())))
