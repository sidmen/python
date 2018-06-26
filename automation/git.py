import git
# from git import Repo
puppet_module = 'hieradata'
absolute_path_to_file = 'automation/test2.txt'

path_to_puppet_module = 'git/puppet/' + puppet_module
repo = git.Repo(path_to_puppet_module)


def git_master_branch():
    repo.git.checkout('master')
    repo.git.add(absolute_path_to_file)
    repo.git.commit('-am', message)
    repo.git.push()
