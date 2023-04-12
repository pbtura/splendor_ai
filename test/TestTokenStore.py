'''
Created on Apr 11, 2023

@author: bucpa
'''
import unittest
from TokenStore import TokenStore 
from Color import Color 

class Test(unittest.TestCase):

    store:TokenStore
    
    def setUp(self):
        self.store = TokenStore(7,6,5,4,3,2)
        pass


    def tearDown(self):
        pass


    def testAddGreen(self):
        #(white, blue, green, red, black, gold)
        expected = TokenStore(7,6,7,4,3,2)
        self.store.updateTokens({ Color.GREEN: 2})
        unittest.TestCase.assertDictEqual(self, expected.tokens, self.store.tokens)
        pass

    def testRemoveGreen(self):
        #(white, blue, green, red, black, gold)

        expected = TokenStore(7,6,2,4,3,2)
        self.store.updateTokens({ Color.GREEN: -3})
        unittest.TestCase.assertDictEqual(self, expected.tokens, self.store.tokens)
        pass
    
    def testAddBlueAndGreen(self):
        #(white, blue, green, red, black, gold)
        expected = TokenStore(7,10,8,4,3,2)
        self.store.updateTokens({ Color.BLUE: 4, Color.GREEN: 3})
        unittest.TestCase.assertDictEqual(self, expected.tokens, self.store.tokens)
        pass
    
    def testRemoveTooMany(self):
        
        unittest.TestCase.assertRaises(self, ValueError, self.store.updateTokens, { Color.GREEN: -6})
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAddGreen']
    unittest.main()