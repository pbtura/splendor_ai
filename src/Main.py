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

if __name__ == "__main__":
    foo = GemCost(0,1,2,3,4)
    nb = CardCost(4,3,2,1,0)
    card = ResourceCard(1, Color.RED, foo, 2)
    noble = NobleCard(nb)
    store = TokenStore(7,6,5,4,3,2)
   
    print ("Hello, world!")
    print("resource card is", card)
    print("noble card is", noble)
    print("token store is", store)