#!/usr/bin/python

#Note: this program expects an access token
#See https://help.github.com/articles/creating-an-access-token-for-command-line-use/
#Create it at https://github.com/settings/tokens/new

import os
import sys
import subprocess
import ntpath
import argparse

parser = argparse.ArgumentParser(description='Automatically set up your local and online git(hub) repository from the commandline.')

#See http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
#Some Ansi tricks are used ;)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def removeNewline(text):
	return text.replace(text[len(text)-1], "")

def sysDebug(command):
	print(bcolors.UNDERLINE + bcolors.OKGREEN + 'Working on: ' + command + bcolors.ENDC)
	return os.system(command)

def debug(text):
	print(bcolors.UNDERLINE + bcolors.FAIL + text + bcolors.ENDC)

#Settings
current_path = subprocess.check_output('pwd', shell = True)
access_token = os.environ['github_access_token']
user = removeNewline(subprocess.check_output('git config user.name', shell = True))
repo = removeNewline(ntpath.basename(current_path))

parser.add_argument('-u', '--username', default=user, dest='user', help='set the username')
parser.add_argument('-r', '--reponame', default=repo, dest='repo', help='set the name of the repository')
parser.add_argument('-a', '--accesstoken', default=access_token, dest='access_token', help='set the access token')
parser.add_argument('-m', '--message', default='Initial commit', dest='commit_message', help='specify the first commit message')

args = parser.parse_args()
access_token = args.access_token
user = args.user
repo = args.repo
commit_message = args.commit_message

#Commands
gitinit = "git init"
gitadd = "git add ."
gitcommit = "git commit -m" + "'" + commit_message + "'"
github_create_repo = "curl https://api.github.com/user/repos?access_token={0} -d \'{{\"name\" : \"{1}\"}}\'".format(access_token, repo)
github_add_remote = "git remote add origin git@github.com:{0}/{1}.git".format(user, repo)
gitpush = "git push --set-upstream origin master"

#Final settings
if not access_token:
    github_create_repo = "curl -u {0} https://api.github.com/user/repos -d \'{{\"name\" : \"{1}\"}}\'".format(user, repo)

#Local
sysDebug(gitinit)
sysDebug(gitadd)
sysDebug(gitcommit)

#Remote
status_code = sysDebug(github_create_repo)
if not status_code == 0:
    debug('curl did not complete status code is: ' + str(2))
    sys.exit()
sysDebug(github_add_remote)
sysDebug(gitpush)


#Finish
debug("Done")
debug("https://github.com/melvinroest/" + repo + "/settings")



