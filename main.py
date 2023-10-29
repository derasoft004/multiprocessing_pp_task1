# Используя пакет multiprocessing, распараллельте на процессы процедуру
# вычисления суммы элементов матрицы (параллелить вычисление суммы по столбцам или
# строкам, итоговую сумму вычислять в общем потоке). Написанное приложение должно
# быть консольным. Аргументы командной строки – размер матрицы и ее значнеия.

from multiprocessing import Process, Pool
import numpy as np
from random import randint

def enter_the_matrix(n, m):
    content = []
    for i in range(n):
        new_column = []
        content.append(new_column)
        for j in range(m):
            new_column.append(int(input(f'input element[{i + 1}][{j + 1}]: '))) # заполнение вручную
            # new_column.append(randint(0, 10)) # рандомное заполнение
        content[i] = new_column
    return np.array([content[i] for i in range(n)])


def sum_elements(matrix):
    return sum(x for x in matrix)

def run():
    n = int(input('enter the matrix n: '))
    m = int(input('enter the matrix m: '))
    matrix = enter_the_matrix(n, m)
    print(matrix)

    pool = Pool()
    results = pool.map(sum_elements, [matrix[i:i + m] for i in range(0, len(matrix), m)])
    pool.close()
    pool.join()
    print(sum(results[0]))


if __name__ == '__main__':
    run()

























