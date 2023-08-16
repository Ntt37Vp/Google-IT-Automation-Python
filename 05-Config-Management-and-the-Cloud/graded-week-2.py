# Deployment Using Puppet

# Puppet rules
# The VM named puppet is the Puppet Master 
#  The VM named linux-instance is a client 

# The manifests used for the production environment are located in the directory:
# /etc/puppet/code/environments/production/manifests, which contains a site.pp 

# Install packages
# There's a module named packages on the Puppet VM instance
# cd /etc/puppet/code/environments/production/modules/packages
# cat manifests/init.pp

# Now, add an additional resource in the same init.pp file within the path
# /etc/puppet/code/environments/production/modules/packages, ensuring the golang package 
# gets installed on all machines that belong to the Debian family

# sudo chmod 646 manifests/init.pp
# if $facts[os][family] == "Debian" {
#     package { 'golang':
#         ensure => installed,
#     }
# }

# The complete init.pp file would now look similar to the below file:
# class packages {
#    package { 'python-requests':
#        ensure => installed,
#    }
#    if $facts[os][family] == "Debian" {
#      package { 'golang':
#        ensure => installed,
#      }
#   }
# }

# we will also need to ensure that the nodejs package is installed on machines that belong to the RedHat family
# add the ff:
# if $facts[os][family] == "RedHat" {
#   #Resource entry
# }

# The complete init.pp file should now look like this:
# class packages {
#    package { 'python-requests':
#        ensure => installed,
#    }
#    if $facts[os][family] == "Debian" {
#      package { 'golang':
#        ensure => installed,
#      }
#   }
#    if $facts[os][family] == "RedHat" {
#      package { 'nodejs':
#        ensure => installed,
#      }
#   }
# }


##We will be connecting to linux-instance using its external IP address. 
# To fetch the external IP address of linux-instance, use the following command:
# gcloud compute instances describe linux-instance --zone=us-west4-c --format='get(networkInterfaces[0].accessConfigs[0].natIP)'

# SSH into the client vm

# sudo puppet agent -v --test

# check if the puppet manifest works. This VM belongs to Debian family so we should see GOLANG installed
# apt policy golang


###Fetch machine information###
# It's now time to navigate to the machine_info module in our Puppet environment. 
# In the Puppet VM terminal, navigate to the module using the following command:
# cd /etc/puppet/code/environments/production/modules/machine_info
# cat manifests/init.pp

# sudo chmod 646 manifests/init.pp
# the complete manifest file should be
# class machine_info {
#   if $facts[kernel] == "windows" {
#        $info_path = "C:\Windows\Temp\Machine_Info.txt"
#    } else {
#        $info_path = "/tmp/machine_info.txt"
#    }
#  file { 'machine_info':
#        path => $info_path,
#        content => template('machine_info/info.erb'),
#    }
# }


###Puppet Templates####
# Templates are either written in
# Embedded Puppet (EPP) or
# Embedded Ruby (ERB) 

# cat templates/info.erb
# sudo chmod 646 templates/info.erb
# add this last line
# Network Interfaces: <%= @interfaces %>

# to check if it worked, go back to Linux-Instance client VM
# sudo puppet agent -v --test
# cat /tmp/machine_info.txt


###Reboot machine###
# we will be creating a new module named reboot, that checks if a node has been online for more than 30 days. 
# If so, then reboot the computer.

# To do that, you'll start by creating the module directory.
# On Puppet MasterMaster VM
# sudo mkdir -p /etc/puppet/code/environments/production/modules/reboot/manifests
# cd /etc/puppet/code/environments/production/modules/reboot/manifests
# sudo touch init.pp
# sudo nano init.pp
# create the init file
# class reboot {
#   if $facts[kernel] == "windows" {
#     $cmd = "shutdown /r"
#   } elsif $facts[kernel] == "Darwin" {
#     $cmd = "shutdown -r now"
#   } else {
#     $cmd = "reboot"
#   }
# }
# also add:
# if $facts[uptime_days] > 30 {
#         exec { 'reboot':
#            command => $cmd,
#         }
#     }

# The complete reboot/manifests/init.pp should now look like this:
# class reboot {
#   if $facts[kernel] == "windows" {
#     $cmd = "shutdown /r"
#   } elsif $facts[kernel] == "Darwin" {
#     $cmd = "shutdown -r now"
#   } else {
#     $cmd = "reboot"
#   }
#   if $facts[uptime_days] > 30 {
#     exec { 'reboot':
#       command => $cmd,
#      }
#    }
# }

# add to site.pp
# sudo nano /etc/puppet/code/environments/production/manifests/site.pp 
# node default {
#    class { 'packages': }
#    class { 'machine_info': }
#    class { 'reboot': }
# }

# Test, Run the client on linux-instance VM terminal:
# sudo puppet agent -v --test