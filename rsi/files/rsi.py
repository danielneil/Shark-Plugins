#!/usr/bin/python3

import pandas as pd
import datetime
import numpy as np
import sys
import argparse
import os

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock.")
    parser.add_argument("-p", "--periods", help="Number of trading periods for which to compute against.")
    parser.add_argument("-f", "--provider", help="Which provider to the histocal data come from (e.g. yahoo_finance)")
    args = parser.parse_args()
    
     - name: rsi
   desc: "RSI: 2 Period with EMA"
   group: "RSI" 
   periods: 2
   max: 90
   min: 10
   data_format: yahoo_finance_data

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    if not args.periods:
        print ("UNKNOWN - Periods not supplied")
        sys.exit(UNKNOWN)
   
    if not args.provider:
        print ("UNKNOWN - Data provider not supplied")
        sys.exit(UNKNOWN)
        
    ticker = args.ticker
    smaPeriod = int(args.periods)

    history_dir = "/shark/historical/"

    if args.provider == "yahoo_finance_data":
        datafile = history_dir + args.provider + "/" + ticker + ".csv"
        
    try:
        f = open(datafile)
        f.close()
    except IOError:
        print("UNKNOWN - Waiting for historical data file - " + str(datafile))
        sys.exit(UNKNOWN)
        
    data = pd.read_csv(datafile)
    
    dataFrame = data['Adj Close']
    
    sma = np.round(dataFrame.rolling(smaPeriod).mean().iloc[-1], 2)
    
    lastPrice = data['Adj Close'].iloc[-1]
       
    if sma <  lastPrice:
        print("OK - Price $" + str(lastPrice) + " is above SMA $" + str(sma))
        sys.exit(OK)
            
    elif sma >  lastPrice:
        print("WARNING - Price $" + str(lastPrice) + " is below SMA $" + str(sma))
        sys.exit(WARNING)      
