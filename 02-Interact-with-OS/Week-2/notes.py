### Course 2 Week 2 - Reading & Writing Files ###

## Using open() and close()

# file_var = open("file.txt")

# print(file_var.readline())
# print(file_var.read())
# file.close()


## Using with() block instead 
with open("file.txt") as file_var:
	print(file_var.read())

# no need to close() !!!! :)

