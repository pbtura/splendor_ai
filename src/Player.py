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
    cards: Iterable[ResourceCard]
    reservedCards: Iterable[ResourceCard]
    nobles: Iterable[NobleCard]
    
    def __init__(self, turnOrder: int, turnsTaken: int=0 ):
        '''
        Constructor
        '''
        self.turnOrder = turnOrder;
        self.turnsTaken = turnsTaken;
        self.gems = TokenStore(0,0,0,0,0,0)
        self.cards = []
        self.reservedCards = []
        self.nobles = []
        
    def __str__(self)->str:
        return f"turn order:{self.turnOrder}, turns taken:{self.turnsTaken}, gems:{self.gems}, resources:{self.cards}, reserved cards:{self.reservedCards}, nobles:{self.nobles}"
        