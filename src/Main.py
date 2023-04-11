'''
Created on Apr 11, 2023

@author: bucpa
'''
from GemCost import GemCost
from ResourceCard import ResourceCard
from Color import Color

if __name__ == "__main__":
    foo = GemCost(0,1,2,3,4)
    card = ResourceCard(1, Color.RED, foo, 2)
   
    print ("Hello, world!")
    print(card)