'''
Created on May 18, 2023

@author: bucpa
'''
import unittest
import os

from Player import Player
from GameActions import GameActions
from ResourceCard import ResourceCard
from Color import Color
from Cost import Cost
from typing import OrderedDict

class Test(unittest.TestCase):

    def setUp(self):
        self.actions = GameActions(["playerA", "playerB"], 1, os.path.join('..','resources','cards_list.csv'), os.path.join('..','resources','nobles_list.csv'))
        pass


    def tearDown(self):
        self.actions = None
        pass
    
    def testGetResourceTotals(self):
        player:Player = self.actions.currentPlayer
        
        expectedTotals: OrderedDict={Color.WHITE: 0, Color.BLUE: 0, Color.GREEN: 0, Color.RED: 2, Color.BLACK: 1} 

        #add resource cards
        crd1: ResourceCard = ResourceCard(1, Color.RED, Cost(3,0,0,0,0) ,0)
        crd2: ResourceCard = ResourceCard(1, Color.BLACK, Cost(0,0,3,0,0) ,1)
        crd3: ResourceCard = ResourceCard(1, Color.RED, Cost(3,0,0,0,0) ,2)
        player.cards.append(crd1)
        player.cards.append(crd2)
        player.cards.append(crd3)
        
        actualTotals: OrderedDict = player.getResourceTotals()
        for key, value in actualTotals.items():
            self.assertEqual(expectedTotals.get(key), value)


    def testGetPoints(self):

        player = self.actions.currentPlayer
        
        #add resource cards
        crd1: ResourceCard = ResourceCard(1, Color.RED, Cost(3,0,0,0,0) ,2)
        crd2: ResourceCard = ResourceCard(1, Color.BLACK, Cost(0,0,3,0,0) ,1)
        player.cards.append(crd1)
        player.cards.append(crd2)
        
        self.assertEqual(3, player.getTotalPoints())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetPoints']
    unittest.main()