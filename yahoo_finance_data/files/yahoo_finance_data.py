#!/usr/bin/python3

import os
import sys
import argparse
import urllib.request

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = 'Obtains historical instrument data from Yahoo! finance and imports it into Shark.'

############################################################################
# Checks if the historical data directory is writable.
def is_dir_writable():
    
    # Test to see if the directory is writable.
    try:
    
        # open file in write mode
        with open(directory + ".testfile", 'w') as f:
            f.write('testing if writable')

        os.remove(directory + ".testfile")
        
    except Exception as e:
        print("UNKNOWN - Problem writing to " + directory)
        print(e)
        sys.exit(UNKNOWN) 


############################################################################
# Main
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the desired instrument")
    parser.add_argument("-p1", "--period1", help="Time peroid from")
    parser.add_argument("-p2", "--period2", help="Time peroid to")
    parser.add_argument("-i", "--interval", help="Time interval of the data")
    parser.add_argument("-a", "--includeAdjustedClose", help="Include Adjusted Close")
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
    
    directory = "/shark/historical/yahoo_finance_data/" 
    datafile =  str(ticker) + ".csv"
    filename = directory + datafile
    
    url = 'https://query1.finance.yahoo.com/v7/finance/download/'+ticker+'?period1='+period1+'&period2='+period2+'&interval='+interval+'&events=history&includeAdjustedClose='+str(includeAdjustedClose)
     
    is_dir_writable()    
        
    try:
        
        urllib.request.urlretrieve(url, filename)
        
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
