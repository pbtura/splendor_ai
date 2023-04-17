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
from GameActions import GameActions

if __name__ == "__main__":
    game:GameActions = GameActions(["player1", "player2", "player3", "player4"], 1)
    game.takeTurn()

