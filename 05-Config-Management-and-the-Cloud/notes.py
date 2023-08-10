# Week 1 - Automating w/ Config Management
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
