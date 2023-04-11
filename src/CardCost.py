'''
Created on Apr 11, 2023

@author: pbuchheit
'''
from Cost import Cost
class CardCost(Cost):
    '''
    classdocs
    '''


    def __init__(self, blue: int, black: int, white: int, red: int, green: int):
        '''
        Constructor
        '''
        Cost.__init__(self, blue, black, white, red, green)
        

        
        