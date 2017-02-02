#!/usr/bin/python

import os
import subprocess
import ntpath


current_path = subprocess.check_output('pwd', shell = True)

def removeNewline(input):
	return input.replace(input[len(input)-1], "")

#repo name
repo = removeNewline(ntpath.basename(current_path))
#github username
user = removeNewline(subprocess.check_output('git config user.name', shell = True))

gitinit = "git init"
gitadd = "git add ."
gitcommit = "git commit -m 'initial commit'"
github_create_repo = "curl -u {0} https://api.github.com/user/repos -d \'{{\"name\" : \"{1}\"}}\'".format(user, repo)
github_add_remote = "git remote add origin git@github.com:{0}/{1}.git".format(user, repo)
gitpush = "git push --set-upstream origin master"

os.system(gitinit)
os.system(gitadd)
os.system(gitcommit)
os.system(github_create_repo)
os.system(github_add_remote)
os.system(gitpush)
print("A new git and github repo is created with the name " + repo)