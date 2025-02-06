from collections import defaultdict
import argparse
# from signal import signal, SIGPIPE, SIG_DFL
# signal(SIGPIPE,SIG_DFL) 

def countBots(logData, split=False):
    botCounts = defaultdict(int)
    for row in logData:
        if split:
            row = row.split('\t')
        if 'bot' in row[-1].lower():
            botCounts[row[-1]] += 1
            
    return botCounts

def main():
    parser = argparse.ArgumentParser('count_bots.py', description="Counts the number of user agents that include 'bot'.")
    parser.add_argument('file', type=argparse.FileType('r'), help="The Apache file to process (must have tab-separated columns).")
    args = parser.parse_args()
    countBots(args.file, split=True)
    

if __name__ == '__main__':
    main()