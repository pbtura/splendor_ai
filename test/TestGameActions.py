'''
Created on Apr 14, 2023

@author: bucpa
'''
import unittest
import os

from Cost import Cost
from NobleCard import NobleCard
from TestGame import TestGame
from GameActions import GameActions
from GameState import GameState


class TestActions(TestGame):

    def setUp(self):
        pass

    def tearDown(self):
        self.game = None
        self.actions = None

    def initGame(self, random: bool):
        self.actions: GameActions = GameActions(["playerA", "playerB", "playerC", "playerD"], random,
                                                os.path.join('..', 'resources', 'cards_list.csv'),
                                                os.path.join('..', 'resources', 'nobles_list.csv'))
        self.game: GameState = self.actions.game

    def testInitialize(self):
        self.initGame(True)
        # check players were initialized
        self.assertEqual(4, len(self.game.players))

        # check that the token bank was initialized
        self.assertAvailableGemsInitialized(self.game.availableGems)

        # check randomize turn order
        self.assertTrue(self.game.playersRandomized)
        # check randomize resource deck
        self.assertTrue(self.game.resourcesShuffled)
        # check randomize noble deck
        self.assertTrue(self.game.noblesShuffled)

        # check deal resource cards
        actualDeck1: list = self.game.availableResources.get(1)
        actualDeck2: list = self.game.availableResources.get(2)
        actualDeck3: list = self.game.availableResources.get(3)
        self.assertAvailableResourcesDealt(self.game.resourceDeck, actualDeck1, actualDeck2, actualDeck3, True)

        # check deal noble cards
        self.assertEqual(5, len(self.game.noblesDeck))
        self.assertEqual(5, len(self.game.availableNobles))

        self.assertIsNotNone(self.actions)

    def testGetAffordableNobles(self):
        self.initGame(False)
        # noble 1: 4G, 4R
        expectedNoble: NobleCard = self.game.availableNobles[0]
        expectedCost: Cost = Cost(0, 0, 4, 4, 0)
        self.assertEqual(expectedCost, expectedNoble.cost)

        # setup the resource cards
        rc: list = self.game.resourceDeck.get(1)
        self.actions.currentPlayer.cards = [rc[20], rc[21], rc[22], rc[23], rc[28], rc[29], rc[30], rc[31]]

        actualNobles = self.actions.findAffordableNobles()
        self.assertEqual(1, len(actualNobles))

    def testGetTwoAffordableNobles(self):
        self.initGame(False)
        # noble 2: 3W, 3R, 3B
        expectedNoble: NobleCard = self.game.availableNobles[1]
        expectedCost: Cost = Cost(3, 0, 0, 3, 3)
        self.assertEqual(expectedCost, expectedNoble.cost)

        # setup the resource cards
        rc: list = self.game.resourceDeck.get(1)
        self.actions.currentPlayer.cards = [rc[12], rc[13], rc[14], rc[20], rc[21], rc[22], rc[23], rc[28], rc[29], rc[30], rc[31], rc[0], rc[1], rc[2]]

        actualNobles = self.actions.findAffordableNobles()
        self.assertEqual(2, len(actualNobles))

    def testGetZeroAffordableNobles(self):
        self.initGame(False)
        # noble 1: 4G, 4R
        expectedNoble: NobleCard = self.game.availableNobles[0]
        expectedCost: Cost = Cost(0, 0, 4, 4, 0)
        self.assertEqual(expectedCost, expectedNoble.cost)

        # setup the resource cards
        rc: list = self.game.resourceDeck.get(1)
        self.actions.currentPlayer.cards = [rc[20], rc[21], rc[22], rc[23], rc[28], rc[29], rc[30], rc[0]]

        actualNobles = self.actions.findAffordableNobles()
        self.assertEqual(0, len(actualNobles))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
