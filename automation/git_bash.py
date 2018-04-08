#!C:\Users\spoonath\AppData\Local\Programs\Python\Python36\python.exe

import os
import subprocess
from subprocess import call

def cwd():
    print(os.getcwd())

def git_bash():
    path_to_git_bash = "C:/Program Files/Git/git-bash.exe"
    call(path_to_git_bash)

module = input("Enter the module: ").lower().strip()
new_dir = "C:/Users/spoonath/git/puppet/shoretel_cosmo_" + module
os.chdir(new_dir)

git_bash()
