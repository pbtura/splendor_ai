'''
Created on Apr 14, 2023

@author: bucpa
'''
import unittest
from TestGame import TestGame
from GameActions import GameActions
from GameState import GameState


class TestActions(TestGame):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testInitialize(self):
        actions:GameActions = GameActions(["playerA", "playerB", "playerC", "playerD"], 1)
        game:GameState = actions.game
       
        #check players were initialized
        self.assertEqual(4, len(game.players))       
        
        #check that the token bank was initialized
        self.assertAvailableGemsInitialized(game.availableGems)
        
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
        
        self.assertIsNotNone(actions)
        pass
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()