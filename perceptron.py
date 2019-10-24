import os

import numpy

from constants import PWD
from data_utils import read_data
from image_utils import to_bit_pixels


def compute(a: numpy.ndarray, lambdas: numpy.ndarray, x: numpy.ndarray, answer=None):
    x = numpy.concatenate(x)
    print(a[0], a[0].size)
    print(a, a.size)
    print(x, x.size)
    print(lambdas, lambdas.size)
    y1 = numpy.multiply(a[0], x)
    print(numpy.sum(y1))


if __name__ == "__main__":
    lambdas_file = "lambdas.csv"
    a_file = "a.csv"
    image = os.path.join(PWD, "a1.png")

    lambdas = read_data(lambdas_file)
    x = to_bit_pixels(image)
    a = read_data(a_file, transpose=True)

    compute(a, lambdas, x)
