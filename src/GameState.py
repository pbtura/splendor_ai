'''
Created on Apr 11, 2023

@author: bucpa
'''
import os
import csv
import Player
from _collections_abc import Iterable
from TokenStore import TokenStore
from NobleCard import NobleCard
from ResourceCard import ResourceCard
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
        self.resourceDeck1 = [];
        self.resourceDeck2 = [];
        self.resourceDeck3 = [];
    
    @staticmethod
    def parseResourceRow(row: Iterable)->ResourceCard:                
        card = ResourceCard;
        return None;
    
    def importDeck(self):       
        with open(os.path.join('..','resources','cards_list.csv'), newline='') as f:
            reader = csv.reader(f)
            currentDeck:Iterable[ResourceCard]
            for row in reader:
                print(row)
                match(row[0]):
                    case '1':
                        currentDeck = self.resourceDeck1
                    case '2':
                        currentDeck = self.resourceDeck2
                    case '3':
                        currentDeck = self.resourceDeck3
                    case _:
                        #do nothing
                        print('')
                
    
                    
        