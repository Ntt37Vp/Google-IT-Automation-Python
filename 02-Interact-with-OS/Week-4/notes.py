# Course 2 - Week 4 - Managing Data and Processes

# Data Streams

# input() function gets user inputs

# I/O Streams
# STDIN
# STDOUT
# STDERR

# A shell is a command line interface used to interact with your operating system.
# Bash is the default Linux shell
# using env command to check Environment Variables
# echo $PATH
# /usr/sbin/temp is NOT listed by default

# using the OS module
# using SYS module
import os
import sys
import subprocess


print("Home: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

# The .get method is quiet helpful

# using the export command to save an ENV VAR
# export FRUIT=Pineapple
# when the script is ran again, the Banana env var will show


# Command line arguments --  parameters that are passed to a program when it started.


# print(sys.argv)
#  The list of arguments are stored in the sys module.
#  exit status is a value returned by a program to the shell

#  to check the EXIT status using $?
# echo $?

# WC command prints out the number of lines, words and chars in a file
# exit status codes
# 0 - success
# 1 - failed


# In Python 3

# Input handles string as a generic string. It does not evaluate the string as a string expression.

# raw_input doesn’t exist, but with some tricky techniques, it can be supported.

# eval() can be used the same as Python 2.


# Python Subprocesses
# import subprocess
# use the .run method to run a linux system command
# example, to run "date" command enter
# subprocess.run(["date"])
