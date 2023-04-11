'''
Created on Apr 11, 2023

@author: bucpa
'''
from CardCost import CardCost

class NobleCard(object):
    '''
    classdocs
    '''

    POINTS: int = 3
    
    def __init__(self, cost: CardCost):
        '''
        Constructor
        '''
        self.cost = cost
        
    def __str__(self)->str:
        return f"cost:{self.cost}, points:{NobleCard.POINTS}"
        