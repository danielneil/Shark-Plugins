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

DATA_DIR = "/shark/cache/historical_data"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the stock.")
    parser.add_argument("-startdate", "--startdate", help="Format YYYY,MM,DD")
    parser.add_argument("-enddate", "--enddate", help="Format YYYY,MM,DD")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)
        
    if not args.startdate:
        print ("UNKNOWN - No startdate entered")
        sys.exit(UNKNOWN)
        
    if not args.enddate:
        print ("UNKNOWN - No enddate entered")
        sys.exit(UNKNOWN)
  
start = datetime.datetime(2019,5,31) 
end = datetime.datetime(2020,5,30) 
Amazon = yf.Ticker(args.ticker)

whie open("demofile2.txt", "a") as f:
  f.write(Amazon.history(start=start, end=end) 
  f.close()
