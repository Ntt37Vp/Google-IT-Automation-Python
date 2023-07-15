# Course 3 - Week 3 - Remote Repo (GitHub, etc)

# git clone
# git push

# Using SSH (recommended)
# git config --global user.name "Your Name"
# git config --global user.email "yourname@example.com"
# ls ~/.ssh/id_ed25519.pub
# ssh-keygen -t ed25519 -C <youremail>
# cat ~/.ssh/id_ed25519.pub
# Upload .pub to GitHub settings

# Using Cred Helper (15 mins only)
# git config --global credential.helper cache



# git fetch
# git merge
# git pull

# Sample flow of creating a new feature branch
# git checkout -b new_feature
# change codes, then commit
# git push -u origin new_feature
# git rebase
# git rebase branch_name (moves the current branch on top of the new branch)
# git push --delete origin new_feature (to delet the new branch)

# git rebase and git merge (are simiar)
# Rebasing instead of merging rewrites history and maintains linearity, making for cleaner code.

# Practice QUiz
# It's common practice to keep the latest version in the master branch and the latest stable version in a separate branch.
# Git Rebase (use to change the base of the current branch)
# Git Pull (command that will trigger a merge. git pull command runs git fetch with the given parameters, then calls git merge to merge the retrieved branch heads into the current branch.)


