#!C:/Users/spoonath/AppData/Local/Programs/Python/Python36/python.exe

import os
# import subprocess
from subprocess import call


def cwd():
    print(os.getcwd())


def git_bash():
    path_to_git_bash = "C:/Program Files/Git/git-bash.exe"
    call(path_to_git_bash)


module = input("Enter the module: ").lower().strip()
if module == "hieradata":
    new_dir = "C:/Users/spoonath/git/puppet/" + module
elif module == "terraform":
    new_dir = "C:/Users/spoonath/Documents/MISC/Terraform_POC/Terraform"
elif module == "automation":
    new_dir = "C:/Users/spoonath/Documents/MISC/python_scripts/my_git_python/python/automation"
else:
    new_dir = "C:/Users/spoonath/git/puppet/shoretel_cosmo_" + module
os.chdir(new_dir)

git_bash()
