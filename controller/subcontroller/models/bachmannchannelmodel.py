from __future__ import annotations

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QColor


class BachmannCMSTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self._data=data
        self.load_data(data)

    def load_data(self, data):
        
        self.channeldbid = data[0]
        self.wtgid = data[1]
        self.cmsid = data[2]
        self.channel_number = data[3]
        self.identifier = data[4]
        self.label = data[5]
        self.speedlabel = data[6]
        self.powerlabel = data[7]
        self.column_count = 8
        self.row_count = len(self.channeldbid)

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Channel DB ID", "WTG ID", "CMS ID", "Channel Number", "Identifier", "Label", "Speed Label", "Power Label")[section]
        else:
            return f"{section}"
    
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                value = self._data[index.column()][index.row()]
                return str(value)
    
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            if index.column() in ( 4, 5, 6, 7):
                self._data[index.column()][index.row()] = value
                print(self._data)
                return True
            else:
                return False
        return False
    
    def flags(self, index):
        if index.column() in ( 4, 5, 6, 7):
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
        else:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled