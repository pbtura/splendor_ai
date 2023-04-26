'''
Created on Apr 25, 2023

@author: bucpa
'''
from TokenStore import TokenStore
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class TokenStoreModel( QtCore.QAbstractTableModel):
    '''
    classdocs
    '''


    def __init__(self, gems: TokenStore, headers):
        '''
        Constructor
        '''
        super(TokenStoreModel, self).__init__()
        self._data = gems.tokens
        self._headers = headers
    
    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            # Look up the key by header index.
            column = index.column()
            column_key = self._headers[column]
            return int(self._data[column_key])
    
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            column = index.column()
            column_key = self._headers[column]
            self._data[column_key] = value
            return True
    
    def rowCount(self, index):
        # The length of the outer list.
        return 1

    def columnCount(self, index):
        # The length of our headers.
        return len(self._headers)
    
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section].name)

            if orientation == Qt.Vertical:
                return str(section)
            
            
    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled
        