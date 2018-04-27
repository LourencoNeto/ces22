# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 08:53:07 2018

@author: Lourenço Neto
"""

def elem_both_lists_merge(xs, ys):
    """ Using the merge algorithm to found the elements that exists in both lists """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            if xs[xi] == ys[yi] and xs[xi] not in result:
                result.append(xs[xi])
            xi += 1
        
        else:
            
            yi += 1
            
def elem_only_first_list_merge(xs, ys):
    """ Using the merge algorithm to found the existing elements in the first list and only it """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            if not xs[xi] == ys[yi]:
                result.append(xs[xi])
            xi += 1
        else:
            
            yi += 1

def elem_only_second_list_merge(xs, ys):
    """ Using the merge algorithm to found the existing elements in the first list and only it """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            result.extend(ys[yi:])
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            if xs[xi] == ys[yi]:
                yi += 1
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1
            
def elem_either_lists_merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            #result.extend(ys[yi:]) # Add remaining items from ys
            while yi < len(ys):
                if not ys[yi] in result:
                    result.append(ys[yi])
                yi += 1
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            #result.extend(xs[xi:])
            while xi < len(xs):
                if not xs[xi] in result:
                    result.append(xs[xi])
                xi += 1
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            if not xs[xi] in result:
                result.append(xs[xi])
            xi += 1
        else:
            if not ys[yi] in result:
                result.append(ys[yi])
            yi += 1
            
def elem_only_first_list_not_matched_merge(xs, ys):
    """ Using the merge algorithm to found the existing elements in the first list and only it """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):          # If xs list is finished,
            
            return result          # And we're done.

        if yi >= len(ys):          # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            if not xs[xi] == ys[yi]:
                result.append(xs[xi])             
            else:
                yi += 1
            xi += 1
        else:           
            yi += 1
            
print(elem_both_lists_merge([5,7,11,11,11,12,13], [7,8,11]))