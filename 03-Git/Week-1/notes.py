# Course 3 - Git & Github
# Week 1

# Before VCS
# DIFF
# example:
# DIFF file1 file2
# -u flag shows a unified format
# DIFF -u file1 file2
# wdiff shows the words difference
# the DIFF output could also be redirected into a .diff file
# format:
# DIFF -u file1 file2 > change.diff

# .diff can be manually worked on OR automate using PATCH command!
# to use the PATCH:
# PATCH target_file < fix_file.diff

# Here comes VCS
# Git
# git-scm.com

# Steps:
# Install Git
# sudo apt update
# sudo apt install git
# git --version

# Initialize
# mkdir my-git-repo
# cd my-git-repo
# git init

# Config
# git config --global user.name "Name"
# git config --global user.email "user@example.com"

# staging
# git add -a

# commit
# git commit
# git commit -m (to add short commit message)
# git commit -a (shortcut to stage tracked files without using git add)

# review
# git log -p (patch; shows the diff )
# git show commitID (shows details of a specific commit ID)
# git diff (shows the changes made )
# git add -p

# renaming and deleting
# git rm (stop tracking and remove it)
# git mv (rename)

# Undoing
# git checkout filename (git checkout restores files to the latest stored snapshot, reverting any changes before staging.)
# git reset HEAD filename (to untrack; it's like the opposite of git ADD)
# git commit --ammend (to ammend the mistakes on previous commits. git commit --amend allows us to modify and add changes to the most recent commit. )
# WARNING! Do not use git commit --ammend to Public repos because it removes the commit history

# Rollbacks
# git revert (makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.)
