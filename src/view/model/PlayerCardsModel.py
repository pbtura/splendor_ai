'''
Created on Apr 21, 2023

@author: bucpa
'''
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from Player import Player
from ResourceCard import ResourceCard


class PlayerCardsModel(QtCore.QAbstractListModel):
    '''
    classdocs
    '''

    def __init__(self, *args, cards=None, **kwargs):
        super(PlayerCardsModel, self).__init__(*args, **kwargs)
        self.cards = cards or []
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the data structure.
            card:ResourceCard = self.cards[index.row()]
            return player.name

    def rowCount(self, index):
        return len(self.players)   
        