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
- fetch
- merge
- pull
- branch
- checkout


## git files & folders

- .git folder
- .gitignore file

## GitHub

- Pull requests
- SSH authentication to repositories


## Resources

- [Pro Git Book](https://git-scm.com/book/en/v2)


