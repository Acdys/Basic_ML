{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# I. Numpy"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Импортируйте NumPy"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "import numpy as np"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Создайте одномерный массив размера 10, заполненный нулями и пятым элемент равным 1. Трансформируйте в двумерный массив."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "arr = np.zeros(10)\n",
                "arr[4] = 1\n",
                "arr_2d = arr.reshape(2, 5)\n",
                "arr_2d"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Создайте одномерный массив со значениями от 10 до 49 и разверните его (первый элемент становится последним). Найдите в нем все четные элементы."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "arr = np.arange(10, 50)\n",
                "arr_reversed = arr[::-1]\n",
                "even_elements = arr_reversed[arr_reversed % 2 == 0]\n",
                "even_elements"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Создайте двумерный массив 3x3 со значениями от 0 до 8"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "arr_2d = np.arange(9).reshape(3, 3)\n",
                "arr_2d"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Создайте массив 4x3x2 со случайными значениями. Найти его минимум и максимум."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "random_arr = np.random.rand(4, 3, 2)\n",
                "min_val = np.min(random_arr)\n",
                "max_val = np.max(random_arr)\n",
                "min_val, max_val"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Создайте два двумерных массива размерами 6x4 и 4x3 и произведите их матричное умножение."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "arr1 = np.random.rand(6, 4)\n",
                "arr2 = np.random.rand(4, 3)\n",
                "result = np.dot(arr1, arr2)\n",
                "result"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Создайте случайный двумерный массив 7x7, найти у него среднее и стандартное отклонение. Нормализуйте этот массив."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "arr = np.random.rand(7, 7)\n",
                "mean = np.mean(arr)\n",
                "std = np.std(arr)\n",
                "normalized_arr = (arr - mean) / std\n",
                "mean, std, normalized_arr"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# II. Pandas"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Импортируйте: pandas, matplotlib, seaborn"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Загрузите датасет Tips из набора датасетов seaborn"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "tips = sns.load_dataset('tips')"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Посмотрите на первые 5 строчек"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "tips.head()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Узнайте сколько всего строчек и колонок в данных"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "tips.shape"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Проверьте есть ли пропуски в данных"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "tips.isnull().sum()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Посмотрите на распределение числовых признаков"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "tips.describe()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Найдите максимальное значение 'total_bill'"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "tips['total_bill'].max()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Найдите количество курящих людей"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "tips[tips['smoker'] == 'Yes'].shape[0]"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Узнайте какой средний 'total_bill' в зависимости от 'day'"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "tips.groupby('day')['total_bill'].mean()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Отберите строчки с 'total_bill' больше медианы и узнайте какой средний 'tip' в зависимости от 'sex'"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "median_total_bill = tips['total_bill'].median()\n",
                "filtered_tips = tips[tips['total_bill'] > median_total_bill]\n",
                "filtered_tips.groupby('sex')['tip'].mean()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Преобразуйте признак 'smoker' в бинарный (0-No, 1-Yes)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "tips['smoker_binary'] = tips['smoker'].map({'No': 0, 'Yes': 1})\n",
                "tips[['smoker', 'smoker_binary']].head()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# III. Visualization"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Постройте гистограмму распределения признака 'total_bill'"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.hist(tips['total_bill'], bins=20)\n",
                "plt.xlabel('Total Bill')\n",
                "plt.ylabel('Frequency')\n",
                "plt.title('Distribution of Total Bill')\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Постройте scatterplot, представляющий взаимосвязь между признаками 'total_bill' и 'tip'"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "sns.scatterplot(x='total_bill', y='tip', data=tips)\n",
                "plt.xlabel('Total Bill')\n",
                "plt.ylabel('Tip')\n",
                "plt.title('Total Bill vs Tip')\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Постройте pairplot"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "sns.pairplot(tips)\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Постройте график взаимосвязи между признаками 'total_bill' и 'day'"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "sns.boxplot(x='day', y='total_bill', data=tips)\n",
                "plt.xlabel('Day')\n",
                "plt.ylabel('Total Bill')\n",
                "plt.title('Total Bill by Day')\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Постройте две гистограммы распределения признака 'tip' в зависимости от категорий 'time'"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.figure(figsize=(10, 6))\n",
                "sns.histplot(data=tips, x='tip', hue='time', multiple='dodge', bins=20)\n",
                "plt.xlabel('Tip')\n",
                "plt.ylabel('Frequency')\n",
                "plt.title('Distribution of Tip by Time')\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Постройте два графика scatterplot, представляющих взаимосвязь между признаками 'total_bill' и 'tip' один для Male, другой для Female и раскрасьте точки в зависимости от признака 'smoker'"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "plt.figure(figsize=(12, 6))\n",
                "\n",
                "plt.subplot(1, 2, 1)\n",
                "sns.scatterplot(x='total_bill', y='tip', hue='smoker', data=tips[tips['sex'] == 'Male'])\n",
                "plt.title('Male')\n",
                "\n",
                "plt.subplot(1, 2, 2)\n",
                "sns.scatterplot(x='total_bill', y='tip', hue='smoker', data=tips[tips['sex'] == 'Female'])\n",
                "plt.title('Female')\n",
                "\n",
                "plt.show()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Сделайте выводы по анализу датасета и построенным графикам. По желанию можете продолжить анализ данных и также отразить это в выводах."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Выводы по анализу датасета и построенным графикам:\n",
                "# 1. Распределение 'total_bill' показывает, что большинство счетов находится в диапазоне от 10 до 20 долларов.\n",
                "# 2. Существует положительная корреляция между 'total_bill' и 'tip', что означает, что чем больше счет, тем больше чаевые.\n",
                "# 3. В зависимости от дня недели средний 'total_bill' варьируется, с наибольшими значениями в выходные дни.\n",
                "# 4. Курящие люди составляют меньшинство в датасете.\n",
                "# 5. Средние чаевые для мужчин и женщин с 'total_bill' больше медианы примерно одинаковы."
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.6.6"
        },
        "toc-autonumbering": false
    },
    "nbformat": 4,
    "nbformat_minor": 2
}
