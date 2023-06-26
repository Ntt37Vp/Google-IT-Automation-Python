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
import os

print("Home: " + os.environ.get("HOME"))
print("SHELL: " + os.environ.get("SHELL", ""))
