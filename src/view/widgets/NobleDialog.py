from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QDialog, QAbstractItemView

from view.noble_dialog import Ui_NobleDialog


class NobleDialog(QDialog, QObject):
    save = pyqtSignal(QAbstractItemView)

    def __init__(self, parent=None):
        super().__init__(parent)

        # Create an instance of the GUI
        self.ui = Ui_NobleDialog()

        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        self.ui.noblesAvailableTable.setModel(parent.affordableNobles)

    def accept(self):
        self.save.emit(self)

