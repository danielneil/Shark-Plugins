#!/usr/bin/python3.9

import subprocess
import os.path
from os import path
import sys
import argparse
import string

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = 'This executes the backtest code. For a simple backtest example, see the template.'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-b", "--backTestFile", help="The name of the file containing the back test code.")
    parser.add_argument("-s", "--scriptFile", help="A script file containing the commands which are used to build the backtest command line arguments.")
    args = parser.parse_args()

    if not args.backTestFile:
        print ("UNKNOWN - No backTestFile specified")
        sys.exit(UNKNOWN)

    if not args.scriptFile:
        print ("UNKNOWN - No scriptFile specified")
        sys.exit(UNKNOWN)
        
    scriptFile = args.scriptFile
    backTestFile = args.backTestFile
    
    result  = subprocess.run(['/shark/backtests/' + backTestFile, "@" + scriptFile], capture_output=True, text=True)

    print(result.stdout + " " + result.stderr)

    sys.exit(result.returncode)
