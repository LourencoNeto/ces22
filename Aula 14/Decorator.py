# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 00:58:22 2018

@author: Lourenço Neto
"""

import abc

class Habitation(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def assemble(self):
        pass


class SimpleHouse(Habitation):
    def assemble(self):
        print("Just a simple House: 1 bedroom, a small living room, tiny kitchen and the bathroom.")


class HouseDecorator(Habitation):
    def __init__(self, house):
        self.house = house

    def assemble(self):
        self.house.assemble()


class Mansion(HouseDecorator):
    def __init__(self, house):
        super(Mansion, self).__init__(house)

    def assemble(self):
        super(Mansion, self).assemble()
        print("Transforming the Simple House into a Mansion.")


class Duplex(HouseDecorator):
    def __init__(self, house):
        super(Duplex, self).__init__(house)

    def assemble(self):
        super(Duplex, self).assemble()
        print("Now the Simple House has 2 floors.")


if __name__ == '__main__':
    mansion = Mansion(SimpleHouse())
    mansion.assemble()
    print("-----")

    duplex_mansion = Mansion(Duplex(SimpleHouse()))
    duplex_mansion.assemble()