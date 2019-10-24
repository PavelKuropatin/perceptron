import os
import sys
from datetime import datetime

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QTableWidget

from constants import PWD
from image_utils import to_bit_pixels


class MainWindow(QMainWindow):

    def __init__(self, file):
        self.image_table: QTableWidget = None
        self.__img_size = 100
        self.__a_size = 800
        super().__init__()
        uic.loadUi(file, self)

        self.__image_bitmap = None
        self.show()
        self.__init_table_headers()
        self.load_image()

    def load_image(self):
        image = self.__open_file()
        if not image:
            print("no selected image")
            return

        image_pixmap = QPixmap(os.path.join(PWD, image))
        self.image_label.setPixmap(image_pixmap)

        self.__image_bitmap = to_bit_pixels(image)
        # self.render_bitmap(self.__image_bitmap)

    @staticmethod
    def __open_file():
        return os.path.join(PWD, "A1.png")
        # return QFileDialog.getOpenFileName(self, "Choose image", PWD, "*.*")[0]

    def render_bitmap(self, bitmap):
        if not bitmap:
            return

        for i in range(self.__img_size):
            for j in range(self.__img_size):
                self.image_table.setItem(i, j, QTableWidgetItem(str(bitmap[i][j])))
            print(datetime.now())

    def __init_table_headers(self):

        self.image_table.setRowCount(0)
        self.image_table.setColumnCount(0)
        self.image_table.setRowCount(self.__img_size)
        self.image_table.setColumnCount(self.__img_size)
        for i in range(self.__img_size):
            for j in range(self.__img_size):
                self.image_table.setRowHeight(i, 15)
            self.image_table.setColumnWidth(i, 5)

        labels = [''] * self.__img_size
        self.image_table.setHorizontalHeaderLabels(labels)
        self.image_table.setVerticalHeaderLabels(labels)
        for i in range(self.__img_size):
            self.image_table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow("window.ui")
    sys.exit(app.exec_())
