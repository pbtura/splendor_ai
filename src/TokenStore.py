'''
Created on Apr 11, 2023

@author: bucpa
'''
from typing import Dict
from Color import Color
class TokenStore(object):
    '''
    classdocs
    '''

    tokens:Dict[str, int]
    
    def __init__(self, white: int, blue: int, green: int, red: int, black: int, gold: int):
        '''
        Constructor
        '''
        self.tokens = {Color.BLUE: blue, Color.BLACK: black, Color.WHITE: white, Color.RED: red, Color.GREEN: green, Color.GOLD: gold}
    
    def updateTokens(self, tokens:Dict[str, int])-> bool:
        for x,y in tokens.items():
            if ( self.validate(self.tokens[x], y) ):
                self.tokens[x] += y
            else:
                return 0
    
        return 1                
        
    def validate(self, old, new)->bool:

        if(old + new < 0):
            raise ValueError("Cannot remove more gems than are in the store") 
            return 0
        else:
            return 1
        
    def __str__(self)->str:
        return f"{self.tokens}"