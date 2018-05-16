# This script is to test anything in Python


import subprocess
import os
# import pandas
# print(os.environ.get('VCENTER_USERNAME'))
# word = 'split it'
# word_split = str(word).split(" ")[1]
# print(word_split)

package = 'pandas'
pip_list = str(subprocess.call(['pip', 'install', package]))
print(pip_list)
