#!/usr/bin/python3

import pandas as pd
import datetime
import numpy as np
import sys
import argparse
import os
import yfinance as yf

cmd_arg_help = "This plugin downloads yahoo finance historical data."

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

DATA_DIR = "/shark/cache"

https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1604262454&period2=1635798454&interval=1d&events=history&includeAdjustedClose=true

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock.")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)
        
dataFrame = yf.Ticker(args.ticker)

dataFrame.history(peroid="max").to_csv("ticker.csv")
