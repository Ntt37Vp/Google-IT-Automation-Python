###############################################
### Week 1 - Automating w/ Config Management ##
###############################################
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

#################################
### WEEK 2 - Deploying Puppet ###
#################################

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

# A module -- collection of manifests and associated data (like templates and files)


# Deploying Puppets to Clients
# Puppet nodes -- any system that runs a puppet agent
# Different kinds of nodes are defined, allowing different sets of rule catalogs to apply to different types of machines.
# site.pp -->
# CA to authenticate


# sudo puppet config --section master set autosign true
# then ssh into the target client
# ssh clienthostname
# install the client
# sudo apt install puppet
# set the server config on the client:
# sudo puppet config set server servername.domain.com
# sudo puppet agent -v --test

# on the master
# vim /etc/puppet/code/environments/production/manifest/site.pp

# node webserver.example.com {
#     class {'apache':}
# }
# node default {}

# back to the client
# sudo puppet agent -v --test


# to automate puppet using systemctl instead of manual test
# sudo systemctl enable puppet
# sudo systemctl start puppet
# sudo systemctl status puppet


# Practice Quiz
# using FQDN
# node definition is a category of systems defined in the manifest used to apply different rules to different types of system
# node requests for a cert


# Updating Deployments
# puppet parser validate -- command checks the syntax of the manifest to make sure it's correct.
# --noop means no operation; No Operations mode makes Puppet simulate what it would do without actually doing it.

# rspec-puppet -- spec-puppet tests are there to test the behaviour of Puppet when it compiles your manifests into a catalogue of Puppet resources.
# For example, you might want to test that your apache::vhost defined type creates a file resource with a path of /etc/apache2/sites-available/foo when run on a Debian host.

# require 'spec_helper'

# describe 'logrotate::rule' do
#   let(:title) { 'nginx' }

#   it { is_expected.to contain_class('logrotate::setup') }
# end

# Check that your Puppet manifest conform to the style guide
# install it
# package { 'puppet-lint':
#   ensure   => '1.1.0',
#   provider => 'gem',
# }
# RUN it
# $ puppet-lint /etc/puppet/modules


# Practice Quiz
# Environments in Puppet are used to isolate software in development from software being served to end users.
# No Operations mode makes Puppet simulate what it would do without actually doing it. Simulating manifest evaluation without taking any actions
# RSPEC tests do? check the manifest for specific contents
# Canary env ? As a test env to detect problems before they reach prod
# Ways to check syntax of manifests? run full NOOP, run RSPEC tests, Puppet Parser validate?


########################################
### Week 3 - Automation in the Cloud ###
########################################

# SaaS - think WRS ;)
# PaaS -
# IaaS - barebones

# Capacity

# Practice Quiz
# Public cloud
# Container -
# Amzn Elastic Beanstalk, G App Engine, MS App Service (examples of Managed Web App Platforms)
# Private cloud
# Vertical scaling

# Managing Cloud VMs
# the region, machine type,
# reference imaging
# disk image

# show the os version
# cat /etc/lsb-release

# Save the .service file in etc/systemd/system/
# etc/systemd/system/ is the default systemd directory in many Linux distros, including Red Hat Linux.

# Install GCloud CLI
# https://cloud.google.com/sdk/docs/install-sdk#linux
# sample CLI to run multiple vms from template
# gcloud compute instances create --source-instance-template template-name servername1 servername2...

# Load balancer
# Auto-scaling
# load balancer for DB: memcached & redis
# Orchestration -- is the automated configuration and coordination of complex IT systems and services.
# Cloud Infra as Code (IaC)
# Terraform

# Practice Quiz
# Monitoring & Alertign
# Entry point
# Round Robin
# Autoscaling
# Terraform, CloudFormation (AWS), Azure Resource Mgnr
