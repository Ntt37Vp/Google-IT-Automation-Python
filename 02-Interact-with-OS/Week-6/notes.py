# Course 2 Week 6 - Command line

# Interacting with command line
# Basic

# echo
# cat
# chmod
# mkdir
# cd
# ls
# pwd
# cp
# mv
# . shortcut is the cwd
# touch
# permissions:
# rm
# rmdir (for empty dir)

# redirecting streams
# use > to redirect (overrides)
# example below creates hello.txt with 'hello world!' as values
# echo 'hello world!' > hello.txt

# user >> redirect method to APPEND
# example below appends new line to the previous file above
# echo 'hello again, world!' >> hello.txt

# Use 2> to redirect StdErr messages

# Pipes and Pipelines aka piping
# use |
# example below, pipes the output of spider.txt to TR (translate) command that transforms the spaces ' ' , into nl \n
# cat spider.txt | tr ' ' '\n'
# tr command translate or delete char

# SYS module has a usefull STDIN function
# see attached haiku.txt and capitalize.py as examples
# cat haiku.txt | ./capitalize.py


# Bash scripting

# Advanced bash
