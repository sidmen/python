#!/bin/python

#this script shows how to execute shell commands within python


import subprocess

# #######################################################
# code = subprocess.call(['ls', '-l'])
# if code == 0:
#     print("command finished successfully")
# else:
#     print("failed with code: %i" % code)
########################################################

try:
    output = subprocess.check_output(
            ['ls', '-l', 'fake.txt'],
            stderr=subprocess.STDOUT
            )
except OSError as err:
    print("Caught OSError")
    output  = err
except subprocess.CalledProcessError as err:
    print("Caught CalledProcessError")
    output = err
print("%s   %s" % (output, "\ndone it"))
