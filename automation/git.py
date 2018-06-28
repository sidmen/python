import git
from git import Repo

puppet_module = 'hieradata'
commit_message = 'some message'
merge_to_branch = 'qa'
path_to_puppet_module = '/Users/spoonath/git/puppet/' + puppet_module

repo = Repo(path_to_puppet_module)
gitfn = repo.git


def commit_to_master():
    gitfn.checkout('master')
    print("Current branch: master")
    print("Staging new/modified files")
    gitfn.add('.')
    print("Committing changes to master branch")
    gitfn.commit('-am', commit_message)
    print("Push to remote master")
    gitfn.push()
    print("Successfully pushed to master branch")


def merge_from_master():
    print("Switch to %s branch to start merging" % merge_to_branch)
    gitfn.checkout(merge_to_branch)
    print("Current branch: %s" % merge_to_branch)
    print("Sync remote {} to local {}".format(merge_to_branch, merge_to_branch))
    gitfn.pull()
    print("Merge to %s from master" % merge_to_branch)
    gitfn.merge('master')
    print("Push to remote %s" % merge_to_branch)
    gitfn.push()
    print("Switch to master branch")
    gitfn.checkout('master')
    print("Voila! Merge to %s is completed and you are back in master branch" % merge_to_branch)


commit_to_master()
merge_from_master()
