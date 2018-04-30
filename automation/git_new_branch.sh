#!/bin/bash

# $BRANCH = "$1"

cd /c/Users/spoonath/git/puppet/hieradata
git checkout -b "$1" production
touch fqdn/sv2bpsr23qav.stsky.biz.eyaml
touch clusters/sit-cc1.eyaml
git add .
git commit -am "created branch $1"
git push --set-upstream origin "$1"
git rm fqdn/sv2bpsr23qav.stsky.biz.eyaml
git rm clusters/sit-cc1.eyaml
git commit -am "modified $1"
git push --set-upstream origin "$1"
