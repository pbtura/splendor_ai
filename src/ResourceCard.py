'''
Created on Apr 11, 2023

@author: bucpa
'''
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
    
    def __str__(self)->str:
        return f"level {self.level}, color:{self.suit.name}, cost:{self.cost}, points:{self.points}"