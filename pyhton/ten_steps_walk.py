#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:09:08 2022

@author: path
"""

def is_valid_walk(walk):
    if(len(walk) == 10):
        if(walk.count('e') == walk.count('w')):
            if(walk.count('n') == walk.count('s')):
                return True
            
    return False


print(is_valid_walk(['e','w','e','e','w','w','s','s','n','n']))
print(is_valid_walk(['e','w','e','e','w','s','n','n']))