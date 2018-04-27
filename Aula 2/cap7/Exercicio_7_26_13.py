# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 01:12:06 2018

@author: Lourenço Neto
"""

"""
O problema consiste em verificar quais das figuras podem ser desenhadas atendendo o requisito
de passar por cada aresta somente uma vez

Levando em conta que cada figura dessa pode ser tratada como um grafo não direcionado e cíclico,
O percurso, conforme indicação do exercício, se trata de um caminho Euleriano:
    Caso o número de vértices do grafo que possuam grau ímpar seja 0 ou 2, é possível traçar um caminho Euleriano por ele
Sendo assim, para verificação que a figura é possível de se desenhar ou não,
Bastaria passar a matriz de adjacências do grafo e contar quantos vértices está ligado a uma lista ligada (Que informa com quais vértices ele está conectado) 
com número ímpar de elementos. Se a quantidade de vértices que atingem esse requisito for 0 ou 2, a figura pode ser desenhada.
"""