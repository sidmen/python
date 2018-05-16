import os
from pathlib import Path
# CWD = os.path.dirname(os.path.realpath(__file__))
CWD = os.getcwd()
print(CWD)
# print(Path(CWD).parent)

path_to_excel = str(Path(CWD).parent) + '\katello_input.xlsx'
print(path_to_excel)
