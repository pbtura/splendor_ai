'''
Created on Apr 14, 2023

@author: bucpa
'''
from _collections_abc import Iterable
from GameState import GameState

class GameActions(object):
    '''
    classdocs
    '''
    
    game:GameState

    def __init__(self, names: Iterable[str], randomize: bool = 1):
        '''
        Constructor
        '''
        game = GameState()
        