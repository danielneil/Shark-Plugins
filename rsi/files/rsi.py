#!/usr/bin/python3.9

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
    parser.add_argument("-m", "--min", help="The min threshold which will alert if reached.")
    parser.add_argument("-x", "--max", help="The max threshold which will alert if reached.")
    parser.add_argument("-y", "--ma_type", help="If ema or sma will be used when computing the rsi.")
    parser.add_argument("-f", "--provider", help="Which provider to the histocal data come from (e.g. yahoo_finance)")
    args = parser.parse_args()
   
    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    if not args.periods:
        print ("UNKNOWN - Periods not supplied")
        sys.exit(UNKNOWN)
   
    if not args.provider:
        print ("UNKNOWN - Data provider not supplied")
        sys.exit(UNKNOWN)
        
    if not args.min:
        print ("UNKNOWN - min not supplied")
        sys.exit(UNKNOWN)    
        
    if not args.max:
        print ("UNKNOWN - max not supplied")
        sys.exit(UNKNOWN)    
        
    if not args.ma_type:
        print ("UNKNOWN - ma_type not supplied")
        sys.exit(UNKNOWN)            
        
    ticker = args.ticker
    periods = int(args.periods)
    provider = args.provider
    min = args.min
    max = args.max
    ma_type = args.ma_type

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
    
    close_delta = data['Adj Close'].diff()
    
    # Make two series: one for lower closes and one for higher closes
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    
    if ma_type == "ema":
	    # Use exponential moving average
        ma_up = up.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
        ma_down = down.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
    else:
        # Use simple moving average
        ma_up = up.rolling(window = periods, adjust=False).mean()
        ma_down = down.rolling(window = periods, adjust=False).mean()
        
    rsi = ma_up / ma_down
    rsi = 100 - (100/(1 + rsi))

    print(rsi.iloc[-1])
    
