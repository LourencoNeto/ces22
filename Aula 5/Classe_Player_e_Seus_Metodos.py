# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 01:15:38 2018

@author: Lourenço Neto
"""

import abc

class Player(object):
    __metaclass__ = abc.ABCMeta
      
    @abc.abstractmethod    
    def change_stamina(self): #Almost every player get tired at the end of the game and need time to get better. So, it's important to have this function implemented
        """Method that vary the stamina of the player according to its tiredness"""
    
    @abc.abstractmethod
    def training(self): #every player has a training to follow
        """Method to specify the training of the player"""
    
class Defender(Player):
    
    def __init__(self):
        self.stamina = 100
    
    def get_stamina(self):
        return self.stamina
    
    def change_stamina(self, tiredness): #Here, the defender get tired because of the running and, specially, the marking. So, the level of the tiredness it is important
        if(tiredness == "High"):
            self.stamina = self.stamina - 20
        elif(tiredness == "Low"):
            self.stamina = self.stamina + 20
            
    @staticmethod
    def basic_training(): #It's a method that tell the basic training of every defender
        return "Running, passing and marking"
    
    @classmethod
    def advanced_training(cls): #This method calls the static method to its execution. So, it should be a classmethod
        basic_training = cls.basic_training()
        return basic_training + ". After that, positioning and tackling"

class GoalKeeper(Player): 
    def __init__(self):
        self.stamina = 100
    
    def get_stamina(self):
        return self.stamina
    
    @staticmethod
    def change_stamina(): #Here, the goalkeeper, unless it get hurts at the game, pratically won't be tired to the next game. So, specifically to this class, the stamina's variation is almost zero
            return None
        
    @staticmethod
    def basic_training(): #It's a method that tell the basic training of every goalkeeper
        return "Goal handling and positioning"
    
    @classmethod
    def advanced_training(cls): #This method calls the static method to its execution. So, it should be a classmethod
        basic_training = cls.basic_training()
        return basic_training + ". After that, running and practicing reflexes"
    
print(GoalKeeper.advanced_training())
print(Defender.advanced_training())

Cech = GoalKeeper()
print(Cech.get_stamina())

check = GoalKeeper.change_stamina()
if check == None:
    print("GoalKeepers almost don't move in the game. Why would the get tired?")

Kompany = Defender()
print(Kompany.get_stamina())
Kompany.change_stamina("High")
print(Kompany.get_stamina())