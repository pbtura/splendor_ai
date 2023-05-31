'''
Created on Apr 25, 2023

@author: bucpa
'''
from typing import Any

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QModelIndex

from NobleCard import NobleCard


class NobleCardModel(QtCore.QAbstractTableModel):
    '''
    classdocs
    '''
    _headers = ["Points", "Cost"]

    def __init__(self, cards: list[NobleCard]):
        '''
        Constructor
        '''
        super(NobleCardModel, self).__init__()
        self._data = cards
    
    def data(self, index: QModelIndex, role: int = ...) -> Any:
        column = index.column()
        row = index.row()
        item: NobleCard = self._data[row]
        
        if role == Qt.DisplayRole or role == Qt.EditRole:            
            
            match column: 
                case 0:
                    return str(item.points)
                case 1:
                    return str(item.cost)
                case _:
                    return ""

    def getRow(self, index, role):
        row = index.row()
        item: NobleCard = self._data[row]
        
        if role == Qt.DisplayRole or role == Qt.EditRole:                       
            return [str(item.points), str(item.cost)]
                
        elif role == Qt.UserRole:
            return item
    
    def rowCount(self, parent: QModelIndex = ...) -> int:
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, parent: QModelIndex = ...):
        # The length of our headers.
        return len(self._headers)
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section])

            if orientation == Qt.Vertical:
                return ""
        