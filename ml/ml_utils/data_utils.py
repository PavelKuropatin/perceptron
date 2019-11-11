import csv
import random

import numpy as _
import pandas

from utils.constants import LAMBDAS_VALUE


def generate_a(width=800, height=10000):
    valid_height = height - height % width
    invalid_height = height - valid_height
    a = __generate_valid(width, valid_height)
    if valid_height:
        a += __generate_valid(width, invalid_height)
    else:
        a += __generate_invalid(width, height)
        print(height, invalid_height)
    a = _.array(a)
    _.random.shuffle(a)
    return a


def __generate_valid(width, height):
    a = []
    m = 1
    for i in range(height):
        j = i % width

        x = [0] * width
        x[j] = m * (-1 if i % 2 else 1)
        x[-j - 1] = m * (-1 if i % 2 == 0 else 1)
        if width // 2 == (j + 1):
            m *= -1
        a.append(x)
    return a


def __generate_invalid(width, height):
    a = []

    if height % 2:
        a.append([-1] + [0] * (width - 2) + [1])
        height -= 1

    multiple = 1

    for i in range(height):
        if not i % width:
            multiple *= -1
        x = [0] * width
        j = i % width
        print(j, multiple * (-1 if i % 2 else 1), multiple * (-1 if i % 2 == 0 else 1))
        x[-(j + 1)] = multiple * (-1 if i % 2 == 0 else 1)
        a.append(x)
    return a


def check_a(a):
    height, width = len(a), len(a[0])
    for row in a:
        if len([i for i in row if i == 1]) != 1:
            print("one count in row")
            return False
    for row in a:
        if not (-1 in row and 1 in row):
            return False

    for j in range(width):
        column = [a[i][j] for i in range(height)]
        if not (-1 in column and 1 in column):
            return False
    return True


def write_matrix_data(data, filename):
    pandas.DataFrame(data).to_csv(filename)


def read_matrix_data(filename):
    df = pandas.read_csv(filename)
    return _.delete(df.to_numpy(), 0, 1)


def generate_lambdas(size, amount):
    return [
        [random.choice(LAMBDAS_VALUE) for i in range(size)]
        for _ in range(amount)
    ]


def read_csv(filename):
    with open(filename, newline='') as f:
        return [_ for _ in csv.reader(f, delimiter=',')]


if __name__ == '__main__':
    a = read_matrix_data("C:/Users/pavel/PycharmProjects/perceptron/assets/csv/a.csv")
    a = a.transpose()
    print(check_a(a))
