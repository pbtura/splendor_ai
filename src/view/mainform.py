# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bucpa\OneDrive\Documents\eclipse\workspace\splendor_ai\splendor_ui\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1602, 961)
        self.layoutWidget = QtWidgets.QWidget(Widget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 60, 1561, 746))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.playersListView = QtWidgets.QListView(self.layoutWidget)
        self.playersListView.setObjectName("playersListView")
        self.verticalLayout.addWidget(self.playersListView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playerName = QtWidgets.QLabel(self.layoutWidget)
        self.playerName.setObjectName("playerName")
        self.horizontalLayout.addWidget(self.playerName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.currentPoints = QtWidgets.QLabel(self.layoutWidget)
        self.currentPoints.setObjectName("currentPoints")
        self.horizontalLayout.addWidget(self.currentPoints)
        self.currentPointsLabel = QtWidgets.QLabel(self.layoutWidget)
        self.currentPointsLabel.setObjectName("currentPointsLabel")
        self.horizontalLayout.addWidget(self.currentPointsLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.currentCardsLabel = QtWidgets.QLabel(self.layoutWidget)
        self.currentCardsLabel.setObjectName("currentCardsLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.currentCardsLabel)
        self.purchasedCardsList = QtWidgets.QListView(self.layoutWidget)
        self.purchasedCardsList.setObjectName("purchasedCardsList")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.purchasedCardsList)
        self.reservedCardsLabel = QtWidgets.QLabel(self.layoutWidget)
        self.reservedCardsLabel.setObjectName("reservedCardsLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.reservedCardsLabel)
        self.reservedCardsList = QtWidgets.QListView(self.layoutWidget)
        self.reservedCardsList.setObjectName("reservedCardsList")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reservedCardsList)
        self.gemsLabel = QtWidgets.QLabel(self.layoutWidget)
        self.gemsLabel.setObjectName("gemsLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.gemsLabel)
        self.playerGemsTable = GemTableView(self.layoutWidget)
        self.playerGemsTable.setObjectName("playerGemsTable")
        self.playerGemsTable.horizontalHeader().setDefaultSectionSize(60)
        self.playerGemsTable.horizontalHeader().setMinimumSectionSize(40)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.playerGemsTable)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lvOneCardsTable = QtWidgets.QTableView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lvOneCardsTable.sizePolicy().hasHeightForWidth())
        self.lvOneCardsTable.setSizePolicy(sizePolicy)
        self.lvOneCardsTable.setMinimumSize(QtCore.QSize(50, 0))
        self.lvOneCardsTable.setObjectName("lvOneCardsTable")
        self.verticalLayout_2.addWidget(self.lvOneCardsTable)
        self.lvTwoCardsTable = QtWidgets.QTableView(self.layoutWidget)
        self.lvTwoCardsTable.setObjectName("lvTwoCardsTable")
        self.verticalLayout_2.addWidget(self.lvTwoCardsTable)
        self.lvThreeCardsTable = QtWidgets.QTableView(self.layoutWidget)
        self.lvThreeCardsTable.setObjectName("lvThreeCardsTable")
        self.verticalLayout_2.addWidget(self.lvThreeCardsTable)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.layoutWidget1 = QtWidgets.QWidget(Widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 900, 521, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.gameActionsLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.gameActionsLabel.setObjectName("gameActionsLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.gameActionsLabel)
        self.gameActionsDropdown = QtWidgets.QComboBox(self.layoutWidget1)
        self.gameActionsDropdown.setMinimumSize(QtCore.QSize(82, 0))
        self.gameActionsDropdown.setObjectName("gameActionsDropdown")
        self.gameActionsDropdown.addItem("")
        self.gameActionsDropdown.addItem("")
        self.gameActionsDropdown.addItem("")
        self.gameActionsDropdown.addItem("")
        self.gameActionsDropdown.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.gameActionsDropdown)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.endTurnButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.endTurnButton.setObjectName("endTurnButton")
        self.horizontalLayout_3.addWidget(self.endTurnButton)
        self.actionitem_select = QtWidgets.QAction(Widget)
        self.actionitem_select.setObjectName("actionitem_select")

        self.retranslateUi(Widget)
        self.gameActionsDropdown.currentIndexChanged['int'].connect(self.actionitem_select.trigger) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.playerName.setText(_translate("Widget", "TextLabel"))
        self.currentPoints.setText(_translate("Widget", "Points:"))
        self.currentPointsLabel.setText(_translate("Widget", "TextLabel"))
        self.currentCardsLabel.setText(_translate("Widget", "Cards Owned"))
        self.reservedCardsLabel.setText(_translate("Widget", "Cards Reserved"))
        self.gemsLabel.setText(_translate("Widget", "Current Gems"))
        self.gameActionsLabel.setText(_translate("Widget", "Actions"))
        self.gameActionsDropdown.setItemText(0, _translate("Widget", "..."))
        self.gameActionsDropdown.setItemText(1, _translate("Widget", "Take Gems"))
        self.gameActionsDropdown.setItemText(2, _translate("Widget", "Buy Card"))
        self.gameActionsDropdown.setItemText(3, _translate("Widget", "Reserve Card"))
        self.gameActionsDropdown.setItemText(4, _translate("Widget", "Claim Reserved Card"))
        self.endTurnButton.setText(_translate("Widget", "End Turn"))
        self.actionitem_select.setText(_translate("Widget", "item select"))
from view.widgets.GemTableView import GemTableView


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())
