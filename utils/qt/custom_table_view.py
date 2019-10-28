from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex


class CustomTableView(QAbstractTableModel):

    def __init__(self, data):
        self.__bitmap = data
        super(CustomTableView, self).__init__()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return str(self.__bitmap[index.row()][index.column()])

    def rowCount(self, parent: QModelIndex = None) -> int:
        return len(self.__bitmap)

    def columnCount(self, parent: QModelIndex = None) -> int:
        return len(self.__bitmap[0]) if len(self.__bitmap) else 0
