Script to automate initializing a git and github repo including an initial initial commit

Dependencies:
* Python 2.7

To install (bash):
```
cp ./gitcreate.py /usr/local/bin/gitcreate  #copy to a folder from your PATH variable
chmod +x /usr/local/bin/gitcreate           #make it executable
```
Then, restart your shell.

Default usage:
```
gitcreate
```

Options:
```
optional arguments:
  -h, --help                show help message and exit
  -u USER, --username USER
                            set the username of git and github account
  -r REPO, --reponame REPO
                            set the name of the repository
  -a ACCESS_TOKEN, --accesstoken ACCESS_TOKEN
                            set the access token
  -m COMMIT_MESSAGE, --message COMMIT_MESSAGE
                            specify the first commit message
```

Default values (pseudo-code):
```
access_token: os.environ['github_access_token']
user: 'git config user.name'
repo_name: current_path
commit_message: 'Initial commit'
```

To remove (bash):
```
rm /usr/local/bin/gitcreate          
```

Get your Github access token for full automation!


https://github.com/settings/tokens/new

More info at https://help.github.com/articles/creating-an-access-token-for-command-line-use/