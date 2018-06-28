# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 21:31:44 2018

@author: Lourenço Neto
"""


class Controlador_De_Voo:
    """
    Implement cooperative behavior by coordinating Aviao objects.
    Like this, the Controlador_De_Voo will inform the other airplanes the possibles paths to be chosen by the airplane to land in the airport.
    """

    def __init__(self):
        self._aviao_1 = Aviao1(self)
        self._aviao_2 = Aviao2(self)
    
    def print_controled_airplanes(self):
        return self._aviao_1, self._aviao_2

class Aviao1:
    """
    Know its mediator object (In this case, the Controlador_De_Voo).
    Communicate with its mediator whenever it would have otherwise
    communicated with another airplane.
    """

    def __init__(self, mediator):
        self._mediator = mediator
        
    def get_mediator(self):
        return self._mediator

class Aviao2:
    """
    Know its mediator object (In this case, the Controlador_De_Voo).
    Communicate with its mediator whenever it would have otherwise
    communicated with another airplane.
    """

    def __init__(self, mediator):
        self._mediator = mediator
        
    def get_mediator(self):
        return self._mediator

def main():
    mediator = Controlador_De_Voo()
    print(mediator.print_controled_airplanes()) #Likethis, you can see the airplanes that this object is mediator


if __name__ == "__main__":
    main()