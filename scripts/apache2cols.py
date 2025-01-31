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


for line in sys.stdin:
    columns = csv.reader([line], delimiter=" ").__next__()
    print('\t'.join(columns))
    
    
    
    
    