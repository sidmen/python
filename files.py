#!/bin/python

import os
#
# xmen_file = open('xmen.txt')
#
# # print(xmen_file.read())
# # for line in xmen_file:
# #     print(line)
#
# xmen_file.close()
#####################################################################
# # xmen_2_file = open('xmen_2.txt', 'w')
# xmen_2_file = open('xmen_2.txt', 'r+')  # read and write mode
#
# xmen_2_file.seek(-1, os.SEEK_END)
#
# xmen_2_file.write("\nBeast\n")
# xmen_2_file.write("Phoenix\n")
#
# xmen_2_file.close()
#####################################################################
#
# xmen_file = open('xmen.txt', 'a') # append mode
# xmen_file.writelines(['Morph\n', 'Rogue\n'])
# xmen_file.close()
#####################################################################

with open('xmen.txt', 'a') as xmen_file:  # using with you dont have to close the file
    xmen_file.write("Professer Xavier\n")
