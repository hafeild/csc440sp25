'''
File:       apache2cols.py
Author:     Hank Feild
Date:       2025-01-31
Purpose:    Convert Apache log format to tab-delimited columns.

Usage example:  
    cat access.log | python3 apache2cols.py > access.tsv
'''

import csv
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 
import argparse

# # This assumes that certain fields will always contain a fixed number of
# # space-separated fields.  This is not a general solution.
# for line in sys.stdin:
#     cols = line.strip().split()
#     logicalCols = [
#         cols[0], # ip address
#         cols[1], # client id
#         cols[2], # username
#         ' '.join(cols[3:5]), # timestamp
#         ' '.join(cols[5:8]), # request
#         cols[8], # status code
#         cols[9], # response size in bytes
#         cols[10], # referer [sic]
#         ' '.join(cols[11:]) # user agent
#     ]
#     print('\t'.join(logicalCols))

# for line in sys.stdin:
#     columns = csv.reader([line], delimiter=" ").__next__()
#     print('\t'.join(columns))

def formatFile(input):

    for line in input:
        columns = csv.reader([line], delimiter=" ").__next__()
        print('\t'.join(columns))

def main():
    # Using sys.argv directly.
    # if len(sys.argv) > 1:
    #     with open(sys.argv[1], 'r') as file:
    #         formatFile(file)
    # else:
    #     formatFile(sys.stdin)
    
    parser = argparse.ArgumentParser('apache2cols.py', description="Splits an Apache log into tabular columns.")
    # parser.add_argument('--file', required=False, type=str, help="The Apache file to process.")
    # parser.add_argument('file', nargs="?", type=str, help="The Apache file to process.")
    
    # args = parser.parse_args()
    
    # if args.file is None:
    #     formatFile(sys.stdin)
    # else:
    #     # with open(args.file, 'r') as file:
    #     #     formatFile(file)
    #     formatFile(open(args.file))
    
    parser.add_argument('file', type=argparse.FileType('r'), help="The Apache file to process.")
    args = parser.parse_args()
    formatFile(args.file)
    
    
if __name__ == '__main__':
    main()
    
    