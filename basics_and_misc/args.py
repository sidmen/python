#!/bin/python
#
# import sys
#
# print("First argument %s" % sys.argv[0])

# ####################################################################
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument('filename', help='the file to read')
# args = parser.parse_args()
#
# #This will generate error and help message
#####################################################################

import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0' )
"%(prog)s 2.0" % {'prog': 'reverse-file'}
args = parser.parse_args()
