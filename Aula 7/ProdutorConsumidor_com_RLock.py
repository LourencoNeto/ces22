# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:59:53 2018

@author: Lourenço Neto
"""

import threading
import time
import random

class Itens(object):
    lock = threading.RLock()
    def __init__(self):
        self.list_itens = []
        #self.item = 0
    def execute(self, flag, item = None):
        Itens.lock.acquire()
        
        if flag == 1:
            self.list_itens.append(item)
        elif flag == -1:
           self.list_itens.pop()
        
        """
        if flag == 1:
            self.item += item
        elif flag == -1:
            item = self.item
            self.item -= self.item
            return item
        """
            
        Itens.lock.release()
    def add(self, flag, item):
        Itens.lock.acquire()
        self.execute(1, item)
        Itens.lock.release()
    def remove(self, flag):
        Itens.lock.acquire()
        self.execute(-1)
        Itens.lock.release()
        
        
def producer(itens):
    for i in range(100):
        time.sleep(2)
        item = random.randint(0, 256)
        itens.add(1, item)
        print("Producer notify : item Nº %d appended to list" %item)
    
def consumer(itens): 
    while True:
        time.sleep(3)
        itens.remove(-1)
        print("Consumer notify : an item popped from list" )

itens = Itens()
t1 = threading.Thread(target=producer, args = (itens, ))
t2 = threading.Thread(target=consumer, args = (itens, ))
t1.start()
t2.start()
t1.join()
t2.join()
print("The number of remainingg itens in the box is %d" %len(itens.list_itens))    