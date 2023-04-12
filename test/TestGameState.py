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
    
    def testImportResourceDecks(self):
        decks: dict = None
        with open(os.path.join('..','resources','cards_list.csv'), newline='') as f:
            reader = csv.DictReader(f)
            decks = GameState.importResourceDecks(reader)
        
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

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseResourceRow']
    unittest.main()