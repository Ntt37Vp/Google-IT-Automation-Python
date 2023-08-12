# ##Puppet rules
# The Puppet rules are present in the init file. The purpose of this script is to append /java/bin to the environment variable $PATH, so that scripts in that directory can be executed without writing the full path.
# The purpose of this rule is to append /java/bin to the environment variable $PATH so that scripts in that directory can be executed without writing the full path.

# #Issue detection
# echo $PATH

# Oops, something is wrong; the main directories used for executing binaries in Linux (/bin and /usr/bin) are missing.
    
# ls /

# Commands like ls, cd, mkdir, rm, and others are just small programs that usually live inside a directory on our systems called /usr/bin.

# export PATH=/bin:/usr/bin

# Alright, now that we have a working PATH, let's look at the rule responsible for this breakage. It's located in the profile module of Puppet's production environment. To look at it, go to the manifests/ directory that contains the Puppet rules by using the following command:


# cd /etc/puppet/code/environments/production/modules/profile/manifests
# cat init.pp

# #Fixing the problem
# sudo nano init.pp
# The line content => "PATH=/java/bin\n" should be changed to content => "PATH=\$PATH:/java/bin\n"
# On top of this, files in the /etc/profile.d directory should only be editable by the root user.
# In order to do this we'll need to change the mode of the file to avoid giving others permission to write the file. In other words, the mode should be 0644 not 0646.

# once fixed, run
# sudo puppet agent -v --test