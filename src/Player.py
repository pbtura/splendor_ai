'''
Created on Apr 11, 2023

@author: bucpa
'''
from TokenStore import TokenStore
from _collections_abc import Iterable
from ResourceCard import ResourceCard
from NobleCard import NobleCard

class Player(object):
    '''
    classdocs
    '''

    gems: TokenStore
    cards: list[ResourceCard]
    reservedCards: Iterable[ResourceCard]
    nobles: Iterable[NobleCard]
    
    def __init__(self, playerName: str ):
        '''
        Constructor
        '''
        self.turnsTaken = 0;
        self.name = playerName;
        self.gems = TokenStore(0,0,0,0,0,0)
        self.cards = []
        self.reservedCards = []
        self.nobles = []
        
    def __str__(self)->str:
        return f"turns taken:{self.turnsTaken}, gems:{self.gems}, resources:{self.cards}, reserved cards:{self.reservedCards}, nobles:{self.nobles}"
        