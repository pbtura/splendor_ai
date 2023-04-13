'''
Created on Apr 11, 2023

@author: bucpa
'''
import os
import csv

from Cost import Cost
from _collections_abc import Iterable
from TokenStore import TokenStore
from NobleCard import NobleCard
from ResourceCard import ResourceCard
from Color import Color
from Player import Player

class GameState(object):
    '''
    classdocs
    '''


    players: Iterable[Player]
    availableGems:TokenStore
    availableNobles:Iterable[NobleCard]
    noblesDeck:Iterable[NobleCard]
    
    availableResources:dict[ResourceCard]
    resourceDeck:dict[ResourceCard]

    
    def __init__(self, numberOfPlayers: int, currentRound: int=0):
        '''
        Constructor
        '''
    def initializeResourceDecks(self):  
        
        self.resourceDeck = {}
        with open(os.path.join('..','resources','cards_list.csv'), newline='') as f:
            reader = csv.DictReader(f)
            self.resourceDeck = GameState.importResourceDecks(reader)
    
    def initializeNobleDeck(self):
        self.noblesDeck = []
        with open(os.path.join('..','resources','nobles_list.csv'), newline='') as f:
            reader = csv.DictReader(f)
            self.noblesDeck = GameState.importNobleDeck(reader)
    
    @staticmethod        
    def initializeAvailableGems( numberOfPlayers: int)->TokenStore:
        match numberOfPlayers:
            case 4:
                 availableGems = TokenStore(7,7,7,7,7,5)
            case 3:
                 availableGems = TokenStore(5,5,5,5,5,5)
            case 2:
                 availableGems = TokenStore(4,4,4,4,4,5)
            case _:
                availableGems = None
       
        return availableGems
    
    @staticmethod
    def parseResourceRow(rowData: Iterable)->ResourceCard:
        row = dict(rowData)
        colorName: str = row['Gem color']
        color: Color = Color[colorName] 
        cost: Cost = Cost(row['white'], row['blue'], row['green'], row['red'], row['black'])              
        card = ResourceCard(row['Level'], color, cost, row['PV'])
        
        return card;

    @staticmethod
    def importResourceDecks(reader) -> dict:       
        decks: dict = {1: [], 2: [], 3: []}


        for row in reader:
            #print(row)               
            level: int = int(row['Level']);

            cardList: list = decks.get(level)
            card: ResourceCard = GameState.parseResourceRow(row)
            cardList.append(card)
                
        return decks
    
    @staticmethod
    def parseNobleRow(rowData: Iterable)->NobleCard:
        row = dict(rowData)
        cost: Cost = Cost(row['white'], row['blue'], row['green'], row['red'], row['black'])              
        card = NobleCard( cost, row['PV'])
        
        return card;
    
    @staticmethod
    def importNobleDeck(reader) -> Iterable[NobleCard]:
        nobles = []
        for row in reader:
            card: NobleCard = GameState.parseNobleRow(row)
            nobles.append(card)
        return nobles
                    
    def addPlayers(self, names:list[str]):
        self.players = []
        for name in names:
            player:Player = Player(name)
            self.players.append(player)
                    
        