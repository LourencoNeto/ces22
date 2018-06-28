# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:14:49 2018

@author: Lourenço Neto
"""

from abc import ABC, abstractmethod

#Sample to treat A/B Test

# Abstract Interface used by the client
class Website(ABC):

    def __init__(self, implementation):
        # encapsulate an instance of a concrete implementation class
        self._implementation = implementation

    def __str__(self):
        return 'Interface: {}; Implementation: {}'.format(
            self.__class__.__name__, self._implementation.__class__.__name__)

    @abstractmethod
    def show_page(self):
        pass

# Concrete Interface 1
class FreeWebsite(Website):

    def show_page(self):
        ads = self._implementation.get_ads()
        text = self._implementation.get_excerpt()
        call_to_action = self._implementation.get_call_to_action()
        print(ads)
        print(text)
        print(call_to_action)
        print('')
    
# Concrete Interface 2
class PaidWebsite(Website):

    def show_page(self):
        text = self._implementation.get_article()
        print(text)
        print('')
        
# Abstract Implementation that will change the interface depending of the implementation
class Implementation(ABC):

    def get_excerpt(self):
        return 'excerpt from the article'

    def get_article(self):
        return 'full article'

    def get_ads(self):
        return 'some ads'

    @abstractmethod
    def get_call_to_action(self):
        pass
    
# Concrete Implementation 1
class ImplementationA(Implementation):

    def get_call_to_action(self):
        return 'To remove the adds, you have to pay 2 dollars'
    
# Concrete Implementation 2
class ImplementationB(Implementation):

    def get_call_to_action(self):
        return 'You can remove half of the adds for free. Choose'

# Client
def main():
    a_free = FreeWebsite(ImplementationA())
    print(a_free)
    a_free.show_page()

    b_free = FreeWebsite(ImplementationB())
    print(b_free)
    b_free.show_page()

    a_paid = PaidWebsite(ImplementationA())
    print(a_paid)
    a_paid.show_page()

    b_paid = PaidWebsite(ImplementationB())
    print(b_paid)
    b_paid.show_page()

if __name__ == '__main__':
    main()

