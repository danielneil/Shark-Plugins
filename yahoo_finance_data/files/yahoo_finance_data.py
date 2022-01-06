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
    
    datafile =  "/shark/historical/yahoo_finance/" + str(ticker)
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'+str(ticker)+'?period1='+str(period1)+'&period2='+str(period2)+'&interval='+str(interval)+'&events=history&includeAdjustedClose='+str(includeAdjustedClose)
    
    try:
        urllib.request.urlretrieve(url, datafile)
    except urllib.error.ContentTooShortError as shortError:
        print("Error: Content too short error")
        print("URL: " + str(url))
        sys.exit(UNKNOWN)
    except urllib.error.HTTPError as e:
        print(e)
        print("URL: " + str(url))
        sys.exit(UNKNOWN)
    except urllib.error.URLError as ue: # such as timeout
        print("Error: fail to download!")
        print("URL: " + str(url))
        sys.exit(UNKNOWN)
    except socket.timeout as se: # very important
        print("Error: socket timeout")
        print("URL: " + str(url))
        sys.exit(UNKNOWN)
    except Exception as ee:
        print(ee)    
        print("URL: " + str(url))
        sys.exit(UNKNOWN)
    
    print("Downloaded historical data file for " + str(ticker))
    sys.exit(OK)
