#!/bin/python

import argparser

parser = argparser.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in the words file')

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('/usr/share/dict/words').readlines()
#################################################################
print([word.strip() for word in words if snippet in word.lower()]) # list comprehension #word => 'keith\n', #word.strip() => 'keith'
#################################################################
# matches = []
#
# for word in words:
#     if snippet in word.lower():
#         matches.append(word)
#################################################################
print(matches)
