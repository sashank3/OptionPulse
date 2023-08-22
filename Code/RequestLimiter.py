# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 01:37:32 2023

@author: sasre
"""
import time

def requestLimiter(count):
    
    count += 1
    
    if(count == 29):
        count = 0
        time.sleep(60)
    return count