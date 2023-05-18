'''
Created on Apr 25, 2023

@author: bucpa
'''
from TokenStore import TokenStore
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from typing import OrderedDict
from PyQt5.Qt import QModelIndex

class TokenStoreModel( QtCore.QAbstractTableModel):
    '''
    classdocs
    '''


    def __init__(self, gems: list[ str, TokenStore], headers, editable: list):
        '''
        Constructor
        '''
        super(TokenStoreModel, self).__init__()
        self._data = gems
        self._headers = headers
        self._flags = editable
    
    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            # Look up the key by header index.
            column = index.column()
            column_key = self._headers[column]
            row = index.row()
            store = self._data[row][1]
            return int(store.tokens[column_key])
    
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            column = index.column()
            column_key = self._headers[column]
            self._data[index.row()][1].tokens[column_key] = value
            return True
    
    def refreshData(self, gems):
        self._data = gems
        topLeft = self.index(0,0)
        bottomRight = self.createIndex(len(gems)-1, len(self._headers)-1)
        self.dataChanged.emit(topLeft, bottomRight)
    
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The length of our headers.
        return len(self._headers)
    
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section].name)

            if orientation == Qt.Vertical:
                # keys = list(self._data.keys())
                return str(self._data[section][0])
            
            
    def flags(self, index:QModelIndex):
        if(self._flags[int(index.row())] == 1):
            return Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        