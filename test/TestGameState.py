'''
Created on Apr 12, 2023

@author: bucpa
'''
import unittest
import os
import csv
from ResourceCard import ResourceCard
from GameState import GameState
from Color import Color
from Cost import Cost
from NobleCard import NobleCard
from Player import Player
from TestGame import TestGame
from TokenStore import TokenStore


class TestGameState(TestGame):


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
        
        self.assertEqual(5, len(game.noblesDeck))
        self.assertEqual(5,len(game.availableNobles))
        pass
    
    def testDealNobleCardsForThreePlayers(self):
        game: GameState = GameState()
        game.initializeNobleDeck()
        game.dealNobleCards(3);
        
        self.assertEqual(6, len(game.noblesDeck))
        self.assertEqual(4,len(game.availableNobles))
        pass
    
    def testDealNobleCardsForTwoPlayers(self):
        game: GameState = GameState()
        game.initializeNobleDeck()
        game.dealNobleCards(2);
        
        self.assertEqual(7, len(game.noblesDeck))
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
        
        actualDeck1:list = game.availableResources.get(1)
        actualDeck2:list = game.availableResources.get(2)
        actualDeck3:list = game.availableResources.get(3)
        self.assertAvailableResourcesDealt(game.resourceDeck, actualDeck1, actualDeck2, actualDeck3, 0, expected1, expected2, expected3)
        
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
        
        names: list = ["playerA", "playerB", "playerC", "playerD"]
        game: GameState = GameState()
        game.setupGame(names)
        
        game.startNewGame(1)
        
        #check randomize turn order
        self.assertTrue(game.playersRandomized)
        #check randomize resource deck
        self.assertTrue(game.resourcesShuffled)
        #check randomize noble deck
        self.assertTrue(game.noblesShuffled)
        
        #check deal resource cards              
        actualDeck1:list = game.availableResources.get(1)
        actualDeck2:list = game.availableResources.get(2)
        actualDeck3:list = game.availableResources.get(3)
        self.assertAvailableResourcesDealt(game.resourceDeck, actualDeck1, actualDeck2, actualDeck3, 1)
        
        #check deal noble cards 
        self.assertEqual(5, len(game.noblesDeck))
        self.assertEqual(5,len(game.availableNobles))
        
        pass
    
    def createGame(self) -> GameState:
        names: list = ["playerA", "playerB", "playerC", "playerD"]
        game: GameState = GameState()
        game.setupGame(names)
        game.startNewGame(0)
        
        return game
    
    def testWithdrawGems(self):
        
        game: GameState = self.createGame()
        player: Player = game.players[0]

        #(white, blue, green, red, black)
        expectedCost:dict = {Color.BLUE: 1, Color.RED: 1, Color.BLACK: 1}
        
        game.withdrawGems(player, expectedCost)
        actualPlayer = game.players[0]
        
        for x in expectedCost.keys():
            #check that the gems were withdrawn from the game store
            self.assertEquals( 6, game.availableGems.tokens.get(x))
            
            #check that the gems were added to the player store
            self.assertEqual(1, actualPlayer.gems.tokens.get(x))
        
              
        pass
    
    def testWithdrawGemPair(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        #(white, blue, green, red, black)
        expectedCost:dict = {Color.BLUE: 2}
        
        game.withdrawGems(player, expectedCost)
        actualPlayer = game.players[0]
        
        for x in expectedCost.keys():
            #check that the gems were withdrawn from the game store
            self.assertEquals( 5, game.availableGems.tokens.get(x))
            
            #check that the gems were added to the player store
            self.assertEqual(2, actualPlayer.gems.tokens.get(x))
        
              
        pass
        
    def testWitdrawTooManyGems(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        #(white, blue, green, red, black)
        expectedCost:dict = {Color.WHITE: 1, Color.BLUE: 1, Color.RED: 1, Color.BLACK: 1}              
        
        with self.assertRaises(RuntimeError) as context:
            game.withdrawGems(player, expectedCost)
        self.assertEqual("No more than three gems may be withdrawn from the bank.", str(context.exception))             
    
    def testWithdrawMoreGemsThanAvailable(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        #(white, blue, green, red, black)
        expectedCost:dict = {Color.WHITE: 1}
        
        #withdraw gems until there are no white remaining
        i: int = 0
        while i < 6:
            game.withdrawGems(player, expectedCost)
            i=+1
        
        with self.assertRaises(RuntimeError) as context:
            game.withdrawGems(player, expectedCost)
        self.assertEqual("Cannot remove more gems than are in the store", str(context.exception))   
        
    def testWithdrawInvalidGemPair(self):
        game: GameState = self.createGame()
        player: Player = game.players[0]

        #(white, blue, green, red, black)
        expectedCost:dict = {Color.WHITE: 1}
        
        #withdraw gems until there are no white remaining
        i: int = 0
        while i < 3:
            game.withdrawGems(player, expectedCost)
            i=+1
        
        with self.assertRaises(RuntimeError) as context:
            game.withdrawGems(player, expectedCost)
        self.assertEqual("Cannot withdraw two matched gems when less than four remain.", str(context.exception))
    
    def testPurchaseCard(self):
        
        # game: GameState = self.createGame()
        # player: Player = game.players[0]
        #
        # deckKey: int = 1
        # cardIdx: int = 0
        # expected: ResourceCard = game.availableResources.get(deckKey)[cardIdx]
        # expectedCost:Cost = expected.cost
        
        self.fail("not implemented")
    
    def testPurchaseCardWithInsufficientGems(self):
        self.fail("not implemented")
    
    def testReserveCard(self):
        self.fail("not implemented")
    
    def testClaimNoble(self):
        self.fail("not implemented")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseResourceRow']
    unittest.main()