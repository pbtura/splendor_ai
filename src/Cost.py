'''
Created on Apr 11, 2023

@author: bucpa
'''
import numpy as np
from GemCollection import GemCollection
class Cost(GemCollection):
    '''
    classdocs
    '''

    def __init__(self, white: int, blue: int, green: int, red: int, black: int):
            '''
            Constructor
            '''
            self.blue = blue
            self.black = black
            self.white = white
            self.red = red
            self.green = green
            
    def getValues(self)->np.ndarray:
        return np.array([self.white, self.blue, self.green, self.red, self.black])
    
    def __eq__(self, other):
        return self.white == other.white and self.blue == other.blue and self.green == other.green and self.red == other.red and self.black == other.black
        
    def __str__(self)->str:
        return f"W:{self.white}, U:{self.blue}, G:{self.green}, R:{self.red}, B:{self.black}"