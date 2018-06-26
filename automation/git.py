import git
# from git import Repo
repo = git.Repo('git/puppet/hieradata')
print(repo.git.status())
