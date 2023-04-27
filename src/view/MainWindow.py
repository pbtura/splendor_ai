'''
Created on Apr 21, 2023

@author: bucpa
'''
import sys
import traceback
from view.mainform import Ui_Widget
from view.gem_dialog import Ui_Dialog
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
from GameActions import GameActions
from view.model.PlayerList import PlayerList
from view.widgets.GemTableView import GemTableView
from TokenStore import TokenStore
from view.model.TokenStoreModel import TokenStoreModel
from Color import Color
from PyQt5.Qt import QModelIndex, pyqtSignal, QObject, QAbstractItemView

class MainWindow(QtWidgets.QMainWindow, Ui_Widget):
    '''
    classdocs
    '''
    gameActions: GameActions
    _headers = [Color.WHITE, Color.BLUE, Color.GREEN, Color.RED, Color.BLACK]
    
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
            case 2:
                pass
            case _:
                pass
       
        
    def openGemDialog(self):
        
        bank = self.gameActions.game.availableGems
        
        currentPlayer = self.gameActions.currentPlayer
        
        
        data:list = [["to withdraw:", TokenStore(0,0,0,0,0,0)], ["gems available", bank], ["Currently held", currentPlayer.gems]]
        
        self.tokenModel = TokenStoreModel(data, self._headers, [1, 0, 0])
        
        dlg = GemDialog(self)
        dlg.save.connect(self.handleGemsUpdated)
        dlg.exec()
 
    def handleGemsUpdated(self, parent):
        
        gems = {}
        for x, y in enumerate(self._headers):          
            index: QModelIndex = self.tokenModel.index(0, x)
            model = index.data(Qt.EditRole)
            print(f"{y}:{model}")
            gems[y] = model
        
        try:          
            # print(gems)
            self.gameActions.withdrawGems(gems)
            parent.close()
        except RuntimeError as e:
            print(e)
            errorDialog = QtWidgets.QErrorMessage(parent)
            errorDialog.showMessage( str(e))

class GemDialog(QDialog, QObject):   
        
    save = pyqtSignal(QAbstractItemView)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create an instance of the GUI
        self.ui = Ui_Dialog()

        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.gemsAvailableTable.setModel(parent.tokenModel)
 
    def accept(self):
        print("do nothing")
        self.save.emit(self)

if QtCore.QT_VERSION >= 0x50501:
    def excepthook(type_, value, traceback_):
        traceback.print_exception(type_, value, traceback_)
        QtCore.qFatal('')
sys.excepthook = excepthook
   
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()