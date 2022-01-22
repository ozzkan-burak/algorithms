#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 10:41:41 2022

@author: path
"""
def is_isogram(string):
    string = string.lower()
    stringList = list(string)
    stringCluster = set(string)
    
    if(len(stringList) == len(stringCluster)):
        return True
    else:
        return False
    
print(is_isogram('BurakOzkan'))
print(is_isogram('BuseOzkan'))
    