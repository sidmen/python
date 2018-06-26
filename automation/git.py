import git
# from git import Repo
puppet_module = 'hieradata'
absolute_path_to_file = 'automation/test2.txt'
commit_message =

path_to_puppet_module = 'git/puppet/' + puppet_module
repo = git.Repo(path_to_puppet_module)
gitobj = repo.git


def git_master_branch():
    gitobj.checkout('master')
    gitobj.add(absolute_path_to_file)
    gitobj.commit('-am', commit_message)
    gitobj.push()
