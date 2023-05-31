'''
Created on Apr 11, 2023

@author: bucpa
'''
import numpy as np
from collections import OrderedDict
from Color import Color
from GemCollection import GemCollection


class TokenStore(GemCollection):
    '''
    classdocs
    '''

    tokens: OrderedDict[Color, int]
    
    def __init__(self, white: int, blue: int, green: int, red: int, black: int, gold: int):
        '''
        Constructor
        '''
        self.tokens = OrderedDict({Color.WHITE: white, Color.BLUE: blue, Color.GREEN: green, Color.RED: red, Color.BLACK: black, Color.GOLD: gold})
    
    def getValues(self) -> np.ndarray:
        return np.array(list(self.tokens.values()))
    
    def depositTokens(self, tokens: OrderedDict[Color, int]) -> bool:
        for x, y in tokens.items():
            self.tokens[x] += y
    
        return True
    
    def withdrawTokens(self, tokens: OrderedDict[Color, int]) -> bool:
        for x, y in tokens.items():
            if self.validateWithdraw(self.tokens[x], y, x):
                self.tokens[x] -= y
            else:
                return False
    
        return True
        
    def validateWithdrawPair(self, color: Color) -> bool:
        if self.tokens.get(color) < 4:
            raise RuntimeError("Cannot withdraw two matched gems when less than four remain.")
        else:
            return True
        
    def validateWithdraw(self, old, new, color: Color) -> bool:

        if new >= 2:
            self.validateWithdrawPair(color)
        if old - new < 0:
            raise RuntimeError("Cannot remove more gems than are in the store.") 
        else:
            return True
        
    def __str__(self) -> str:
        return f"{self.tokens}"
