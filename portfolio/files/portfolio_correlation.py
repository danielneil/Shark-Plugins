#!/usr/bin/python3

import pandas as pd
import datetime
import numpy as np
import sys
import argparse
import os

import seaborn as sn
import matplotlib.pyplot as plt

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

cmd_arg_help = "This plugin generates a correlation matrix from all the available historical data of all intruments."

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description=cmd_arg_help)
    parser.add_argument("-p", "--provider", help="Which provider to the histocal data come from (e.g. yahoo_finance)")
    args = parser.parse_args()

    if not args.provider:
        print ("UNKNOWN - Data provider not supplied")
        sys.exit(UNKNOWN)

    history_dir = ""

    if args.provider == "yahoo_finance_data":
        history_dir = "/shark/historical/yahoo_finance_data"


    # Determine the number of historical files available.
    listdirArr = os.listdir(history_dir)
    
    # Extract data from the histoical files and add to data frame.
    file_dict = {}
    for histFile in listdirArr:
        
        dataFile = pd.read_csv(history_dir + "/" + histFile)
        subFrame = dataFile['Adj Close'] 

        colName = histFile.split(".")[0]

        file_dict[colName] = subFrame

    
    df = pd.DataFrame(file_dict)
    pd.set_option('display.max_rows', None)

    corrMatrix = df.corr()

    plt.figure(figsize=(15,10))

    sn.heatmap(corrMatrix, annot=True)

    plt.savefig('/shark/portfolio/correlation_matrix.png')

    sys.exit(0)
