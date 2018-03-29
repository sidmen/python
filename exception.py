#!/bin/python

# This script is for exception handling


import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0' )
"%(prog)s 2.0" % {'prog': 'reverse-file'}
args = parser.parse_args()

try:
    f = open(args.filename)
except IOError as err:
    print("Error: file not found")
else: # use this if required
    with f: #since f is already defined in try block, else, it would have been "with expression as target:"
        limit = args.limit
        lines = f.readlines()
        lines.reverse()
        if limit:
            lines = lines[:limit]
        for line in lines:
            print(line.strip()[::-1])
finally: #optional
    print("\nWe're finished\n")
