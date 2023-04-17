'''
Created on Apr 11, 2023

@author: bucpa
'''
from TokenStore import TokenStore
from ResourceCard import ResourceCard
from NobleCard import NobleCard
from Color import Color
from typing import Iterable

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
        
    def getResourceTotals(self) -> dict[Color: int]:
        card: ResourceCard
        totals: dict[Color: int]={Color.WHITE: 0, Color.BLUE: 0, Color.GREEN: 0, Color.RED: 0, Color.BLACK: 0}
        for card in self.cards:
            t = totals.get(card.suit) + 1
            totals[card.suit] = t
            
        return totals
        
    def __str__(self)->str:
        return f"name:{self.name}, turns taken:{self.turnsTaken}, gems:{self.gems}, resources:{self.cards}, reserved cards:{self.reservedCards}, nobles:{self.nobles}"
        