'''
Created on Apr 21, 2023

@author: bucpa
'''
import sys
from view.mainform import Ui_Widget
from view.gem_dialog import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from GameActions import GameActions
from view.model.PlayerList import PlayerList
from view.GemTableView import GemTableView
from TokenStore import TokenStore
from view.model.TokenStoreModel import TokenStoreModel
from Color import Color

class MainWindow(QtWidgets.QMainWindow, Ui_Widget):
    '''
    classdocs
    '''
    gameActions: GameActions

    def __init__(self, *args, obj=None, **kwargs):
        '''
        Constructor
        '''
        QtWidgets.QMainWindow.__init__(self)
        Ui_Widget.__init__(self)
        
        self.setupUi(self)
        self.players = []
        self.gameActions = GameActions(["p1", "p2", "p3", "p4"])
        self.players = self.gameActions.getPlayersList()
        self.playersModel = PlayerList(players=self.players)
        self.playersListView.setModel(self.playersModel)
       
        self.gameActionsDropdown.currentIndexChanged.connect(self.onActionSelected)
        self.onActionSelected(self.gameActionsDropdown.currentIndex())
    
    def onActionSelected(self, index):
        print(f"dd changed to {index}")
        match index:
            case 0:
                pass
            case 1:
                self.openGemDialog()
            case _:
                pass
       
        
    def openGemDialog(self):
        gems = self.gameActions.game.availableGems
        self.tokenModel = TokenStoreModel(gems, [Color.WHITE, Color.BLUE, Color.GREEN, Color.RED, Color.BLACK])
        dlg = GemDialog(self)
        dlg.exec()
 
class GemDialog(QDialog):   
        
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        self.ui.gemWithdrawTable = GemTableView(self)
        self.ui.gemWithdrawTable.setModel(parent.tokenModel)
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
    
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()