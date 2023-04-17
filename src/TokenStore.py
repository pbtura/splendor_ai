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
    
    def depositTokens(self, tokens:Dict[str, int])-> bool:
        for x,y in tokens.items():
            self.tokens[x] += y
    
        return 1   
    
    def withdrawTokens(self, tokens:Dict[str, int])-> bool:
        for x,y in tokens.items():              
            if( self.validateWithdraw(self.tokens[x], y, x) ):
                self.tokens[x] -= y
            else:
                return 0
    
        return 1               
        
    def validateWithdrawPair(self, color: Color)-> bool:
        if(self.tokens.get(color) < 4):
            raise RuntimeError("Cannot withdraw two matched gems when less than four remain.")
            return 0
        else:
            return 1
        
    def validateWithdraw(self, old, new, color: Color)->bool:

        if(new >= 2):
            self.validateWithdrawPair(color)
        if(old - new < 0):
            raise RuntimeError("Cannot remove more gems than are in the store.") 
            return 0
        else:
            return 1
        
    def __str__(self)->str:
        return f"{self.tokens}"