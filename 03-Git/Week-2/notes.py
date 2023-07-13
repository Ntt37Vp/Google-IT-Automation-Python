# Undoing
# git checkout filename (git checkout restores files to the latest stored snapshot, reverting any changes before staging.)
# git reset HEAD filename (to untrack; it's like the opposite of git ADD)
# git commit --ammend (to ammend the mistakes on previous commits. git commit --amend allows us to modify and add changes to the most recent commit. )
# WARNING! Do not use git commit --ammend to Public repos because it removes the commit history

# Rollbacks
# git revert (makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.)
# git revert, a new commit is created with inverse changes. This cancels previous changes instead of making it as though the original commit never happened.


# Branching & Merging
# A branch is a pointer
# "Master" is the default branch
# format
# git branch new-branch-name OR shortcut git checkout -b branch-name
# to transfer to another branch, use:
# git checkout
# git branch -d branch-name-to-delete (to delete a branch)
# git merge
# Merging combines branched data and history together
# git log --graph --oneline
