import os
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QFileDialog

from ml.ml_utils.image_utils import to_bit_pixels
from utils.constants import PWD, IMAGE
from utils.qt.bitmap_table_view import BitmapTableView


class MainWindow(QMainWindow):

    def __init__(self, file):
        self.image_table: QTableWidget = None
        super().__init__()
        uic.loadUi(file, self)

        self.__image_bitmap = None
        self.show()
        self.load_image()

    def load_image(self):
        image = self.__open_file()
        if not image:
            print("no selected image")
            return

        image_pixmap = QPixmap(os.path.join(PWD, image))
        self.image_label.setPixmap(image_pixmap)

        self.__image_bitmap = to_bit_pixels(image)
        self.image_table.setModel(BitmapTableView(self.__image_bitmap))

    def __open_file(self):
        # return os.path.join(PWD, "A1.png")
        return QFileDialog.getOpenFileName(self, "Choose image", IMAGE, "*.*")[0]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow("window.ui")
    sys.exit(app.exec_())
