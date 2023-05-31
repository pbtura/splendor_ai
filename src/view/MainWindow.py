'''
Created on Apr 21, 2023

@author: bucpa
'''
import sys
import traceback
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from GameActions import GameActions
from view.gem_dialog import Ui_Dialog
from view.model.NobleCardModel import NobleCardModel
from view.model.PlayerList import PlayerList
from view.widgets.GemDialog import GemDialog
from view.widgets.GemTableView import GemTableView
from TokenStore import TokenStore
from view.model.TokenStoreModel import TokenStoreModel
from Color import Color
from Player import Player
from ResourceCard import ResourceCard
from view.model.ResourceCardModel import ResourceCardModel
from PyQt5.Qt import QModelIndex, pyqtSignal, QObject, QAbstractItemView

from view.mainform import Ui_Widget


class MainWindow(QtWidgets.QMainWindow, Ui_Widget):
    '''
    classdocs
    '''
    gameActions: GameActions
    _headers = [Color.WHITE, Color.BLUE, Color.GREEN, Color.RED, Color.BLACK]
    _playerCardsModel: ResourceCardModel
    _selectedCard: ResourceCard
    _reservedCard: ResourceCard
    tokenModel: TokenStoreModel

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

        headersList = self._headers
        headersList.append(Color.GOLD)

        # initialize the gems bank
        bank = self.gameActions.game.availableGems
        data: list = [["gems available", bank]]

        tokenModel = TokenStoreModel(data, headersList, [0])
        self.bankGemsTable.setModel(tokenModel)

        self.withdrawGemsButton.clicked.connect(self.openGemDialog)

        # populate the player gems table
        data: list = [["", self.gameActions.currentPlayer.gems]]
        self._playerGemModel = TokenStoreModel(data, headersList, [0])
        self.playerGemsTable.setModel(self._playerGemModel)

        self.cards = self.gameActions.game.availableResources
        self.purchaseCardButton.setEnabled(False)
        self.reserveCardButton.setEnabled(False)
        self.purchaseReservedButton.setEnabled(False)

        self.lvOneModel = ResourceCardModel(self.cards.get(1))
        self.lvTwoModel = ResourceCardModel(self.cards.get(2))
        self.lvThreeModel = ResourceCardModel(self.cards.get(3))

        self.lvOneCardsTable.setModel(self.lvOneModel)
        self.lvTwoCardsTable.setModel(self.lvTwoModel)
        self.lvThreeCardsTable.setModel(self.lvThreeModel)

        self.lvOneCardsTable.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.lvTwoCardsTable.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.lvThreeCardsTable.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        self.lvOneCardsTable.clicked.connect(
            lambda index, model=self.lvOneModel: self.resourceCardSelected(index, model))
        self.lvTwoCardsTable.clicked.connect(
            lambda index, model=self.lvTwoModel: self.resourceCardSelected(index, model))
        self.lvThreeCardsTable.clicked.connect(
            lambda index, model=self.lvThreeModel: self.resourceCardSelected(index, model))

        # setup the available nobles table
        self.availableNoblesModel = NobleCardModel(self.gameActions.availableNobles)
        self.availableNoblesTable.setModel(self.availableNoblesModel)

        # setup the reserved cards table
        reservedCardsModel = ResourceCardModel(self.gameActions.currentPlayer.reservedCards)
        self.reservedCardsTable.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.reservedCardsTable.setModel(reservedCardsModel)
        self.reservedCardsTable.clicked.connect(lambda index, model=reservedCardsModel: self.reservedCardSelected(index, model))

        self.purchaseReservedButton.clicked.connect(self.claimReservedClicked)

        # setup the purchase and reserve buttons
        self.purchaseCardButton.clicked.connect(self.purchaseButtonClicked)
        self.reserveCardButton.clicked.connect(self.reserveCardButtonClicked)

        # setup the end turn button
        self.endTurnButton.clicked.connect(self.handleEndTurnClicked)

        self.updatePlayerData()

    @property
    def selectedCard(self) -> ResourceCard:
        return self._selectedCard

    @selectedCard.setter
    def selectedCard(self, card: ResourceCard):
        self._selectedCard = card
        # enable/disable the purchase and reserve buttons here
        if card is None:
            self.purchaseCardButton.setEnabled(False)
            self.reserveCardButton.setEnabled(False)
        else:
            self.purchaseCardButton.setEnabled(True)
            self.reserveCardButton.setEnabled(True)

    @property
    def reservedCard(self) -> ResourceCard:
        return self._reservedCard

    @reservedCard.setter
    def reservedCard(self, card: ResourceCard):
        self._reservedCard = card
        # enable/disable the purchase and reserve buttons here
        if card is None:
            self.purchaseReservedButton.setEnabled(False)
        else:
            self.purchaseReservedButton.setEnabled(True)

    def resourceCardSelected(self, item: QModelIndex, model: ResourceCardModel):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ControlModifier:
            self.selectedCard = None
        else:
            self.selectedCard = model.getRow(item, Qt.UserRole)
            # msgDialog = QtWidgets.QMessageBox(self)
            # msgDialog.setText(str(self.selectedCard))
            # msgDialog.show()

    def reservedCardSelected(self, item: QModelIndex, model: ResourceCardModel):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers == QtCore.Qt.ControlModifier:
            self.reservedCard = None
        else:
            self.reservedCard = model.getRow(item, Qt.UserRole)

    def purchaseButtonClicked(self):
        self.openPurchaseCardDialog(self.selectedCard)

    def reserveCardButtonClicked(self):
        self.gameActions.reserveCard(self.selectedCard.level, self.selectedCard)
        self.updatePlayerData()

    def claimReservedClicked(self):
        self.openClaimCardDialog(self.reservedCard)

    def updatePlayerData(self):
        player = self.gameActions.currentPlayer
        self.playerName.setText(player.name)
        self.currentPointsLabel.setText(str(player.getTotalPoints()))
        self._playerCardsModel = ResourceCardModel(player.cards)
        self.purchasedCardsTable.setModel(self._playerCardsModel)
        self.reservedCardsTable.setModel(ResourceCardModel(player.reservedCards))
        self.refreshPlayerGems()
        self.purchaseCardButton.setEnabled(False)
        self.reserveCardButton.setEnabled(False)
        self.purchaseReservedButton.setEnabled(False)

    def refreshPlayerGems(self):
        data: list = [["Currently held", self.gameActions.currentPlayer.gems]]
        self._playerGemModel.refreshData(data)

    def openGemDialog(self):

        bank = self.gameActions.game.availableGems

        currentPlayer = self.gameActions.currentPlayer

        data: list = [["to withdraw:", TokenStore(0, 0, 0, 0, 0, 0)], ["gems available", bank],
                      ["Currently held", currentPlayer.gems]]

        self.tokenModel = TokenStoreModel(data, self._headers, [1, 0, 0])

        dlg = GemDialog(self)
        dlg.save.connect(self.handleGemsUpdated)
        dlg.exec()

    def handleGemsUpdated(self, parent):

        gems = {}
        for x, y in enumerate(self._headers):
            index: QModelIndex = self.tokenModel.index(0, x)
            model = index.data(Qt.EditRole)
            # print(f"{y}:{model}")
            gems[y] = model

        try:
            # print(gems)
            self.gameActions.withdrawGems(gems)
            parent.close()
            self.updatePlayerData()
        except RuntimeError as e:
            print(e)
            errorDialog = QtWidgets.QErrorMessage(parent)
            errorDialog.showMessage(str(e))

    def openPurchaseCardDialog(self, card: ResourceCard) -> None:
        bank = self.gameActions.game.availableGems

        currentPlayer = self.gameActions.currentPlayer

        data: list = [["Card cost:", card.cost.getAsTokens()],
                      ["Currently held", currentPlayer.gems], ["gems to pay", TokenStore(0, 0, 0, 0, 0, 0)]]

        self.tokenModel = TokenStoreModel(data, self._headers, [0, 0, 1])

        dlg = GemDialog(self)
        dlg.save.connect(self.handleCardPurchased)
        dlg.exec()

    def handleCardPurchased(self, parent):

        gems = {}
        for x, y in enumerate(self._headers):
            index: QModelIndex = self.tokenModel.index(2, x)
            model = index.data(Qt.EditRole)
            # print(f"{y}:{model}")
            gems[y] = model

        try:
            self.gameActions.purchaseCard(self.selectedCard.level, self.selectedCard, gems)
            parent.close()
            self.updatePlayerData()
        except RuntimeError as e:
            print(e)
            errorDialog = QtWidgets.QErrorMessage(parent)
            errorDialog.showMessage(str(e))

    def openClaimCardDialog(self, card: ResourceCard) -> None:
        bank = self.gameActions.game.availableGems

        currentPlayer = self.gameActions.currentPlayer

        data: list = [["Card cost:", card.cost.getAsTokens()],
                      ["Currently held", currentPlayer.gems], ["gems to pay", TokenStore(0, 0, 0, 0, 0, 0)]]

        self.tokenModel = TokenStoreModel(data, self._headers, [0, 0, 1])

        dlg = GemDialog(self)
        dlg.save.connect(self.handleCardClaimed)
        dlg.exec()

    def handleCardClaimed(self, parent):
        gems = {}
        for x, y in enumerate(self._headers):
            index: QModelIndex = self.tokenModel.index(2, x)
            model = index.data(Qt.EditRole)
            # print(f"{y}:{model}")
            gems[y] = model

        try:
            self.gameActions.claimReservedCard(self.selectedCard, gems)
            parent.close()
            self.updatePlayerData()
        except RuntimeError as e:
            print(e)
            errorDialog = QtWidgets.QErrorMessage(parent)
            errorDialog.showMessage(str(e))

    def handleEndTurnClicked(self):
        self.gameActions.endTurn()
        self.updatePlayerData()

if QtCore.QT_VERSION >= 0x50501:
    def excepthook(type_, value, traceback_):
        traceback.print_exception(type_, value, traceback_)
        QtCore.qFatal('')
sys.excepthook = excepthook

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
