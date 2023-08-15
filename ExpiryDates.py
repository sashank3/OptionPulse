# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:03:38 2023

@author: sasre
"""


from thetadata import ThetaClient


def expiryDateFinder(ticker):
    
    client = ThetaClient()
    
    with client.connect():
        data = client.get_expirations(ticker)
        filteredData = data[data[:] >= "2022-01-01"]
    
    return filteredData
        