from typing import Dict, List

import numpy as np
from PIL import Image


def by_avg_sum(rgb):
    if isinstance(rgb, tuple):
        rgb = sum(rgb) // 3
    return int(rgb < 128)


def to_bit_pixels(img_path, convert_func=by_avg_sum, mode="r"):
    image = Image.open(img_path, mode)
    rgb_pixels = image.load()

    return np.array([
        [
            convert_func(rgb_pixels[i, j])
            for i in range(image.width)
        ]
        for j in range(image.height)
    ])


def save_as_image(values: np.ndarray, path: str, mapping: Dict[int, List[int]], multiplier: int):
    w, h = values.shape
    arr = np.zeros([w, h, 3], dtype=np.uint8)
    for ij, value in np.ndenumerate(values):
        arr[ij[0]][ij[1]] = mapping[value]
    arr = np.asarray(arr, dtype=np.uint8)
    arr = np.repeat(arr, multiplier, axis=0)
    arr = np.repeat(arr, multiplier, axis=1)
    image = Image.fromarray(arr)
    image.save(path)
