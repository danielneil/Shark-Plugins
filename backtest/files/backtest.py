#!/usr/bin/python3

import subprocess
import os
import sys
import argparse

OK           = 0
WARNING      = 1
CRITICAL     = 2
UNKNOWN      = 3

if __name__ == "__main__":

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

    process = subprocess.Popen(['/shark/backtests/' + backTestFile, "@" + scriptFile], stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()

    exitcode = process.wait()

    print(stdout + stderr)

    sys.exit(exitcode)
