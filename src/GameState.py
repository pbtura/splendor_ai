'''
Created on Apr 11, 2023

@author: bucpa
'''
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
    
    def __init__(self, currentRound: int=0):
        '''
        Constructor
        '''
        