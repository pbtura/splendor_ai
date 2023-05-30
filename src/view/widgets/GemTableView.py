'''
Created on Apr 25, 2023

@author: bucpa
'''
from PyQt5 import QtCore
import PyQt5.Qt as qt
from PyQt5.QtCore import Qt
from PyQt5.Qt import QAbstractTableModel

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
        
    def setModel(self, model: QAbstractTableModel):
        super().setModel(model)
        
        r: int = 0
        while r < model.rowCount(0):              
            i: int = 0
            while i < model.columnCount(r):
                flags = model.flags(model.index(r, i))    
                if(flags & Qt.ItemIsEditable):
                    self.openPersistentEditor(model.index(r, i))
                i+=1
            r += 1
            
# class ComboDelegate(qt.QItemDelegate):
#     """
#     A delegate that places a fully functioning QComboBox in every
#     cell of the column to which it's applied
#     """
#     def __init__(self, parent):
#
#         qt.QItemDelegate.__init__(self, parent)
#
#     def createEditor(self, parent, option, index):
#         combo = qt.QComboBox(parent)
#         li = []
#         li.append("Zero")
#         li.append("One")
#         li.append("Two")
#         li.append("Three")
#         li.append("Four")
#         li.append("Five")
#         combo.addItems(li)
#         self.connect(combo, self.currentIndexChanged)
#         return combo
#
#     def setEditorData(self, editor, index):
#         editor.blockSignals(True)
#         editor.setCurrentIndex(int(index.model().data(index)))
#         editor.blockSignals(False)
#
#     def setModelData(self, editor, model, index):
#         model.setData(index, editor.currentIndex())
#
#     @QtCore.pyqtSlot()
#     def currentIndexChanged(self):
#         self.commitData.emit(self.sender())
#
