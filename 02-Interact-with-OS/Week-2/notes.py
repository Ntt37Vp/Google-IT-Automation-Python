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
# os.path.abspath('file.txt')  #returns the absolute path
# os.path.getsize('file')
# os.path.getmtime('file')

# using datetime module to convert the unix time
# import datetime
# timestamp = os.path.getmtime('file.txt')
# print(datetime.datetime.fromtimestamp(timestamp))


# Directories
# os.getcwd()  Returns the current working directory
# os.mkdir()  Creates a directory (with a specified mode)
# os.chdir()  Change the current working directory
# os.rmdir()
# os.listdir()  Returns a list of the names of the entries in a directory
# os.path.join()
# Join two or more pathname components, inserting '/' as needed.
# If any component is an absolute path, all previous path components will be discarded.
# An empty last part will result in a path that ends with a separator.
# By using os.path.join we can concatenate directories in a way that can be used with other os.path() functions.


## Reading and Writing CSV files

# Parsing a file means analyzing its content to correctly structure the data.
# HTML, JSON, CSV are examples

# Using CSV module
# import csv
#
# f = open('country.csv')
# csv_f = csv.reader(f)
# for row in csv_f:
#     Name, Code = row
#     print(f"{Name}, {Code}")
# f.close()


## Generating CSV
