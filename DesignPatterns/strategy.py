'''
https://medium.com/@sheikhsajid/design-patterns-in-python-part-1-the-strategy-pattern-54b24897233e
'''
from abc import ABC, abstractmethod

class QuackStratergy(ABC):
    @abstractmethod
    def quack(self):
        """ Required method """
class LoudQuackStratergy(QuackStratergy):
    def quack(self):
        print("QUACK QUACK Louder!!!")
class GentleQuackStratergy(QuackStratergy):
    def quack(self):
        print("quack gentle!!!")

class LightStratergy(ABC):
    @abstractmethod
    def lights_on(self):
        """ hmm implement it bro"""

class OnForTenSecondStratergy(LightStratergy):
    def lights_on(self):
        print("Lights on for 10 seconds")