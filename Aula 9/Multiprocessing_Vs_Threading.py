# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:34:31 2018

@author: Lourenço Neto
"""

import random
from threading import Thread
from multiprocessing import Process
import time


size = 10000000   # Number of random numbers to add to list
threads = 2 # We can only create 2 threads at the same time (because of GLI)
my_list = []
for i in range(threads):
    my_list.append([])
def func(count, mylist):
    for i in range(count):
        mylist.append(random.random())
def multithreaded():
    jobs = []
    for i in range(threads):
        thread = Thread(target=func,args=(size,my_list[i]))
        jobs.append(thread)
    for j in jobs:
        j.start() 
    for j in jobs:
        j.join()

def multiprocessed():
    processes = []
    for i in range(threads):
        p = Process(target=func,args=(size,my_list[i]))
        processes.append(p)
    for p in processes:
        p.start()
    for p in processes:
        p.join()

start_time_process = time.time()
multiprocessed()   
print("--- %s seconds ---" % (time.time() - start_time_process))
print(len(my_list[0]))

start_time_thread = time.time()   
multithreaded() 
print("--- %s seconds ---" % (time.time() - start_time_thread))
print(len(my_list[0]))
 
"Comparing the execution time, it is possible to see the huge advantage in time of multiprocessing"
"However, if the parallel execution can return useful info for the api, then you should use the threading, because the main program and the thread shares memory"
