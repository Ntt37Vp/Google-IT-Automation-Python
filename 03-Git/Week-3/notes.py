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


# git pull

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
