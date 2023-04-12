'''
Created on Apr 11, 2023

@author: bucpa
'''
from GemCost import GemCost
from ResourceCard import ResourceCard
from Color import Color
from CardCost import CardCost
from NobleCard import NobleCard
from TokenStore import TokenStore
from Player import Player
from GameState import GameState

if __name__ == "__main__":
    foo = GemCost(0,1,2,3,4)
    nb = CardCost(4,3,2,1,0)
    card = ResourceCard(1, Color.RED, foo, 2)
    noble = NobleCard(nb)
    store = TokenStore(7,6,5,4,3,2)
    player1 = Player(1, 4)
   
    print ("Hello, world!")
    print("resource card is", card)
    print("noble card is", noble)
    print("original token store is", store)

    
    '''update the token store'''
    result = store.updateTokens({Color.BLACK: 3, Color.RED: 1, Color.GREEN: 2})
    if(result):
        print("updated token store is", store)
    else:
        print("token update failed")
    
    print("player is", player1)
    '''update the player data'''
    
    '''initialize a game'''
    game = GameState(2)
    game.importDeck()