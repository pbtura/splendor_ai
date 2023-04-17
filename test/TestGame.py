'''
Created on Apr 14, 2023

@author: bucpa
'''
import unittest

from ResourceCard import ResourceCard
from GameState import GameState
from Color import Color
from Cost import Cost
from TokenStore import TokenStore
from NobleCard import NobleCard
from Player import Player
from typing import Iterable

class TestGame(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def assertNobleDeckInitialized(self, deck: Iterable[NobleCard]):
        self.assertIsNotNone(deck)
        self.assertEqual(10, len(deck))

    def assertResourceDeckInitialized(self,  decks: dict):
        self.assertIsNotNone(decks)
        self.assertEqual(40, len(decks.get(1)))
        self.assertEqual(30, len(decks.get(2)))
        self.assertEqual(20, len(decks.get(3)))
        
        card: ResourceCard
        for card in decks.get(1):
            self.assertEqual(1, card.level)
        
        for card in decks.get(2):
            self.assertEqual(2, card.level)
        
        for card in decks.get(3):
            self.assertEqual(3, card.level)

    def assertAvailableGemsInitialized(self, gems: TokenStore):
        self.assertEqual(7, gems.tokens[Color.WHITE])
        self.assertEqual(7, gems.tokens[Color.BLUE])
        self.assertEqual(7, gems.tokens[Color.GREEN])
        self.assertEqual(7, gems.tokens[Color.RED])
        self.assertEqual(7, gems.tokens[Color.BLACK])
        self.assertEqual(5, gems.tokens[Color.GOLD])
        
    def assertAvailableGemsInitializedForThreePlayers(self, gems: TokenStore):
        self.assertEqual(5, gems.tokens[Color.WHITE])
        self.assertEqual(5, gems.tokens[Color.BLUE])
        self.assertEqual(5, gems.tokens[Color.GREEN])
        self.assertEqual(5, gems.tokens[Color.RED])
        self.assertEqual(5, gems.tokens[Color.BLACK])
        self.assertEqual(5, gems.tokens[Color.GOLD])
    
    def assertAvailableGemsInitializedForTwoPlayers(self, gems: TokenStore):
        self.assertEqual(4, gems.tokens[Color.WHITE])
        self.assertEqual(4, gems.tokens[Color.BLUE])
        self.assertEqual(4, gems.tokens[Color.GREEN])
        self.assertEqual(4, gems.tokens[Color.RED])
        self.assertEqual(4, gems.tokens[Color.BLACK])
        self.assertEqual(5, gems.tokens[Color.GOLD])
        
    def assertAvailableResourcesDealt(self, resourceDeck: dict, actualDeck1, actualDeck2, actualDeck3, shuffled: bool, expected1: list[ResourceCard] = None, expected2: list[ResourceCard]= None, expected3: list[ResourceCard] = None):
        #we want to test that the top 4 cards 
        #have been moved to the availableResources deck
        self.assertEqual(36, len(resourceDeck.get(1)))
        self.assertEqual(26, len(resourceDeck.get(2)))
        self.assertEqual(16, len(resourceDeck.get(3)))
                     
        self.assertEquals(4, len(actualDeck1))
        self.assertEquals(4, len(actualDeck2))
        self.assertEquals(4, len(actualDeck3))
        
        #if the deck has been randomized, we don't want to do the equality check
        if not shuffled:
            for idx, card in enumerate(actualDeck1):
                self.assertResourceCardsEqual(expected1[idx], card)
                
            for idx, card in enumerate(actualDeck2):
                self.assertResourceCardsEqual(expected2[idx], card)
                
            for idx, card in enumerate(actualDeck3):
                self.assertResourceCardsEqual(expected3[idx], card)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()