### COURSE 2 - Week 2 - Reading & Writing Files ###

# Using open() and close()

# file_var = open("file.txt")

# print(file_var.readline())
# print(file_var.read())
# file.close()


# Using with() block instead
# with open("file.txt") as file_var:
# 	print(file_var.read())
# # no need to close() !!!! :)


# Iterating through files
# with open('file.txt') as file:
# 	for line in file:
# 		print(line.upper())


# Writing Files (remember to use the W mode)
# with open('file2.txt', "w") as file:
#     file.write("It was a dark and stormy night")


# USING OS module
import os

# os.remove('file2.txt')
# os.rename('filename')
# os.path.exists('file3.txt')
