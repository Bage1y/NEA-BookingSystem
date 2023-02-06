#imports
import json
from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel,Qt

# re-json-dump
def jsonrefill(parameter):
    file = open("rooms.json", 'w')
    file.close()
    file = open("rooms.json", "w")
    file.write(json.dumps(parameter))
    file.close()
def recordjsonrefill(parameter):
    file = open("record.json", 'w')
    file.close()
    file = open("record.json", "w")
    file.write(json.dumps(parameter))
    file.close()

# linear search
def linearsearch(editlist, room, searchitem):
    finallist = []
    for i in range(len(editlist) - 1):
        if editlist[i]['Status'] == 'Available':
            if editlist[i][searchitem] == room:
                finallist.append(editlist[i])
    return finallist

#TABLE
class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self,data):
        QAbstractTableModel.__init__(self)
        self._data = data
    def rowCount(self,parent=None):
        return self._data.shape[0]
    def columnCount(self,parent=None):
        return self._data.shape[1]
    def data(self,index,role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(),index.column()])
    def headerData(self,col,orientation,role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None