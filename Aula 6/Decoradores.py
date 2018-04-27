# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:16:53 2018

@author: Lourenço Neto
"""

"Suavização de divisão, para impedir resultado infinito"

def info(debug = False):
    def decorador(func):
        def interna(*args):
            if debug:
                print("Executando funcao " + func.__name__)
            return func(*args)
        return interna
    return decorador

@info(True)
def suavizacao(valor_padrao):
    def deco(func):
        def interna(*args, **kwargs):
            n_args = [i if i != None and i != 0 else valor_padrao for i in args]
            n_kwargs = {c:v if v != None and v != 0 else valor_padrao for c,v in kwargs.items()}
            if args[0] == 0:
                n_args[0] = args[0]
            return func(*n_args, **n_kwargs)
        return interna
    return deco            

@suavizacao(0.000000001)
@info(True)
def func_principal(a, b):
    return a/b
                
print(func_principal(5,0))
print(func_principal(5,1))

    