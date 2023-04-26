'''
Created on Apr 25, 2023

@author: bucpa
'''
from PyQt5 import QtCore
import PyQt5.Qt as qt

class GemTableView(qt.QTableView):
    '''
    classdocs
    '''


    def __init__(self,  *args, **kwargs):
        '''
        Constructor
        '''
        qt.QTableView.__init__(self,  *args, **kwargs)
        # combo = self.setItemDelegateForColumn(0, ComboDelegate(self))
        # self.setItemDelegateForColumn(1, ComboDelegate(self))


class ComboDelegate(qt.QItemDelegate):
    """
    A delegate that places a fully functioning QComboBox in every
    cell of the column to which it's applied
    """
    def __init__(self, parent):

        qt.QItemDelegate.__init__(self, parent)
        
    def createEditor(self, parent, option, index):
        combo = qt.QComboBox(parent)
        li = []
        li.append("Zero")
        li.append("One")
        li.append("Two")
        li.append("Three")
        li.append("Four")
        li.append("Five")
        combo.addItems(li)
        self.connect(combo, self.currentIndexChanged)
        return combo
        
    def setEditorData(self, editor, index):
        editor.blockSignals(True)
        editor.setCurrentIndex(int(index.model().data(index)))
        editor.blockSignals(False)
        
    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentIndex())
        
    @QtCore.pyqtSlot()
    def currentIndexChanged(self):
        self.commitData.emit(self.sender())
    