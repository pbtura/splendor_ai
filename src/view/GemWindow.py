'''
Created on Apr 25, 2023

@author: bucpa
'''
import sys
import traceback
from view.mainform import Ui_Widget
from view.gem_dialog import Ui_Dialog
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog
from GameActions import GameActions
from view.model.PlayerList import PlayerList
from TokenStore import TokenStore
from view.model.TokenStoreModel import TokenStoreModel
from Color import Color

class GemWindow(QtWidgets.QMainWindow, Ui_Dialog):
    '''
    classdocs
    '''


    def __init__(self, *args, obj=None, **kwargs):
        '''
        Constructor
        '''
        QtWidgets.QMainWindow.__init__(self)
        Ui_Dialog.__init__(self)
        
        self.setupUi(self)
        self.players = []
        self.gameActions = GameActions(["p1", "p2", "p3", "p4"])
        
        gems = self.gameActions.game.availableGems
        tokenModel = TokenStoreModel(gems, [Color.WHITE, Color.BLUE, Color.GREEN, Color.RED, Color.BLACK], 0)
        self.gemsAvailableTable.setModel(tokenModel)
        
        currentPlayer = self.gameActions.currentPlayer
        tokenDataModel = TokenStoreModel(currentPlayer.gems, [Color.WHITE, Color.BLUE, Color.GREEN, Color.RED, Color.BLACK], 1)
        self.gemWithdrawTable.setModel(tokenDataModel)
        
    def accept(self):
        pass
    
    def reject(self):
        pass

if QtCore.QT_VERSION >= 0x50501:
    def excepthook(type_, value, traceback_):
        traceback.print_exception(type_, value, traceback_)
        QtCore.qFatal('')
sys.excepthook = excepthook

app = QtWidgets.QApplication(sys.argv)

window = GemWindow()
window.show()
app.exec()      