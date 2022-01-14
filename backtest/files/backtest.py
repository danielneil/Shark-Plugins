#!/usr/bin/python

import pandas as pd
import datetime
import subprocess
import os
import sys
import argparse

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

cmd_arg_help = 'This executes the backtest code. For a simple backtest example, see the template'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-s", "--scriptFile", help="A script file containing the commands which are used to build the backtest command line arguments")
    args = parser.parse_args()

    if not args.scriptFile:
        print ("UNKNOWN - No scriptFile specified")
        sys.exit(UNKNOWN)

    scriptFile = args.scriptFile 

    process = subprocess.Popen(['/shark/backtests/bin/' + scriptFile], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()

    exitcode = process.wait()

    print(stdout + stderr)

    sys.exit(exitcode)
