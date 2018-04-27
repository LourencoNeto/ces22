# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:02:10 2018

@author: Lourenço Neto
"""

def conversation(kind, *args, **kwargs):
    print("An example of a" + kind + " conversation:")
    list_of_keys = list(kwargs.keys())
    first_key = list_of_keys[0]
    second_key = list_of_keys[1]
    for arg in args:
        print(arg)
    i = 0
    name = None
    for kw in kwargs.keys():
        if i % 2 == 0:
            name = first_key
        else:
            name = second_key
        print("- " + name + ": "+ kwargs[kw])
        i = i + 1
        
conversation("Business", "Andre and Carlos are old collegues which don't work together since 2010."
             "After 6 years, they met eachother at a restaurant and had lunch together once more.",
             "See the beggining of the conversation:",
             Andre = "Where are you working now Carlos?",
             Carlos = "I'm working as VP in the ABC company. A dream coming true!",
             Andre1 = "I'm so happy for you. Since the day that we met eachother you talk about it. On my case, I still work at XYZ entrepise, but as a partner now. I got the promotion last week",
             Carlos1 = "That's great to hear!! To celebrate our reunion and your promotion, I will pay our lunchs. Now, tell me more about how XYZ is going.")