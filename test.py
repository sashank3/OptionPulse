# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 01:49:24 2023

@author: sasre
"""

import pandas as pd
from datetime import date
from thetadata import ThetaClient, OptionReqType, OptionRight, DateRange, SecType

client = ThetaClient()  # We don't need to provide a username / password because this is a free request.

with client.connect():  # Make any requests for data inside this block. Requests made outside this block wont run.
    data = client.get_strikes("AAPL", date(2022, 7, 1))
    
    dataOptions = client.get_hist_option(
          req = OptionReqType.EOD,
          root = "AAPL",
          exp = date(2022, 7, 1),
          strike = 245,
          right = OptionRight.CALL,
          date_range = DateRange(date(2012, 8, 1), date(2030, 12, 31)))
    
# We are out of the client.connect() block, so we can no longer make requests.   
print(dataOptions)

