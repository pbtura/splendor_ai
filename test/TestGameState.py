'''
Created on Apr 12, 2023

@author: bucpa
'''
import unittest
from _collections_abc import Iterable
from ResourceCard import ResourceCard
from GameState import GameState
from Color import Color
from Cost import Cost


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testParseResourceRow(self):
       
        rowData: Iterable = {1,"BLUE",0,"2g+2k",0,0,2,0,2}
        #(white, blue, green, red, black)
        expectedCost:Cost = Cost( 0,0,2,0,2)
        expectedCard:ResourceCard = ResourceCard( 1, Color["BLUE"], expectedCost, 0)
        actualCard:ResourceCard = GameState.parseResourceRow(rowData)
        self.assertIsNotNone(actualCard)
        self.assertEqual(expectedCard, actualCard);
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testParseResourceRow']
    unittest.main()