import csv
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from time import perf_counter
from math import pi
from matplotlib.animation import FuncAnimation, PillowWriter


def task1():
    list1 = [randint(-1000, 1000) for _ in range(10 ** 6)]
    list2 = [randint(-1000, 1000) for _ in range(10 ** 6)]
    np_mass1 = np.array(list1)
    np_mass2 = np.array(list2)

    t_start1 = perf_counter()
    for i in range(10 ** 6):
        list1[i] *= list2[i]
    t_all1 = perf_counter() - t_start1

    t_start2 = perf_counter()
    np.multiply(np_mass1, np_mass2)
    t_all2 = perf_counter() - t_start2

    print(f'Время перемножения стандартных списков - {t_all1}')
    print(f'Время перемножения numpy массивов - {t_all2}')
    print(f'Разница во времени - {t_all1 - t_all2}')


def task2():
    with open('data2.csv', 'r') as table:
        table = list(csv.reader(table, delimiter=','))
        column = np.array([])
        table.pop(0)
        for row in table:
            column = np.append(column, float(row[3]))

    fig = plt.figure(figsize=(14, 6))
    ax0 = fig.add_subplot(1, 2, 1)
    ax0.set_title('Гистограмма')
    ax0.set_xlabel('Интервалы')
    ax0.set_ylabel('Количество значений, которые попали в заданные интервалы')
    ax0.hist(column, 20)
    ax0.grid()

    ax1 = fig.add_subplot(1, 2, 2)
    ax1.set_title('Нормализованная гистограмма')
    ax1.hist(column, 20, density=True)
    ax1.set_xlabel('Интервалы')
    ax1.set_ylabel('Вероятность')
    ax1.grid()

    plt.show()

    print(f'Cреднеквадратичное отклонение - {np.std(column)}')


def task3():
    x = np.linspace(-3 * pi, 3 * pi, 100)
    y = np.cos(x)
    z = x / np.sin(x)

    fig = plt.figure(figsize=(7, 4))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('Ox')
    ax.set_ylabel('Oy')
    ax.set_zlabel('Oz')
    ax.set_title('Трёхмерный график')
    ax.plot(x, y, z)

    plt.show()


def animation():
    fig = plt.figure()
    ax = fig.add_subplot()
    x, ysin = [], []
    ln1, = plt.plot([], [], 'k')

    def init():
        ax.set_xlim(0, 10)
        ax.set_ylim(-1.5, 1.5)

    def update(i):
        x.append(i)
        ysin.append(np.sin(i))
        ln1.set_data(x, ysin)

    ani = FuncAnimation(fig, update, np.linspace(0, 10), init_func=init)
    writer = PillowWriter(fps=25)
    ani.save("animation.gif", writer=writer)


if __name__ == "__main__":
    task1()
    task2()
    task3()
    animation()
