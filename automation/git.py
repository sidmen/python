import git
from git import Repo

puppet_module = 'hieradata'
absolute_path_to_file = 'clusters/hq7.eyaml'
commit_message = 'some message'

path_to_puppet_module = 'git/puppet/' + puppet_module
repo = git.Repo(path_to_puppet_module)
gitobj = repo.git


def git_master_branch():
    gitobj.checkout('master')
    gitobj.add(absolute_path_to_file)
    gitobj.commit('-am', commit_message)
    gitobj.push()


#### NEED TO TEST THIS #####

# def git_qa_branch():
#     gitobj.checkout('qa')
#     gitobj.pull()
#     gitobj.merge('master')

###############################


git_master_branch()
