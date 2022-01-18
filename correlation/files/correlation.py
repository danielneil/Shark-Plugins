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

def DataFileReady(datafile):

    try:
        f = open(datafile)
        f.close()
    except IOError:
        print("UNKNOWN - Waiting for historical data file - " + str(datafile))
        sys.exit(UNKNOWN)

cmd_arg_help = "This plugin checks the correlation between two instrumenets"

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t1", "--ticker1", help="Ticker code of the first intrument to test correlation")
    parser.add_argument("-t2", "--ticker2", help="Ticker code of the second intrument to test correlation ")
    parser.add_argument("-f", "--provider", help="Which provider to the histocal data come from (e.g. yahoo_finance)")
    args = parser.parse_args()

    if not args.ticker1:
        print ("UNKNOWN - No ticker found")
        sys.exit(UNKNOWN)

    if not args.ticker2:
        print ("UNKNOWN - No ticker2 found")
        sys.exit(UNKNOWN)

    if not args.provider:
        print ("UNKNOWN - Data provider not supplied")
        sys.exit(UNKNOWN)

    ticker1 = args.ticker1
    ticker2 = args.ticker2

    history_dir = "/shark/historical/"

    datafile1 = ""
    datafile2 = ""

    if args.provider == "yahoo_finance_data":
        datafile1 = history_dir + args.provider + "/" + ticker1 + ".csv"
        datafile2 = history_dir + args.provider + "/" + ticker2 + ".csv"

    DataFileReady(datafile1)
    DataFileReady(datafile2)
        
    data1 = pd.read_csv(datafile1)
    data2 = pd.read_csv(datafile2)
    
    dataFrame1 = data1['Adj Close']
    dataFrame2 = data2['Adj Close']

    correlation = dataFrame1.corr(dataFrame2)

    corr_abs = abs(correlation)

    exitcode = OK

    if corr_abs > .5:
        print("CRITICAL - Strong correlation of " + str(correlation))
        exitcode = CRITICAL
    else:
        print("OK - Weak correlation of " + str(correlation))


    sys.exit(exitcode)
