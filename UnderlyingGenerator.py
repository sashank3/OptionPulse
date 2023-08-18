# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:47:48 2023

@author: sasre
"""

import pandas as pd
from datetime import date
from thetadata import ThetaClient, DateRange, StockReqType


Stocks = pd.DataFrame()
client = ThetaClient() 
ticker = "AAPL"

with client.connect(): 
    
    for year in range(2022, 2024):
        for month in range(1,13):
            
            if(month == 2):
                day = 28
            elif(month in [4,6,9,11]):
                day = 30
            else:
                day = 31
        
            dataStocks = client.get_hist_stock(
                req = StockReqType.EOD,
                root = ticker,
                date_range = DateRange(date(year, month, 1), date(year, month, day)))
            
            Stocks = Stocks.append(dataStocks, ignore_index=True)
    
    Stocks.to_csv('Data/Underlying_Data/AAPL_stock_data.csv')