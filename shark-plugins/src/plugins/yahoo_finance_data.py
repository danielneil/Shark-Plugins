#!/usr/bin/python3

import yfinance as yf
import datetime 
start = datetime.datetime(2012,5,31) 
end = datetime.datetime(2013,1,30) 
Amazon = yf.Ticker("BTC-USD") 
print(Amazon.history(start=start, end=end))
