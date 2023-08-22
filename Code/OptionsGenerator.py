# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 21:00:30 2023

@author: sasre
"""

import pandas as pd
from datetime import date
from RequestLimiter import requestLimiter
from ExpiryDates import expiryDateFinder
from thetadata import ThetaClient, OptionReqType, OptionRight, DateRange, NoData


Options = pd.DataFrame()
client = ThetaClient() 
count = 5
ticker = "AAPL"


datesOfExpiry = expiryDateFinder(ticker)

with client.connect():  
    
    for dateOfExpiry in datesOfExpiry:
        
        print(" ")
        print("=================================================")
        print("Starting for dateOfExpiry: " + str(dateOfExpiry))    
        print("=================================================")
        print(" ")
        
        strikes = client.get_strikes(ticker, dateOfExpiry)
        strikeStart = int(strikes.min())
        strikeEnd = int(strikes.max())
        
        for strike in range(strikeStart, strikeEnd, 5):
            
            try:
                #Options Data:
                dataOptions = client.get_hist_option(
                      req = OptionReqType.EOD,
                      root = ticker,
                      exp = dateOfExpiry,
                      strike = strike,
                      right = OptionRight.CALL,
                      date_range = DateRange(date(2012, 8, 1), date(2030, 12, 31)))
                    
                #Add Strike Price:
                dataOptions['DataType.STRIKEPRICE'] = strike
                dataOptions['DataType.EXPIRY'] = dateOfExpiry
            
                Options = Options.append(dataOptions, ignore_index=True)
            
            except NoData:
                count = requestLimiter(count)
                continue
                
            #To prevent timeout from API. Maximum of 30 API Calls per minute.    
            count = requestLimiter(count)
            
        Options.to_csv('Data/options_EOD_data_' + str(dateOfExpiry).split()[0] + '.csv')
        Options = pd.DataFrame()
        
        
# We are out of the client.connect() block, so we can no longer make requests.   


def dataToCsv(csv_filename, database):

    database.to_csv(csv_filename, index=False)


















