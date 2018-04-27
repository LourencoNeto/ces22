# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 22:49:44 2018

@author: Lourenço Neto
"""

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main():
    import random
    import time
    
    rng = random.Random()   # Instantiate a generator
    
    size = 4
    tries = 0
    over = False
    while not over:        
       start_time = time.time()
       bd = list(range(size))     # Generate the initial permutation
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           print("Found solution {0} in {1} tries.".format(bd, tries))
           tries = 0
           size = size + 4
           
           if time.time() - start_time > 60: #The execution time of searching a useful combination is greater than a minute, tell it
               print("The maximum size puzzle looked for is {0}" .format(size - 8))
               over = True
main()