'''
Created on Apr 25, 2023

@author: bucpa
'''
import sys
from view.mainform import Ui_Widget
from PyQt5.QtCore import QObject
from view.gem_dialog import Ui_Dialog
from view.model.TokenStoreModel import TokenStoreModel
from GameActions import GameActions
from view.GemTableView import GemTableView
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from Color import Color

class GemDialogController(QtWidgets.QMainWindow, QDialog):
    '''
    classdocs
    '''


    # def __init__(self, model: TokenStoreModel):
    #     '''
    #     Constructor
    #     '''
    #     super().__init__()
    #
    #     self._model = model
        
    def __init__(self, parent=None):
        super().__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        # Create an instance of the GUI
        
        
        self.gameActions = GameActions(["p1", "p2", "p3", "p4"])
        
        self.ui = Ui_Dialog()
        self.ui.gemWithdrawTable = GemTableView(self)
        gems = self.gameActions.game.availableGems
        tokenModel = TokenStoreModel(gems, [Color.WHITE, Color.BLUE, Color.GREEN, Color.RED, Color.BLACK])
        self.ui.gemWithdrawTable.setModel(tokenModel)
        self.ui.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = GemDialogController()
window.show()
app.exec()        