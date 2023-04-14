'''
Created on Apr 11, 2023

@author: bucpa
'''
import os
import csv
import random
from collections import deque

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
    noblesDeck:deque[NobleCard]
    
    availableResources:dict[int,list[ResourceCard]]
    resourceDeck:dict[int, deque[ResourceCard]]
    
    playersRandomized:bool = 0
    resourcesShuffled:bool = 0
    noblesShuffled:bool = 0
    
    def __init__(self):
        '''
        Constructor
        '''
        self.availableResources = {1: [], 2: [], 3: []}
        self.noblesDeck = deque()
    
    def setupGame(self, names:list[str]):
        #initialize players
        self.addPlayers(names) 
        #initialize resource deck
        self.initializeResourceDecks()
        #initialize noble deck
        self.initializeNobleDeck()
        #initialize token bank
        self.initializeAvailableGems()
           
    
    def startNewGame(self, randomize:bool = 1):   
        
        #this is primarily for testing purposes. During normal usage,
        #randomize should always be true
        if(randomize):
            #randomize turn order
            random.shuffle(self.players)
            self.playersRandomized = 1          
        
            #randomize resource deck
            for y in self.resourceDeck.values(): 
                random.shuffle(y)
            self.resourcesShuffled = 1
            
            #randomize noble deck
            random.shuffle(self.noblesDeck)
            self.noblesShuffled = 1
        else:
            self.playersRandomized = 0
            self.resourcesShuffled = 0
            self.noblesShuffled = 0
        
        #deal resource cards          
        self.initializeAvailableResourceCards()
        
        #deal noble cards 
        self.dealNobleCards(len(self.players))       
        
    def addPlayers(self, names:list[str]):
        self.players = []
        for name in names:
            player:Player = Player(name)
            self.players.append(player)
                
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
    
    def dealResourceCards(self, level: int, numberOfCards: int):
        available:list = self.availableResources.get(level)

        i: int = 0;
        cards: deque = self.resourceDeck.get(level)
        while i < numberOfCards and len(cards) > 0 :          
            available.append( cards.popleft())
            i+=1
    
    def dealNobleCards(self, numberOfPlayers: int):
        self.availableNobles = []
        
        i: int = 0;
        cards: deque = self.noblesDeck
        while i < numberOfPlayers + 1 and len(cards) > 0 :          
            self.availableNobles.append( cards.popleft())
            i+=1
        
    def initializeAvailableResourceCards(self):
                
        self.dealResourceCards(1, 4)
        self.dealResourceCards(2, 4)
        self.dealResourceCards(3, 4)
        
          
    def initializeAvailableGems(self):
        numberOfPlayers: int = len(self.players)
        match numberOfPlayers:
            case 4:
                self.availableGems = TokenStore(7,7,7,7,7,5)
            case 3:
                self.availableGems = TokenStore(5,5,5,5,5,5)
            case 2:
                self.availableGems = TokenStore(4,4,4,4,4,5)
            case _:
                self.availableGems = None
       
    
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
        decks: dict = {1: deque(), 2: deque(), 3: deque()}


        for row in reader:
            #print(row)               
            level: int = int(row['Level']);

            cardList: deque = decks.get(level)
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
        nobles: deque = deque()
        for row in reader:
            card: NobleCard = GameState.parseNobleRow(row)
            nobles.append(card)
        return nobles
    
    def withdrawGems(self, player:Player, gems: dict):
        
        if(len(gems) > 3):
            raise RuntimeError("No more than three gems may be withdrawn from the bank.")

        self.availableGems.withdrawTokens(gems);
        player.gems.updateTokens(gems)       
    
    def purchaseCard(self, player:Player, deck: int, card: int):     
        print("purchasing card") 
        
    def reserveCard(self, player:Player, deck: int, card: int):    
        print("reserving card")  
        
    def claimNoble(self, player:Player, card: int):
        print("claiming noble")
                    
        