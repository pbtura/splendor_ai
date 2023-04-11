'''
Created on Apr 11, 2023

@author: pbuchheit
'''

class GemCost:
    '''
    classdocs
    '''


    def __init__(self, blue: int, black: int, white: int, red: int, green: int):
        '''
        Constructor
        '''
        self.blue = blue
        self.black = black
        self.white = white
        self.red = red
        self.green = green
        
    def __str__(self)->str:
        return f"Cost is U:{self.blue}, B:{self.black}, W:{self.white}, R:{self.red}, G:{self.green}"

        
        