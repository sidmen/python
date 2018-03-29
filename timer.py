#!/bin/python

import time # to import the whole package
# from time import localtime, strftime, mktime # to import specific functions from the package (in this case 'time.' is not reqd in front of fns)

start_time = time.localtime()
print("Timer started at %s" % time.strftime("%X", start_time))

#Wait for user input
raw_input("Please press 'Enter' to continue...")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print("Timer stopped at %s" % time.strftime("%X", stop_time))
print("Total time: %s seconds" % difference)
