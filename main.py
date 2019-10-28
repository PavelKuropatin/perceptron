import os
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QFileDialog

from ml.ml_utils.data_utils import read_matrix_data, read_csv
from ml.ml_utils.image_utils import to_bit_pixels
from ml.perceptron import Perceptron
from utils.constants import PWD, IMAGE, A_FILE, LAMBDAS_0_FILE, CLASSES_FILE
from utils.qt.bitmap_table_view import BitmapTableView


class MainWindow(QMainWindow):

    def __init__(self, file):
        self.image_table: QTableWidget = None
        self.__image_bitmap = None
        self.__perceptron: Perceptron = None

        super().__init__()
        uic.loadUi(file, self)

        self.__init_data()
        self.__init_ui()
        self.show()

    def __init_data(self):
        a = read_matrix_data(A_FILE)
        lambdas = read_matrix_data(LAMBDAS_0_FILE)
        self.__perceptron = Perceptron(a, lambdas)
        self.__classes = {int(index): key for key, index in read_csv(CLASSES_FILE)}
        self.__classes_r = {key: int(index) for key, index in read_csv(CLASSES_FILE)}

    def __init_ui(self):
        self.a_table.setModel(BitmapTableView(self.__perceptron.a))
        self.__refresh_out()

    def __refresh_out(self):
        self.out_table.setModel(BitmapTableView(self.__perceptron.out_data))
        sums = ", ".join([f"sum{self.__classes[i]}:{value}" for i, value in enumerate(self.__perceptron.sums)])
        self.sum_label.setText(sums)

    def load_image(self):
        image = self.__open_file()
        if not image:
            print("no selected image")
            return

        image_pixmap = QPixmap(os.path.join(PWD, image))
        self.image_label.setPixmap(image_pixmap)

        self.__image_bitmap = to_bit_pixels(image)
        self.image_table.setModel(BitmapTableView(self.__image_bitmap))
        self.__perceptron.learning(self.__image_bitmap, 1)
        self.__refresh_out()

    def __open_file(self):
        return os.path.join(IMAGE, "a/1.png")
        return QFileDialog.getOpenFileName(self, "Choose image", IMAGE, "*.*")[0]

    def learn_perceptron(self):
        self.learn_button.setEnabled(False)
        classes = os.listdir(IMAGE)
        images_to_load = []
        for _class in classes:
            class_images_dir = os.path.join(IMAGE, _class)
            images_to_load += [
                (os.path.join(class_images_dir, image), self.__classes_r[_class.upper()])
                for image in os.listdir(class_images_dir)
            ]
        print(images_to_load)
        self.__refresh_out()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow("window.ui")
    sys.exit(app.exec_())
