#!/usr/bin/python3

import sys
import argparse
import urllib.request

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = 'This obtains historical instrument data from yahoo finance.'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the desired instrument")
    parser.add_argument("-p1", "--period1", help="Data start date")
    parser.add_argument("-p2", "--period2", help="Data end date")
    parser.add_argument("-i", "--interval", help="Time interval of the data")
    parser.add_argument("-a", "--includeAdjustedClose", help="includeAdjustedClose [TRUE|FALSE] ")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    if not args.period1:
        print ("UNKNOWN - No period1 specified")
        sys.exit(UNKNOWN)
        
    if not args.period2:
        print ("UNKNOWN - No period2 specified")
        sys.exit(UNKNOWN)
    
    if not args.interval:
        print ("UNKNOWN - No interval specified")
        sys.exit(UNKNOWN) 
        
    if not args.includeAdjustedClose:
        print ("UNKNOWN - No includeAdjustedClose specified")
        sys.exit(UNKNOWN) 
        
    ticker = args.ticker 
    period1 = args.period1
    period2 = args.period2
    interval = args.interval
    includeAdjustedClose = args.includeAdjustedClose
    
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'+ticker+'?period1='+period1+'&period2='+period2+'&interval='+interval+'&events=history&includeAdjustedClose='+includeAdjustedClose
    urllib.request.urlretrieve(url, "/shark/historical/yahoo_finance/" + ticker)

    sys.exit(OK)
