'''
Created on Apr 21, 2023

@author: bucpa
'''
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from Player import Player

class PlayerList(QtCore.QAbstractListModel):
    '''
    classdocs
    '''

    def __init__(self, *args, players=None, **kwargs):
        super(PlayerList, self).__init__(*args, **kwargs)
        self.players = players or []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            player:Player = self.players[index.row()]
            return player.name

    def rowCount(self, index):
        return len(self.players)   
        