from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QDialog, QAbstractItemView

from view.gem_dialog import Ui_Dialog


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

