#!/usr/bin/python3

import sys
import argparse
import urllib2

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = 'This obtains historical instrument data from yahoo finance.'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the desired instrument")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 

    dataFile = urllib2.urlopen("https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1609831036&period2=1641367036&interval=1d&events=history&includeAdjustedClose=true")
    
    with open('/shark/historical/yahoo_finance/BTC-USD','wb') as output:
        output.write(dataFile.read())
 
    sys.exit(OK)
