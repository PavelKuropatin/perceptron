import os
from collections import defaultdict

PWD = os.getcwd()
__ASSETS = os.path.join(PWD, "assets")
__CSV = os.path.join(__ASSETS, "csv")
IMAGE = os.path.join(__ASSETS, "image")
A_IMAGE = os.path.join(IMAGE, "a_image.png")

LAMBDAS_0_FILE = os.path.join(__CSV, "lambdas0.csv")
LAMBDAS_FILE = os.path.join(__CSV, "lambdas.csv")
LAMBDAS_VALUE = [-1, 0, 1]

A_FILE = os.path.join(__CSV, "a.csv")
Y_FILE = os.path.join(__CSV, "y.csv")
CLASSES_FILE = os.path.join(__CSV, "classes.csv")

IMAGE_SIZE = 100
A_SIZE = 800
LAMBDAS_COUNT = 5

VALUE_COLORS_MAPPING = defaultdict(lambda: [255, 255, 255], {
    1: [0, 255, 0],
    0: [0, 0, 0],
    -1: [255, 0, 0],
})
