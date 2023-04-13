'''
Created on Apr 12, 2023

@author: bucpa
'''
import unittest
import os
import csv
from _collections_abc import Iterable
from ResourceCard import ResourceCard
from GameState import GameState
from Color import Color
from Cost import Cost
from TokenStore import TokenStore
from NobleCard import NobleCard


class TestGameState(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def assertResourceCardsEqual(self,expected:ResourceCard, actual:ResourceCard):
        self.assertEqual(expected.level, actual.level)
        self.assertEqual(expected.points, actual.points)
        self.assertEqual(expected.suit, actual.suit)
        self.assertEqual(expected.cost, actual.cost)
    
    def assertNobleCardsEqual(self,expected:NobleCard, actual:NobleCard):
        self.assertEqual(expected.points, actual.points)
        self.assertEqual(expected.cost, actual.cost)
        
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
    
    def assertNobleDeckInitialized(self, deck: Iterable[NobleCard]):
        self.assertIsNotNone(deck)
        self.assertEqual(10, len(deck))
    
    def testImportResourceDecks(self):
        decks: dict = None
        with open(os.path.join('..','resources','cards_list.csv'), newline='') as f:
            reader = csv.DictReader(f)
            decks = GameState.importResourceDecks(reader)
        
        self.assertResourceDeckInitialized(decks)
            
        pass
    
    def testParseResourceRow(self):
    
        rowData: dict = {'Level':1,'Gem color':"BLUE",'PV':0, 'Price':"2g+2k",'white':0,'blue':0,'green':2,'red':0,'black':2}
        #(white, blue, green, red, black)
        expectedCost:Cost = Cost( 0,0,2,0,2)
        expectedCard:ResourceCard = ResourceCard( 1, Color.BLUE, expectedCost, 0)
        actualCard:ResourceCard = GameState.parseResourceRow(rowData)
        self.assertIsNotNone(actualCard)
        self.assertResourceCardsEqual(expectedCard, actualCard);
        pass
    
    def testInitializeResourceDeck(self):
        game: GameState = GameState(2)
        game.initializeResourceDecks()
        
        self.assertResourceDeckInitialized(game.resourceDeck)
        pass
    
    def testInitializeAvailableGemsForTwoPlayers(self):
        
        gems: TokenStore = GameState.initializeAvailableGems(2)
        
        self.assertEqual(4, gems.tokens[Color.WHITE])
        self.assertEqual(4, gems.tokens[Color.BLUE])
        self.assertEqual(4, gems.tokens[Color.GREEN])
        self.assertEqual(4, gems.tokens[Color.RED])
        self.assertEqual(4, gems.tokens[Color.BLACK])
        self.assertEqual(5, gems.tokens[Color.GOLD])
        pass
    
    def testInitializeAvailableGemsForThreePlayers(self):
        
        gems: TokenStore = GameState.initializeAvailableGems(3)
        
        self.assertEqual(5, gems.tokens[Color.WHITE])
        self.assertEqual(5, gems.tokens[Color.BLUE])
        self.assertEqual(5, gems.tokens[Color.GREEN])
        self.assertEqual(5, gems.tokens[Color.RED])
        self.assertEqual(5, gems.tokens[Color.BLACK])
        self.assertEqual(5, gems.tokens[Color.GOLD])
        pass
    
    def testInitializeAvailableGemsForFourPlayers(self):
        
        gems: TokenStore = GameState.initializeAvailableGems(4)
        
        self.assertEqual(7, gems.tokens[Color.WHITE])
        self.assertEqual(7, gems.tokens[Color.BLUE])
        self.assertEqual(7, gems.tokens[Color.GREEN])
        self.assertEqual(7, gems.tokens[Color.RED])
        self.assertEqual(7, gems.tokens[Color.BLACK])
        self.assertEqual(5, gems.tokens[Color.GOLD])
        pass
    
    def testParseNobleRow(self):
        rowData: dict = {'PV':3, 'white':0,'blue':0,'green':4,'red':0,'black':4}
        expectedCost:Cost = Cost( 0,0,4,0,4)
        expectedCard:NobleCard = NobleCard( expectedCost, 3)
        actualCard:NobleCard = GameState.parseNobleRow(rowData)
        self.assertIsNotNone(actualCard)
        self.assertNobleCardsEqual(expectedCard, actualCard);
        pass
    
    def testImportNobleDeck(self):
        decks: dict = None
        with open(os.path.join('..','resources','nobles_list.csv'), newline='') as f:
            reader = csv.DictReader(f)
            decks = GameState.importNobleDeck(reader)
        
        self.assertNobleDeckInitialized(decks)            
        pass
    
    def testInitializeNobleDeck(self):
        game: GameState = GameState(2)
        game.initializeNobleDeck()
        
        self.assertNobleDeckInitialized(game.noblesDeck)
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseResourceRow']
    unittest.main()