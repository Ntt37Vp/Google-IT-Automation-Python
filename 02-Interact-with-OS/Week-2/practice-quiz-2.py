# 1 -
import os
import csv


# # Create a file with data in it
# def create_file(filename):
#     with open(filename, "w") as file:
#         file.write("name,color,type\n")
#         file.write("carnation,pink,annual\n")
#         file.write("daffodil,yellow,perennial\n")
#         file.write("iris,blue,perennial\n")
#         file.write("poinsettia,red,perennial\n")
#         file.write("sunflower,yellow,annual\n")
#
#
# # Read the file contents and format the information about each row
# def contents_of_file(filename):
#     return_string = ""
#
#     # Call the function to create the file
#     create_file(filename)
#
#     # Open the file
#     with open(filename) as file:
#         # Read the rows of the file into a dictionary
#         file_reader = csv.DictReader(file)
#         # Process each item of the dictionary
#         for row in file_reader:
#             return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
#     return return_string
#
#
# # Call the function
# print(contents_of_file("flowers.csv"))


# 2 -
# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,types\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(filename) as file:
        # Read the rows of the file
        rows = csv.reader(file)
        # Process each row
        for row in rows:
            name, color, types = row
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(name, color, types)

    return return_string


# Call the function
print(contents_of_file("flowers.csv"))

# 3 -
# 4 - same amount of var, both csv.reader and csv.DictReader, instance of reader class must be created
# 5 - If we are analyzing files contents to correctly structure the data, what action are we performing
# Parsing?