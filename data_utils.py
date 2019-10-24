import numpy
import pandas


def generate_a(width=800, height=10000):
    valid_height = height - height % width
    invalid_height = height - valid_height
    a = __generate_valid(width, valid_height)
    if valid_height:
        a += __generate_valid(width, invalid_height)
    else:
        a += __generate_invalid(width, height)
        print(height, invalid_height)
    a = numpy.array(a)
    numpy.random.shuffle(a)
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


def __check_a(a):
    height, width = len(a), len(a[0])
    for row in a:
        if not (-1 in row and 1 in row):
            return False

    for j in range(width):
        column = [a[i][j] for i in range(height)]
        if not (-1 in column and 1 in column):
            return False
    return True


def write_data(data, filename, transpose=True):
    df = pandas.DataFrame(data)
    if transpose:
        df = df.transpose()
    df.to_csv(filename)


def read_data(filename, transpose=True):
    df = pandas.read_csv(filename).transpose()
    array = df.to_numpy()[1:]
    return array.transpose() if transpose else array


def generate_lambdas(size, amount):
    return [
        [1] * size
        for _ in range(amount)
    ]
