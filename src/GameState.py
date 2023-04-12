'''
Created on Apr 11, 2023

@author: bucpa
'''
import os
import csv
import Player

from Cost import Cost
from _collections_abc import Iterable
from TokenStore import TokenStore
from NobleCard import NobleCard
from ResourceCard import ResourceCard
from Color import Color
class GameState(object):
    '''
    classdocs
    '''


    players: Iterable[Player]
    availableGems:TokenStore
    availableNobles:Iterable[NobleCard]
    
    availableResources1:Iterable[ResourceCard]
    resourceDeck1:Iterable[ResourceCard]
    
    availableResources2:Iterable[ResourceCard]
    resourceDeck2:Iterable[ResourceCard]
    
    availableResources3:Iterable[ResourceCard]
    resourceDeck3:Iterable[ResourceCard]
    
    def __init__(self, numberOfPlayers: int, currentRound: int=0):
        '''
        Constructor
        '''
    def initializeResourceDecks(self):  
        
        with open(os.path.join('..','resources','cards_list.csv'), newline='') as f:
            reader = csv.DictReader(f)
    
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
            #make sure we filter out and headers or other unwanted lines               
            level: int = int(row['Level']);

            cardList: list = decks.get(level)
            card: ResourceCard = GameState.parseResourceRow(row)
            cardList.append(card)
                
        return decks
                
    
                    
        