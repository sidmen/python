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
if module == "hieradata" or module == "hiera":
    new_dir = "C:/Users/spoonath/git/puppet/hieradata"
elif module == "terraform" or module == "terra":
    new_dir = "C:/Users/spoonath/Documents/MISC/Terraform_POC/Terraform"
elif module == "automation" or module == "auto":
    new_dir = "C:/Users/spoonath/Documents/MISC/python_scripts/my_git_python/python/automation"
elif module == "data":
    new_dir = "C:/Users/spoonath/Documents/MISC/data_science_using_python"
elif module == "blackbox":
    new_dir = "C:/Users/spoonath/git/puppet/shoretel_blackbox" 
elif module == "boss":
    new_dir = "C:/Users/spoonath/git/puppet/shoretel_boss"
else:
    new_dir = "C:/Users/spoonath/git/puppet/shoretel_cosmo_" + module
os.chdir(new_dir)

git_bash()
