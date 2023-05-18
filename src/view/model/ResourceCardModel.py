'''
Created on Apr 25, 2023

@author: bucpa
'''
from TokenStore import TokenStore
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from typing import OrderedDict
from PyQt5.Qt import QModelIndex
from ResourceCard import ResourceCard

class ResourceCardModel( QtCore.QAbstractTableModel):
    '''
    classdocs
    '''
    _headers = ["Level", "Color", "Points", "Cost"]

    def __init__(self, cards: list[ ResourceCard]):
        '''
        Constructor
        '''
        super(ResourceCardModel, self).__init__()
        self._data = cards
    
    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            # Look up the key by header index.
            column = index.column()
            row = index.row()
            item:ResourceCard = self._data[row]
            
            match column: 
                case 0:
                    return str(item.level)
                case 1:
                    return str(item.suit)
                case 2:
                    str(item.points)
                case 3:
                    return str(item.cost)
                case _:
                    return ""

    
    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The length of our headers.
        return len(self._headers)
            
            
    # def flags(self, index:QModelIndex):
    #     if(self._flags[int(index.row())] == 1):
    #         return Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled
    #     return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        