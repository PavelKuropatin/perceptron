import numpy
from PIL import Image


def by_avg_sum(rgb):
    return int(rgb < 128)


def to_bit_pixels(img_path, convert_func=by_avg_sum, mode="r"):
    image = Image.open(img_path, mode)
    rgb_pixels = image.load()

    return numpy.array([
        [
            convert_func(rgb_pixels[i, j])
            for i in range(image.width)
        ]
        for j in range(image.height)
    ])
