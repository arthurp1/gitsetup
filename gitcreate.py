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


# cmd1 
# hello = "Hello {0} {1}".format(42, 'twenny five')

gitinit = "git init"
gitadd = "git add ."
gitcommit = "git commit -m 'initial commit'"
github_create_repo = "curl -u {0} https://api.github.com/user/repos -d \'{{\"name\" : \"{1}\"}}\'".format(user, repo)
github_add_remote = "git remote set-url origin git@github.com:{0}/{1}.git".format(user, repo)
gitpush = "git push --set-upstream origin master"

os.system(gitinit)
os.system(gitadd)
os.system(gitcommit)
print(github_create_repo)
print(github_add_remote)
print(gitpush)




# cmd2 = 'remote set-url origin git@github.com:${USER:-${GITHUBUSER}}/${REPONAME:-${CURRENTDIR}}.git'
# subprocess.call(['touch ', r, '.html'], shell = True)


# subprocess.Popen('touch %u.html', shell = True)

# print(r)
# # print(u)

# def subprocess_cmd(command):
#     git add. 
#     git -m 's'

# subprocess_cmd(cmd1, cmd2, cmd3, )

# subprocess_cmd('git remote set-url orgiin git@github.com%u/ add ; git commit -m \'initial commit\' ; )



# CURRENTDIR=${PWD##*/}
# GITHUBUSER=$(git config github.user)
# 
# git remote set-url origin git@github.com:${USER:-${GITHUBUSER}}/${REPONAME:-${CURRENTDIR}}.git
# git add .
# git commit -m 'initial commit'
# git push --set-upstream origin master
# }

# executable with python gitcreate.py
# create alias