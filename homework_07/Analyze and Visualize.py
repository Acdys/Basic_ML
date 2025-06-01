# Импортируйте NumPy

import numpy as np

# Создайте одномерный массив размера 10, заполненный нулями и пятым элемент равным 1. Трансформируйте в двумерный массив

arr = np.zeros(10)
arr[4] = 1
arr_2d = arr.reshape(2, 5)
arr_2d

# Создайте одномерный массив со значениями от 10 до 49 и разверните его (первый элемент становится последним). Найдите в нем все четные элементы

arr = np.arange(10, 50)
arr_reversed = arr[::-1]
even_elements = arr_reversed[arr_reversed % 2 == 0]
even_elements

# Создайте двумерный массив 3x3 со значениями от 0 до 8

arr_2d = np.arange(9).reshape(3, 3)
arr_2d

# Создайте массив 4x3x2 со случайными значениями. Найти его минимум и максимум

random_arr = np.random.rand(4, 3, 2)
min_val = np.min(random_arr)
max_val = np.max(random_arr)
min_val, max_val

# Создайте два двумерных массива размерами 6x4 и 4x3 и произведите их матричное умножение

arr1 = np.random.rand(6, 4)
arr2 = np.random.rand(4, 3)
result = np.dot(arr1, arr2)
result

# Создайте случайный двумерный массив 7x7, найти у него среднее и стандартное отклонение. Нормализуйте этот массив

arr = np.random.rand(7, 7)
mean = np.mean(arr)
std = np.std(arr)
normalized_arr = (arr - mean) / std
mean, std, normalized_arr

# Импортируйте: pandas, matplotlib, seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузите датасет Tips из набора датасетов seaborn

tips = sns.load_dataset('tips')

# Посмотрите на первые 5 строчек

tips.head()

# Узнайте сколько всего строчек и колонок в данных

tips.shape

# Проверьте есть ли пропуски в данных

tips.isnull().sum()

# Посмотрите на распределение числовых признаков

tips.describe()

# Найдите максимальное значение 'total_bill'

tips['total_bill'].max()

# Найдите количество курящих людей

tips[tips['smoker'] == 'Yes'].shape[0]

# Узнайте какой средний 'total_bill' в зависимости от 'day'

tips.groupby('day')['total_bill'].mean()

# Отберите строчки с 'total_bill' больше медианы и узнайте какой средний 'tip' в зависимости от 'sex'

median_total_bill = tips['total_bill'].median()
filtered_tips = tips[tips['total_bill'] > median_total_bill]
filtered_tips.groupby('sex')['tip'].mean()

# Преобразуйте признак 'smoker' в бинарный (0-No, 1-Yes)

tips['smoker_binary'] = tips['smoker'].map({'No': 0, 'Yes': 1})
tips[['smoker', 'smoker_binary']].head()

# Постройте гистограмму распределения признака 'total_bill'

plt.hist(tips['total_bill'], bins=20)
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title('Distribution of Total Bill')
plt.show()

# Постройте scatterplot, представляющий взаимосвязь между признаками 'total_bill' и 'tip'

sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Total Bill vs Tip')
plt.show()

# Постройте pairplot

sns.pairplot(tips)
plt.show()

# Постройте график взаимосвязи между признаками 'total_bill' и 'day'

sns.boxplot(x='day', y='total_bill', data=tips)
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.title('Total Bill by Day')
plt.show()

# Постройте две гистограммы распределения признака 'tip' в зависимости от категорий 'time'

plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x='tip', hue='time', multiple='dodge', bins=20)
plt.xlabel('Tip')
plt.ylabel('Frequency')
plt.title('Distribution of Tip by Time')
plt.show()

# Постройте два графика scatterplot, представляющих взаимосвязь между признаками 'total_bill'

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.scatterplot(x='total_bill', y='tip', hue='smoker', data=tips[tips['sex'] == 'Male'])
plt.title('Male')
plt.subplot(1, 2, 2)
sns.scatterplot(x='total_bill', y='tip', hue='smoker', data=tips[tips['sex'] == 'Female'])
plt.title('Female')
plt.show()

# Выводы по анализу датасета и построенным графикам:

#1. Распределение `total_bill` показывает, что большинство счетов находится в диапазоне от 10 до 20 долларов
#2. Существует положительная корреляция между `total_bill` и `tip` - чем больше счет, тем больше чаевые
#3. Средний `total_bill` варьируется по дням недели, с наибольшими значениями в выходные (Sat/Sun)
#4. Курящие люди составляют меньшинство в датасете (~38%)
#5. Средние чаевые для мужчин и женщин при `total_bill` > медианы примерно одинаковы
