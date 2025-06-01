# Задача №1

def divide_bread(N, K):
    x = K // N  # Количество кусков хлеба, которое достанется каждому хоббиту
    y = K % N   # Количество кусков хлеба, которое останется в корзинке
    return x, y

# Например:

N = 3  # Количество хоббитов
K = 14  # Количество кусков хлеба
x, y = divide_bread(N, K)
print(f"Каждому хоббиту достанется {x} куска хлеба, в корзинке останется {y} куска.")

# Задача №2

def is_leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return "YOU SHALL PASS"
    else:
        return "YOU SHALL NOT PASS"

# Например:

print(is_leap_year(2000))  # YOU SHALL PASS (кратен 400)
print(is_leap_year(2020))  # YOU SHALL PASS (кратен 4, но не 100)
print(is_leap_year(1900))  # YOU SHALL NOT PASS (кратен 100, но не 400)
print(is_leap_year(2021))  # YOU SHALL NOT PASS (не кратен 4)

# Задача №3

import math


def calculate_amulet_area(a, b, c):
    # Проверка на положительность сторон
    if a <= 0 or b <= 0 or c <= 0:
        return "Стороны должны быть положительными"

    # Проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Такого треугольника не существует"

    # Вычисляем полупериметр
    p = (a + b + c) / 2

    # Вычисляем площадь по формуле Герона (исправлены скобки)
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return area


# Например:

print(calculate_amulet_area(3, 4, 5))  # 6.0
print(calculate_amulet_area(1, 1, 3))  # "Такого треугольника не существует"
print(calculate_amulet_area(-1, 2, 2))  # "Стороны должны быть положительными"

# Задача №4

def euclidean_distance(a, b):
    """
    Вычисляет евклидово расстояние между точками a и b.
    Точки заданы как списки/кортежи координат одинаковой длины
    """
    sum_sq = 0.0
    for ai, bi in zip(a, b):
        sum_sq += (ai - bi)**2
    return sum_sq**0.5

def manhattan_distance(a, b):
    """
    Вычисляет расстояние Манхэттена между точками a и b.
    Точки заданы как списки/кортежи координат одинаковой длины
    """
    distance = 0.0
    for ai, bi in zip(a, b):
        distance += abs(ai - bi)
    return distance


def cosine_distance(a, b):
    """
    Вычисляет косинусное расстояние между векторами a и b.
    Точки заданы как списки/кортежи координат одинаковой длины.
    Возвращает 1 - косинус угла между векторами (нормализованное расстояние)
    """
    dot_product = 0.0
    norm_a = 0.0
    norm_b = 0.0

    for ai, bi in zip(a, b):
        dot_product += ai * bi
        norm_a += ai ** 2
        norm_b += bi ** 2

    norm_a = norm_a ** 0.5
    norm_b = norm_b ** 0.5

    if norm_a == 0 or norm_b == 0:
        return 1.0  # Если один из векторов нулевой

    cosine_similarity = dot_product / (norm_a * norm_b)
    return 1.0 - cosine_similarity

# Например:

point_a = (1, 2, 3)
point_b = (4, 5, 6)

print("Евклидово расстояние:", euclidean_distance(point_a, point_b))
print("Расстояние Манхэттена:", manhattan_distance(point_a, point_b))
print("Косинусное расстояние:", cosine_distance(point_a, point_b))

# Задача №5

import numpy as np

# Случайный массив длиной 100
arr = np.random.rand(100)

# Нормализуем массив
normalized_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("Исходный массив:")
print(arr)
print("Нормализованный массив:")
print(normalized_arr)
print("Максимальное значение:", np.max(normalized_arr))
print("Минимальное значение:", np.min(normalized_arr))

# Задача №6

import numpy as np

# Создаем массив 5x6 со случайными целыми числами от 0 до 50
my_array = np.random.randint(0, 51, size=(5, 6))

# Находим индекс колонки с максимальным элементом
max_col_index = np.argmax(np.max(my_array, axis=0))

# Выбираем всю колонку по найденному индексу
selected_column = my_array[:, max_col_index]

print('Shape: ', my_array.shape)
print('Array')
print(my_array)
print(selected_column)

# Задача №7

import numpy as np

def get_unique_rows(X):
    tuples = [tuple(row) for row in X]
    _, unique_indices = np.unique(tuples, axis=0, return_index=True)
    X_unique = X[sorted(unique_indices)]
    return X_unique

# Например:
X = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3],  # Дубликат
    [7, 8, 9],
    [4, 5, 6]   # Дубликат
])

print("Исходная матрица:")
print(X)

unique_X = get_unique_rows(X)
print("Уникальные строки:")
print(unique_X)
