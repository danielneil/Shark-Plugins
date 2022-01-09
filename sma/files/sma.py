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

cmd_arg_help = "This plugin checks the simple moving average (SMA) for a stock. Based on the output, you can decide to set certain warning and critical threshold levels."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock.")
    parser.add_argument("-p", "--periods", help="Number of trading periods for which to compute against.")
    parser.add_argument("-max", "--max", help="Warn if the result is greater than this threshold.")
    parser.add_argument("-min", "--min", help="Warn if the result is less than this threshold.")
    parser.add_argument("-f", "--provider", help="Which provider to the histocal data come from (e.g. yahoo_finance)")
    args = parser.parse_args()

    if not args.ticker:
        print ("CRITICAL - No ticker found")
        sys.exit(CRITICAL)

    if not args.periods:
        print ("CRITICAL - Periods not supplied")
        sys.exit(CRITICAL)

    if not args.max:
        print ("CRITICAL - Max not supplied")
        sys.exit(CRITICAL)
        
    if not args.min:
        print ("CRITICAL - Min not supplied")
        sys.exit(CRITICAL)
   
    if not args.provider:
        print ("CRITICAL - Data provider not supplied")
        sys.exit(CRITICAL)
        
    ticker = args.ticker
    smaPeriod = int(args.periods)

    history_dir = "/shark/historical/"

    if args.provider == "yahoo_finance":
        datafile = history_dir + args.provider
        
    data = pd.read_csv(datafile + "/" + ticker + ".csv")
    dataFrame = data['Adj Close']
    sma = np.round(dataFrame.rolling(smaPeriod).mean().iloc[-1], 2)

    if args.raw:
        print(str(sma))
        sys.exit(OK)
    else:
        if args.max and int(args.max) <  sma:
            print("WARNING - SMA($" + str(sma) + ") is above threshold " + str(args.max))
            sys.exit(WARNING)
        elif args.min and int(args.min) >  sma:
            print("WARNING - SMA($" + str(sma) + ") is below threshold " + str(args.min))
            sys.exit(WARNING)
        else:
            print("OK - $" + str(sma))
