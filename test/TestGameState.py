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
from Player import Player


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
        game: GameState = GameState()
        game.initializeResourceDecks()
        
        self.assertResourceDeckInitialized(game.resourceDeck)
        pass
    
    def testInitializeAvailableGemsForTwoPlayers(self):
        
        game: GameState = GameState()
        game.addPlayers(["a", "b"])
        game.initializeAvailableGems()
        
        self.assertAvailableGemsInitializedForTwoPlayers(game.availableGems)
        pass
    
    def testInitializeAvailableGemsForThreePlayers(self):
        
        game: GameState = GameState()
        game.addPlayers(["a", "b", "c"])
        game.initializeAvailableGems()
        
        self.assertAvailableGemsInitializedForThreePlayers(game.availableGems)
        pass
    
    def testInitializeAvailableGemsForFourPlayers(self):
        
        game: GameState = GameState()
        game.addPlayers(["a", "b", "c", "d"])
        game.initializeAvailableGems()
        
        self.assertAvailableGemsInitialized(game.availableGems)
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
        game: GameState = GameState()
        game.initializeNobleDeck()
        
        self.assertNobleDeckInitialized(game.noblesDeck)
        pass
    
    def testAddPlayers(self):
        game: GameState = GameState()
        playerNames = ["playerA", "playerB"]
        game.addPlayers(playerNames)
        self.assertIsNotNone(game.players)
        self.assertEqual(2, len(game.players))
        
        player:Player
        for index, player in enumerate(game.players):
            self.assertEqual(playerNames[index], player.name)
        pass
    
    def testDealResourceCards(self):
        
        game: GameState = GameState()
        game.initializeResourceDecks()
        deck1: list[ResourceCard] = game.resourceDeck.get(1)
        expected1: list[ResourceCard] = [deck1[0], deck1[1], deck1[2], deck1[3]]
        
        game.dealResourceCards(1, 4)
        #we want to test that the top 4 cards 
        #have been moved to the availableResources deck
        self.assertEqual(36, len(game.resourceDeck.get(1)))
        actualDeck1:list = game.availableResources.get(1)
        self.assertEquals(4, len(actualDeck1))
        for idx, card in enumerate(actualDeck1):
            self.assertResourceCardsEqual(expected1[idx], card)
            
        pass
    
    def testDealNobleCards(self):
        game: GameState = GameState()
        game.initializeNobleDeck()
        game.dealNobleCards(4);
        
        self.assertEqual(5,len(game.availableNobles))
        pass
    
    def testDealNobleCardsForThreePlayers(self):
        game: GameState = GameState()
        game.initializeNobleDeck()
        game.dealNobleCards(3);
        
        self.assertEqual(4,len(game.availableNobles))
        pass
    
    def testDealNobleCardsForTwoPlayers(self):
        game: GameState = GameState()
        game.initializeNobleDeck()
        game.dealNobleCards(2);
        
        self.assertEqual(3,len(game.availableNobles))
        pass
    
    def testInitializeAvailableResourceCards(self):
        game: GameState = GameState()
        game.initializeResourceDecks()
        deck1: list[ResourceCard] = game.resourceDeck.get(1)
        deck2: list[ResourceCard] = game.resourceDeck.get(2)
        deck3: list[ResourceCard] = game.resourceDeck.get(3)
        
        expected1: list[ResourceCard] = [deck1[0], deck1[1], deck1[2], deck1[3]]
        expected2: list[ResourceCard] = [deck2[0], deck2[1], deck2[2], deck2[3]]
        expected3: list[ResourceCard] = [deck3[0], deck3[1], deck3[2], deck3[3]]
        
        game.initializeAvailableResourceCards()
        
        #we want to test that the top 4 cards 
        #have been moved to the availableResources deck
        self.assertEqual(36, len(game.resourceDeck.get(1)))
        self.assertEqual(26, len(game.resourceDeck.get(2)))
        self.assertEqual(16, len(game.resourceDeck.get(3)))
        
        actualDeck1:list = game.availableResources.get(1)
        actualDeck2:list = game.availableResources.get(2)
        actualDeck3:list = game.availableResources.get(3)
        
        self.assertEquals(4, len(actualDeck1))
        self.assertEquals(4, len(actualDeck2))
        self.assertEquals(4, len(actualDeck3))
        
        for idx, card in enumerate(actualDeck1):
            self.assertResourceCardsEqual(expected1[idx], card)
            
        for idx, card in enumerate(actualDeck2):
            self.assertResourceCardsEqual(expected2[idx], card)
            
        for idx, card in enumerate(actualDeck3):
            self.assertResourceCardsEqual(expected3[idx], card)
        
        pass

    def testSetupGame(self):
        names: list = ["playerA", "playerB", "playerC", "playerD"]
        game: GameState = GameState()
        game.setupGame(names)
        
        #check players were initialized
        self.assertEqual(4, len(game.players))
        
        #check resource cards were initialized
        self.assertResourceDeckInitialized(game.resourceDeck)
        
        #check the nobles deck was initialized
        self.assertNobleDeckInitialized(game.noblesDeck)
        
        #check that the token bank was initialized
        self.assertAvailableGemsInitialized(game.availableGems)
        
        pass
    
    def testStartNewGame(self):
        
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseResourceRow']
    unittest.main()