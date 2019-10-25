import os

PWD = os.getcwd()
__ASSETS = os.path.join(PWD, "assets")
__CSV = os.path.join(__ASSETS, "csv")
IMAGE = os.path.join(__ASSETS, "image")

LAMBDAS_0_FILE = os.path.join(__CSV, "lambdas0.csv")
LAMBDAS_FILE = os.path.join(__CSV, "lambdas.csv")
A_FILE = os.path.join(__CSV, "a.csv")
Y_FILE = os.path.join(__CSV, "y.csv")

IMAGE_SIZE = 100
A_SIZE = 800
LAMBDAS_COUNT = 5