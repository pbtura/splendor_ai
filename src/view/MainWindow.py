'''
Created on Apr 21, 2023

@author: bucpa
'''
import sys
from view.mainform import Ui_Widget
from view.gem_dialog import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog

class MainWindow(QtWidgets.QMainWindow, Ui_Widget):
    '''
    classdocs
    '''


    def __init__(self, *args, obj=None, **kwargs):
        '''
        Constructor
        '''
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setupUi(self)
        self.gameActionsDropdown.currentIndexChanged.connect(self.onTakeGemsSelected)
    
    def onTakeGemsSelected(self):
        print("dd changed")
        dlg = GemDialog(self)
        dlg.exec()
 
class GemDialog(QDialog):   
        
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
    
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()