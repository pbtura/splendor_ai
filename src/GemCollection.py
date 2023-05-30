'''
Created on Apr 18, 2023

@author: bucpa
'''
from abc import abstractmethod, ABC

class GemCollection(ABC):

    @abstractmethod
    def getValues(self)->list:
        pass
        