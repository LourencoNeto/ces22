# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 21:40:00 2018

@author: Lourenço Neto
"""

# States of a reversible counter until 4 

class RevCounterState(object):
    """ Abstract base class of state of a reversible counter from 0 to 4 """
    
    name = "state"
    allowed = []
    
    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current:',self,' => switched to new state',state.name)         
            self.__class__ = state
        else:
            print('Current:',self,' => switching to',state.name,'not possible.')

    def __str__(self):
        return self.name
    
class Zero(RevCounterState):
    """ State of count zero """

    name = "counter 0"
    allowed = ['counter 1', 'counter 4']

class One(RevCounterState):
    """ State of count one """

    name = "counter 1"
    allowed = ['counter 2', 'counter 0']

class Two(RevCounterState):
    """ State of count two """

    name = "counter 2"
    allowed = ['counter 3', 'counter 1']

class Three(RevCounterState):
    """ State of count three """

    name = "counter 3"
    allowed = ['counter 4', 'counter 2']
    
class Four(RevCounterState):
    """ State of count four """

    name = "counter 4"
    allowed = ['counter 0', 'counter 3']

class RevCounter(object):
    """ A class representing a computer """

    def __init__(self, model='HP'):
        self.model = model
        # State of the computer - default is off.
        self.state = Zero()

    def change(self, state):
        """ Change state """

        self.state.switch(state)

if __name__ == "__main__":
    counter = RevCounter()
    # Sum one
    counter.change(One)
    # Get back to the previous state
    counter.change(Zero)
    # Sum one again
    counter.change(One)
    # Advance to the next state
    counter.change(Two)
    # Advance to the next state
    counter.change(Three)
    # Get back to the previous state
    counter.change(Two)
    # Advance to the next state
    counter.change(Three)
    # Advance to the final state
    counter.change(Four)