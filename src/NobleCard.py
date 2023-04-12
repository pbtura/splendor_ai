'''
Created on Apr 11, 2023

@author: bucpa
'''
from CardCost import CardCost

class NobleCard(object):
    '''
    classdocs
    '''
    
    def __init__(self, cost: CardCost, points: int):
        '''
        Constructor
        '''
        self.cost = cost
        self.points = points
        
    def __str__(self)->str:
        return f"cost:{self.cost}, points:{self.points}"
        