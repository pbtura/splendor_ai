'''
Created on Apr 14, 2023

@author: bucpa
'''

from itertools import cycle
from _collections_abc import Iterable
from GameState import GameState

class GameActions(object):
    '''
    classdocs
    '''
    
    game:GameState
    players:cycle

    def __init__(self, names: Iterable[str], randomize: bool = 1):
        '''
        Constructor
        '''
        self.game = GameState()
        self.game.setupGame(names)
        self.game.startNewGame(randomize)
        self.players = cycle(self.game.players)

        