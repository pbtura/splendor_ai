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
        expected = TokenStore(7,6,5,4,5,2)
        self.store.updateTokens({ Color.GREEN: 2})
        unittest.TestCase.assertDictEqual(self, expected.tokens, self.store.tokens)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAddGreen']
    unittest.main()