#!/usr/bin/python3

import datetime
import subprocess
import os
import sys
import argparse

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = 'This executes the data code.'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-t", "--ticker", help="Ticker code of the desired instrument")
    args = parser.parse_args()

    if not args.ticker:
        print ("UNKNOWN - No ticker specified")
        sys.exit(UNKNOWN)

    ticker = args.ticker 


    
    exitcode = process.wait()

    print(stdout)

    sys.exit(exitcode)
