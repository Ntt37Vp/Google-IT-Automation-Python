# ##Week 1 - Automating w/ Config Management
# Config Management -> Node
# Puppet (think Ansible ;)
# IaC (infra as code)

# in Puppet:
# "Resources" - it's the basic unit for modeling the config
# "Class" -
# "Provider" - aka the package manager?

# A class with no parameters
# class base::linux {
#   file { '/etc/passwd':
#     owner => 'root',
#     group => 'root',
#     mode  => '0644',
#   }
#   file { '/etc/shadow':
#     owner => 'root',
#     group => 'root',
#     mode  => '0440',
#   }
# }

# A class with parameters
# class apache (String $version = 'latest') {
#   package {'httpd':
#     ensure => $version, # Using the class parameter from above
#     before => File['/etc/httpd.conf'],
#   }
#   file {'/etc/httpd.conf':
#     ensure  => file,
#     owner   => 'httpd',
#     content => template('apache/httpd.conf.erb'), # Template from a module
#   }
#   service {'httpd':
#     ensure    => running,
#     enable    => true,
#     subscribe => File['/etc/httpd.conf'],
#   }
# }

# Domain-specific lang
# Variables are preceded with $ sign
# Conditional statements
# Facts - variables that represent char of a system
# Declarative languages - like Puppet DSL
# Procedural languages - like Python or C
# idempotent action - can be performed over & over again w/o changing the system after the 1st time the action was ran
# EXEC runs commands for the users
# use ONLYIF for commands that are not idempotent such as mv, example:
# exec { 'move example file':
#     command => 'mv /home/user/example.txt /home/user/Desktop',
#     onlyif => 'test -e /home/user/example.txt',
# }

# Test and Repair paradigm (makes sure the next steps are necessary and are not already in place)

### WEEK 2 - Deploying Puppet ###
# sudo apt install puppet-master
# create a puppet file "Manifest" ends with .pp

# vim tools.pp
# package { 'htop':
#  ensure => present,
# }

# Apply
# sudo puppet apply -v tools.pp

# CATALOG -- list of rules that are generated for one specific computer once the server has evaluated all var, cond and func

# When declaring resources initially, we type the resource type in lowercase. When we reference a resource relationship from another file, we capitalize the resource name being referenced.

# Metadata is data about data, and in this case, often takes the form of installation and compatibility information.

# New functions added after installing a new module can be found in the lib folder in the directory of the new module.  

