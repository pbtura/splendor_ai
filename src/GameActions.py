'''
Created on Apr 14, 2023

@author: bucpa
'''

from itertools import cycle
from GameState import GameState
from Player import Player
from typing import Iterable

class GameActions(object):
    '''
    classdocs
    '''
    
    game:GameState
    players:cycle
    currentPlayer:Player

    def __init__(self, names: Iterable[str], randomize: bool = 1):
        '''
        Constructor
        '''
        self.game = GameState()
        self.game.setupGame(names)
        self.game.startNewGame(randomize)
        self.players = cycle(self.game.players)
        
    def promptUser(self):
        action: str = input("Choose an action: 1)list available cards, 2)take gems, 3)buy card, 4)reserve card  ")
        print(action)

    def takeTurn(self):
        self.currentPlayer = next(self.players)
        self.promptUser()
        # print(currentPlayer)
        
    
    def listAvailableResources(self):
        print(f"LV 1: {self.game.availableResources.get(1)[0]} | {self.game.availableResources.get(1)[1] } | {self.game.availableResources.get(1)[2]} | {self.game.availableResources.get(1)[3]}" )
        print(f"LV 2: {self.game.availableResources.get(2)[0]} | {self.game.availableResources.get(2)[1] } | {self.game.availableResources.get(2)[2]} | {self.game.availableResources.get(2)[3]}" )
        print(f"LV 3: {self.game.availableResources.get(3)[0]} | {self.game.availableResources.get(3)[1] } | {self.game.availableResources.get(3)[2]} | {self.game.availableResources.get(3)[3]}" )
