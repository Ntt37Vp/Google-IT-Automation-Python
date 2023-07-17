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

<<<<<<< HEAD
# git remote show origin
# git branch -r
# git fetch
# git merge
# Note: git pull instantly merges while git fetch only retrieves remote updates.

# Git Remote Summary
# git remote        | Lists remote repos
# git remote -v     | List remote repos verbosely
# git remote show   | Describes a single remote repo
# git remote update | Fetches the most up-to-date objects
# git fetch         | Downloads specific objects
# git branch -r     | Lists remote branches; can be combined with other branch arguments to manage remote branches


# Practice Quiz
# git remote update will fetch the contents of all remote branches and allow us to merge the contents ourselves.
# If you want to see more information about a particular remote branch, you can use the git remote show command. Don't forget the commit ID!
# git fetch will download remote updates, such as objects and refs, from the remote branch.
# git pull automatically merges the remote branch with the current branch.
# explicit merge

# Solving Conflicts
#
=======
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


>>>>>>> a22d9a802e041268e70a2dd51c5f72c3761c42ae
