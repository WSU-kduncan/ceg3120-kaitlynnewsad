# Project 0 - Git Guide

In your repo for this course, create a file named `git-guide.md`. In this file, write up a quick guide to using git & GitHub. For each command, include a brief definition of what it does, and a sample of how to use it.

## Command line git

- status
  - Shows status of the local repository. This status includes:
    - number of local commits that have not been synced with remote (GitHub)
    - list of files in local folder than are NOT being tracked by git
    - list of files in local folder that have changes that need to be committed
  - `git status`
- clone
  - Clone a repository into a new directory 
  - `git clone`
- add
  - Add file contents to the index. If you want to make changes in the next commit must run `git add` again.
  - `git add`
- rm
  - Remove files from the working tree and from the index. 
    - Will not remove a file from your working directory. 
    - The files being removed have to be indentical to the tip of the branch, and no updates. 
  - `git rm`
- commit
  - Record the chnages to your repository. Use this after the `git add`
  - `git commit`
- push
  - Update remote refs along with associated objects
  - `git push`
- fetch
  - Download objects and refs from another repository
  - Can fetch from either a single named repository or URL
  - `git fetch`
- merge
  - Join two or more development histories together
  - Is used by 'git pull' to incorporate changes from another repository and can be used by hand to merge changes from one branch into another.
  - `git merge`
- pull
  - Fetch from and integrate with another repository or a local branch
  - `git pull` runs `git fetch` with the given parameters and then depending on configuration options or command line flags
  - `git pull`
- branch
  - List, create, or delete branches
  - `--list`: shows existing branches
  - `git branch`
- checkout
  - Switch branches or restore working tree files
  - Updates files in the working tree to match the version in the index or the specified tree
  - `git checkout`


## git files & folders

- .git folder
  - Contains all information that is necessary for the project and all information relating commits, remote repository address.
  - Also contains a log that stores the commit history.
  - `cd .git`
- .gitignore file
  -  A text file that tells Git which files or folders to ignore in a project
  -  `cd gitignore`

## GitHub

- Pull requests
  - Tells others chnages you have made with with the repository.
  - [How Pull Request Sample] (https://docs.github.com/en/issues/tracking-your-work-with-issues/assigning-issues-and-pull-requests-to-other-github-users)
- SSH authentication to repositories
  - SSH key is an alternate way to identify yourself that doesn't require you to enter you username and password every time
  - SSH keys come in pairs, a public key that gets shared with services like GitHub, and a private key that is stored only on your computer. If the keys match,   you're granted access.
  - [How To Create a SSH Key] https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html


## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)


