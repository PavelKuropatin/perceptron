import os
import sys

import numpy as _
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from ml.ml_utils.data_utils import read_matrix_data, read_csv, write_matrix_data
from ml.ml_utils.image_utils import to_bit_pixels
from ml.perceptron import Perceptron
from utils.constants import PWD, IMAGE, A_FILE, CLASSES_FILE, LAMBDAS_FILE


class MainWindow(QMainWindow):

    def __init__(self, file):
        # self.image_table: QTableWidget = None
        self.__image_bitmap = None
        self.__perceptron: Perceptron = None
        self.__answers = []
        super().__init__()
        uic.loadUi(file, self)

        self.__init_data()
        self.learn_button.setEnabled(False)
        # self.learn_perceptron()
        # sys.exit(0)
        self.show()

    def __init_data(self):
        a = read_matrix_data(A_FILE)
        # lambdas = read_matrix_data(LAMBDAS_0_FILE)
        lambdas = read_matrix_data(LAMBDAS_FILE)
        self.__perceptron = Perceptron(a, lambdas)
        self.__classes = {int(index): key for key, index in read_csv(CLASSES_FILE)}
        self.__classes_r = {key: int(index) for key, index in read_csv(CLASSES_FILE)}

    def load_image(self):
        image = self.__open_file()
        if not image:
            print("no selected image")
            return

        image_pixmap = QPixmap(os.path.join(PWD, image))
        self.image_label.setPixmap(image_pixmap)
        self.__image_bitmap = to_bit_pixels(image)

    def __open_file(self):
        return QFileDialog.getOpenFileName(self, "Choose image", IMAGE, "*.*")[0]

    def learn_perceptron(self):
        classes = [path for path in os.listdir(IMAGE) if os.path.isdir(os.path.join(IMAGE, path))]
        images_to_load = []
        for _class in classes:
            class_images_dir = os.path.join(IMAGE, _class)
            images_to_load += [
                (os.path.join(class_images_dir, image), self.__classes_r[_class.upper()])
                for image in os.listdir(class_images_dir)
            ]
        _.random.shuffle(images_to_load)
        for image, proper_class in images_to_load:
            print(image, proper_class)
            self.__perceptron.learning(to_bit_pixels(image), proper_class)

        write_matrix_data(self.__perceptron.lambdas, LAMBDAS_FILE)

    def recognize_image(self):
        if self.__image_bitmap is not None:
            out_class = self.__perceptron.recognizing(self.__image_bitmap)
            print(self.__perceptron.sums)
            answer = QMessageBox.question(self, "Result", f"Class : {self.__classes[out_class]}",
                                          QMessageBox.Yes | QMessageBox.No)
            self.__answers.append(1 if answer == QMessageBox.Yes else 0)
            percent = sum(self.__answers) / len(self.__answers) * 100
            self.percent_label.setText(str(int(percent)))
            print(percent)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow("window.ui")
    sys.exit(app.exec_())
