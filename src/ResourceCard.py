'''
Created on Apr 11, 2023

@author: bucpa
'''
import numpy as np
import pynput
from Color import Color
from Cost import Cost

class ResourceCard(object):
    '''
    classdocs
    '''

    def __init__(self, level: int, suit: Color, cost: Cost, points: int):
        '''
        Constructor
        '''
        self.level = int(level)
        self.suit = suit
        self.cost = cost
        self.points = int(points)
        self.id = str(level) + "" + suit.name + "" + np.array2string( cost.getValues(), None, None, None, '' )
        
    def __eq__(self, other):
        return self.level == other.level and self.suit == other.suit and self.cost == other.cost and self.points == other.points
            
    def __str__(self)->str:
        return f"level {self.level}, color:{self.suit.name}, cost:{self.cost}, points:{self.points}"
    
    def __repr__(self)->str:
        return f"level {self.level}, color:{self.suit.name}, cost:{self.cost}, points:{self.points}"