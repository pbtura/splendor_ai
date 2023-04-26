'''
Created on Apr 14, 2023

@author: bucpa
'''
import numpy as np
from pynput.keyboard import Listener 

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
    listener:Listener
    listening: bool = 0
   
    def __init__(self, names: Iterable[str], randomize: bool = 1):
        '''
        Constructor
        '''
        self.game = GameState()
        self.game.setupGame(names)
        self.game.startNewGame(randomize)
        self.players = cycle(self.game.players)
        
        # self.listener = Listener(
        #     on_press = self.on_press
        # )
        
    def getPlayersList(self)->list:
        return self.game.players
    
    def promptUser(self):
        print("Choose an action: 1)list available cards, 2)take gems, 3)buy card, 4)reserve card 5)list affordable cards q)end turn 0)cancel  ")
        self.listener.start()
        self.listener.join()
        

    def on_press(self,key):
        print("Key pressed: {0}".format(key))
        if hasattr(key, 'char'):  # Write the character pressed if available
             
            match key.char:
                case '1':
                    print(f"pressed {key.char}")
                    self.listAvailableResources()
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    pass
                case '5':
                    cards = self.findAffordableCards()
                    print(cards)
                case 'q':
                    self.takeTurn()
                case _:
                    pass

    def takeTurn(self):
        if not(self.listening):
            self.listening = 1
            self.promptUser()
        self.currentPlayer = next(self.players)
        print(f"player {self.currentPlayer.name}, it is your turn")
    
    def findAffordableCards(self)->list:  
        gems = self.currentPlayer.gems
        resources = self.game.availableResources
        discounts = list( self.currentPlayer.getResourceTotals().values() )
        result = self.game.findAvailableResources(gems, resources, discounts)
        
        return result  
    
    def listAvailableResources(self):
        print(f"LV 1: {self.game.availableResources.get(1)[0]} | {self.game.availableResources.get(1)[1] } | {self.game.availableResources.get(1)[2]} | {self.game.availableResources.get(1)[3]}" )
        print(f"LV 2: {self.game.availableResources.get(2)[0]} | {self.game.availableResources.get(2)[1] } | {self.game.availableResources.get(2)[2]} | {self.game.availableResources.get(2)[3]}" )
        print(f"LV 3: {self.game.availableResources.get(3)[0]} | {self.game.availableResources.get(3)[1] } | {self.game.availableResources.get(3)[2]} | {self.game.availableResources.get(3)[3]}" )
        
    def listAvailableNobles(self):
        for x, y in enumerate(self.game.availableNobles):
            print(f"Noble {x}: {y}")


    
