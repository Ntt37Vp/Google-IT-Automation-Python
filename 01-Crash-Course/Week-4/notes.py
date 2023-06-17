# Course 1 Week 4 - Strings, Lists & Dicts

###################### STRINGS ###########################
# Strings are Arrays
# String is an IMMUTABLE data type
# Assigning string to a var
# greeting = "Hello World"

# Multi-line string using three quotes
'''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''

# String data type can be sliced, modified and concantenated
# String Methods examples
# upper()
# lower()
# strip()

# Sample function that replaces old domain by new domain
# def replace_domain(email, old_domain, new_domain):
#     if "@" + old_domain in email:
#         index = email.index("@" + old_domain)
#         new_email = email[:index] + "@" + new_domain
#         return new_email
#     return email

# More Strings Methods
# lstrip()
# rstrip()
# endswith()
# isnumeric()
# join()

# Formatting using format()
# def student_grade(name, grade):
# 	return "{} received {}% on the exam".format(name, grade)
# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

# Formatting using f string method
# def student_grade(name, grade):
# 	return f"{name} received {grade}% on the exam"

# print(student_grade("Reed", 80))
# print(student_grade("Paige", 92))
# print(student_grade("Jesse", 85))

# Formatting expression example to limit the digits
# price = 7.50
# with_tax = price * 1.09
# print(price, with_tax)  # will output 7.5 8.175
# # updating using :.2 format
# print("Base price: ${:.2f} With Tax: ${:.2f}".format(price, with_tax))


# String Reference Guide
# String operations

#     len(string) - Returns the length of the string
#     for character in string - Iterates over each character in the string
#     if substring in string - Checks whether the substring is part of the string
#     string[i] - Accesses the character at index i of the string, starting at zero
#     string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted, its value defaults to 0. If j is omitted, the value will default to len(string).

# String methods

#     string.lower() - Returns a copy of the string with all lowercase characters
#     string.upper() - Returns a copy of the string with all uppercase characters
#     string.lstrip() - Returns a copy of the string with the left-side whitespace removed
#     string.rstrip() - Returns a copy of the string with the right-side whitespace removed
#     string.strip() - Returns a copy of the string with both the left and right-side whitespace removed
#     string.count(substring) - Returns the number of times substring is present in the string
#     string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.
#     string.isalpha() - Returns True if there are only alphabetic characters in the string. If not, returns False.
#     string.split() - Returns a list of substrings that were separated by whitespace (a space, tab, or new line)
#     string.split(delimiter) - Returns a list of substrings that were separated by whitespace or a delimiter
#     string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.
#     delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter

# String Operations and Methods
#
#     .format() - String method that can be used to concatenate and format strings.
#
#         {:.2f} - Within the .format() method, limits a floating point variable to 2 decimal places. The number of decimal places can be customized.
#
#     len(string) - String operation that returns the length of the string.
#
#     string[x] - String operation that accesses the character at index [x] of the string, where indexing starts at zero.
#
#     string[x:y] - String operation that accesses a substring starting at index [x] and ending at index [y-1]. If x is omitted, its value defaults to 0. If y is omitted, the value will default to len(string).
#
#     string.replace(old, new) - String method that returns a new string where all occurrences of an old substring have been replaced by a new substring.
#
#     string.lower() - String method that returns a copy of the string with all lowercase characters.

### Study Guide ###
# This function accepts a given string and checks each character of
# the string to see if it is a letter or not. If the character is a
# letter, that letter is added to the end of the string variable
# "forwards" and to the beginning of the string variable "backwards".
# def mirrored_string(my_string):
#     # Two variables are initialized as string data types using empty
#     # quotes. The variable "forwards" will hold the "my_string"
#     # minus any character that is not a letter. The "backwards"
#     # variable will hold the same letters as "forwards", but in
#     # in reverse order.
#     forwards = ""
#     backwards = ""
#
#     # The for loop iterates through each character of the "my_string"
#     for character in my_string:
#
#         # The if-statement checks if the character is not a space.
#         if character.isalpha():
#             # If True, the body of the loop adds the character to the
#             # to the end of "forwards" and to the front of
#             # "backwards".
#             forwards += character
#             backwards = character + backwards
#
#         # If False (meaning the character is not a letter), no action
#         # is needed. This coding approach results prevents any
#         # non-alphabetical characters from being written to the
#         # "forwards" and "backwards" variables. The for loop will
#         # restart until all characters in "my_string" have been
#         # processed.
#
#     # The final if-statement compares the "forwards" and "backwards"
#     # strings to see if the letters are the same both forwards and
#     # backwards. Since Python is case sensitive, the two strings will
#     # need to be converted to use the same case for this comparison.
#     if forwards.lower() == backwards.lower():
#         return True
#     return False
#
#
# print(mirrored_string("12 Noon"))  # Should be True
# print(mirrored_string("Was it a car or cat I saw"))  # Should be False
# print(mirrored_string("'eve, Madam Eve"))  # Should be True

### Study Guide 2 ####
# This function converts measurement equivalents. Output is formatted
# as, "x ounces equals y pounds", with y limited to 2 decimal places.
# def convert_weight(ounces):
#     # Conversion formula: 1 pound = 16 ounces
#     pounds = ounces / 16
#
#     # The result is composed using the .format() method. There are two
#     # placeholders in the string: the first is for the "ounces"
#     # variable and the second is for the "pounds" variable. The second
#     # placeholder formats the float result of the conversion
#     # calculation to be limited to 2 decimal places.
#     result = "{} ounces equals {:.2f} pounds".format(ounces, pounds)
#     return result
#
#
# print(convert_weight(12))  # Should be: 12 ounces equals 0.75 pounds
# print(convert_weight(50.5))  # Should be: 50.5 ounces equals 3.16 pounds
# print(convert_weight(16))  # Should be: 16 ounces equals 1.00 pounds

# Study Guide 3
# This function generates a username using the first 3 letters of a
# user’s last name plus their birth year.
# def username(last_name, birth_year):
#     # The .format() method will use the first 3 letters at index
#     # positions [0,1,2] of the "last_name" variable for the first
#     # {} placeholder. The second {} placeholder concatenates the user’s
#     #  "birth_year" to that string to form a new string username.
#     return ("{}{}".format(last_name[0:3], birth_year))
#
#
# print(username("Ivanov", "1985"))
# # Should display "Iva1985"
# print(username("Rodríguez", "2000"))
# # Should display "Rod2000"
# print(username("Deng", "1991"))
# # Should display "Den1991"

# Study Guide 4
# This function checks a given schedule entry for an old date and, if
# found, the function replaces it with a new date.
# def replace_date(schedule, old_date, new_date):
#     # Check if the given "old_date" appears at the end of the given
#     # string variable "schedule".
#     if schedule.endswith(old_date):
#         # If True, the body of the if-block will run. The variable "n" is
#         # used to hold the slicing index position. The len() function
#         # is used to measure the length of the string "new_date".
#         p = len(old_date)
#
#         # The "new_schedule" string holds the updated string with the
#         # old date replaced by the new date. The schedule[:-p] part of
#         # the code trims the "old_date" substring from "schedule"
#         # starting at the final index position (or right-side) counting
#         # towards the left the same number of index positions as
#         # calculated from len(old_date). Then, the code schedule[-p:]
#         # starts the indexing position at the slot where the first
#         # character of the "old_date" used to be positioned. The
#         # .replace(old_date, new_date) code inserts the "new_date" into
#         # the position where the "old_date" used to exist.
#         new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
#
#         # Returns the schedule with the new date.
#         return new_schedule
#
#     # If the schedule does not end with the old date, then return the
#     # original sentence without any modifications.
#     return schedule
#
#
# print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024"))
# # Should display "Last year’s annual report will be released in March 2024"
# print(replace_date("In April, the CEO will hold a conference", "April", "May"))
# # Should display "In April, the CEO will hold a conference"
# print(replace_date("The convention is scheduled for October", "October", "June"))
# # Should display "The convention is scheduled for June"

###################### LISTS ###########################
# List is a MUTABLE data type
# like Strings, LISTS are sequences

# List Methods
# append() Adds an element at the end of the list
# insert() Adds an element at the specified position
# remove() Removes the first item with the specified value
# pop() Removes the element at the specified position

# enumerate() returns a tuple of the index and the item

# Iterating Over Lists Using Enumerate

# List Comprehension
# multiples = [(x*7) for x in range(1,11)]
# print(multiples)

# languages = ["Python", "Java", "C", "PHP"]
# new_list = [len(lang) for lang in languages]
# print(new_list)


# More List Comprehension Examples
# Simple List Comprehension
# print("List comprehension result:")

# # The following list comprehension compacts several lines
# # of code into one line:
# print([x*2 for x in range(1,11)])

# ### Long form for loop
# print("Long form code result:")

# # The list comprehension above accomplishes the same result as
# # the long form version of the code:
# my_list = []
# for x in range(1,11):
#    my_list.append(x*2)
# print(my_list)


# List Comprehension with Conditional Statement
# print("List comprehension result:")

# # The following list comprehension compacts multiple lines
# # of code into one line:
# print([ x for x in range(1,101) if x % 10 == 0 ])

# ### Long form for loop with nested if-statement
# print("Long form code result:")

# # The list comprehension above accomplishes the same result as
# # the long form version of the code:
# my_list = []
# for x in range(1,101):
#   if x % 10 == 0:
#     my_list.append(x)
# print(my_list)


# Study Guide: Lists Operations and Methods
# Lists and tuples are both sequences and they share a number of sequence operations. The following common sequence operations are used by both lists and tuples:
#     len(sequence) - Returns the length of the sequence.

#     for element in sequence - Iterates over each element in the sequence.

#     if element in sequence - Checks whether the element is part of the sequence.

#     sequence[x] - Accesses the element at index [x] of the sequence, starting at zero

#     sequence[x:y] - Accesses a slice starting at index [x], ending at index [y-1]. If [x] is omitted, the index will start at 0 by default. If [y] is omitted, the len(sequence) will set the ending index position by default.

#     for index, element in enumerate(sequence) - Iterates over both the indices and the elements in the sequence at the same time.


# Coding Skills Exercise 1
# # This block of code changes the year on a list of dates.
# # The "years" list is given with existing elements.
# years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]


# # The variable "updated_years" is initialized as a list data type
# # using empty square brackets []. This list will hold the new list
# # with the updated years.
# updated_years = []

# # The for loop checks each "year" element in the list "years".
# for year in years:

#     # The if-statement checks if the "year" element ends with the
#     # substring "2023".
#     if year.endswith("2023"):

#         # If True, then a temporary variable "new" will hold the
#         # modified "year" element where the "2023" substring is
#         # replaced with the substring "2024".
#         new = year.replace("2023","2024")

#         # Then, the list "updated_years" is appended with the changed
#         # element held in the temporary variable "new".
#         updated_years.append(new)

#     # If False, the original "year" element will be appended to the
#     # the "updated_years" list unchanged.
#     else:
#         updated_years.append(year)


# print(updated_years)
# # Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]


# Coding Skills Exercise 2
# # This list comprehension creates a list of squared numbers (n*n). It
# # accepts two integer variables through the function’s parameters.
# def squares(start, end):

# # The list comprehension calculates the square of a variable integer
# # "n", where "n" ranges from the "start" to "end" variables inclusively.
# # To be inclusive in a range(), add +1 to the end of range variable.
#     return [n*n for n in range(start,end+1)]


# print(squares(2, 3))  # Should print [4, 9]
# print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Coding Skills Exercise 3
# # This block of code also changes the year on a list of dates using a
# # different approach than demonstrated in Skill Group 1. By using a
# # list comprehension, you can see how it is possible to refactor the
# # code to a shorter, more efficient code block.

# # The "years" list is given with existing elements.
# years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# # The list comprehension below creates a new list "updated_years" to
# # hold the command to replace the "2023" substring of the "year"
# # element with the substring "2024". This action will be executed if
# # the last 4 indices of the "year" string is equal to the substring
# # "2023". If false (else), the "year" element will be included in the
# # new list "updated_years" unchanged.
# updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]


# print(updated_years)
# # Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

# Coding Skills Exercise 4
# # This function splits a given string into a list of elements. Then, it
# # modifies each element by moving the first character to the end of the
# # element and adds a dash between the element and the moved character.
# # For example, the element "2two" will be changed to "two-2". Finally,
# # the function converts the list back to a string, and returns the
# # new string.
# def change_string(given_string):

# # Initialize "new_string" as a string data type by using empty quotes.
#     new_string = ""
#     # Split the "given_string" into a "new_list", with each "element"
#     # holding an individual word from the string.
#     new_list = given_string.split()

#     # The for loop iterates over each "element" in the "new_list".
#     for element in new_list:

#         # Convert the list into a "new_string" by using the assignment
#         # operator += to concatenate the following items:
#         # + Each list "element" (starting at index position [1:]),
#         # + a dash "-",
#         # + append the first character of the "element" (using the index
#         # [0]) to the end of the "element", and finally,
#         # + a space " " to separate each "element" in the "new_string".
#         new_string += element[1:] + "-"  + element[0] + " "

#     # Return the list that has been converted back into a string.
#     return new_string


# print(change_string("1one 2two 3three 4four 5five"))
# # Should print "one-1 two-2 three-3 four-4 five-5"


# Coding Skills Exercise 5
# This function accepts a list name and a list of elements, and returns
# a string with the format: "The "list_name" list includes: element1,
# element2, element3".
# def list_elements(list_name, elements):

#     # This task can be completed in a single line of code. The
#     # concatenation of strings, "list_name", and the list "elements" can
#     # occur on the return line. In this case, the string "The " is added
#     # to the "list_name", plus the string " list includes: ", then the
#     # "elements" are joined using a comma to separate each element of the
#     # list.
#     return "The " + list_name + " list includes: " + ", ".join(elements)


# print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))
# # Should print "The Printers list includes: Color Printer, Black and White Printer, 3-D Printer"


#### I asked ChatGPT how to loop through a list of tuples ###
# data = [('Ken', 30, 'Chef'), ('Pat', 35, 'Lawyer'), ('Amanda', 25, 'Engineer')]
#
# for item in data:
#     name, age, profession = item  # Unpack the tuple elements
#
#     # Generate the desired output
#     output = f"{name} is {age} years old and works as {profession}"
#     print(output)


###################### DICTIONARY ###########################
# A Python dictionary is a collection which is ordered** and changeable. No duplicate members.
# It is of course, a Mutable data type.

# Sample dict
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# Access values by referencing the keys
# print(thisdict["year"])

# Use IN keyword to check if the key is on the dict\
# remove elements from a dictionary by using the del keyword.

## Looping through dict
# using .items() method
# for x, y in thisdict.items():
#   print(x, y)
# using .values()
# for x in thisdict.values():
#   print(x)
# using .keys()
# for x in thisdict.keys():
#   print(x)

## DICT Study Guide ##

# Syntax
    # my_dictionary = {keyA:value1,value2, keyB:value3,value4}
# Operations
    # len(dictionary) - Returns the number of items in a dictionary.
    # for key, in dictionary - Iterates over each key in a dictionary.
    # for key, value in dictionary.items() - Iterates over each key, value pair in a dictionary.
    # if key in dictionary - Checks whether a key is in a dictionary.
    # dictionary[key] - Accesses a value using the associated key from a dictionary.
    # dictionary[key] = value - Sets a value associated with a key.
    # del dictionary[key] - Removes a value using the associated key from a dictionary.
# Methods
# dictionary.get(key, default) - Returns the value corresponding to a key, or the default value if the specified key is not present.
# dictionary.keys() - Returns a sequence containing the keys in a dictionary.
# dictionary.values() - Returns a sequence containing the values in a dictionary.
# dictionary[key].append(value) - Appends a new value for an existing key.
#  dictionary.update(other_dictionary) - Updates a dictionary with the items from another dictionary. Existing entries are updated; new entries are added.
# dictionary.clear() - Deletes all items from a dictionary.
# dictionary.copy() - Makes a copy of a dictionary.

## Dict Coding Skills 1 ##
# This function returns the total time, with minutes represented as
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day.
# def sum_server_use_time(Server):
#     # Initialize the variable as a float data type, which will be used
#     # to hold the sum of the total hours and minutes of server usage by
#     # end users in a day.
#     total_use_time = 0.0
#
#     # Iterate through the "Server" dictionary’s key and value items
#     # using a for loop.
#     for key, value in Server.items():
#         # For each end user key, add the associated time value to the
#         # total sum of all end user use time.
#         total_use_time += Server[key]
#
#     # Round the return value and limit to 2 decimal places.
#     return round(total_use_time, 2)
#
#
# FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
#
# print(sum_server_use_time(FileServer))  # Should print 20.1

## Dict Coding Skills 2 ##
# This function receives a dictionary, which contains common employee
# last names as keys, and a list of employee first names as values.
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the
# values ["Maria", "Hugo", "Lucia"] should be converted to a list
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].

# def list_full_names(employee_dictionary):
#     # Initialize the "full_names" variable as a list data type using
#     # empty [] square brackets.
#     full_names = []
#
#     # The outer for loop iterates through each "last_name" key and
#     # associated "first_name" values, in the "employee_dictionary" items.
#     for last_name, first_names in employee_dictionary.items():
#
#         # The inner for loop iterates over each "first_name" value in
#         # the list of "first_names" for one "last_name" key at a time.
#         for first_name in first_names:
#             # Append the new "full_names" list with the "first_name" value
#             # concatenated with a space " ", and the key "last_name".
#             full_names.append(first_name + " " + last_name)
#
#     # Return the new "full_names" list once the outer for loop has
#     # completed all iterations.
#     return (full_names)
#
#
# print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# # Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']


## Dict Coding Skills 3 ##
# This function receives a dictionary, which contains resource
# categories (keys) with a list of available resources (values) for a
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which
# categories (values) each resource (key) belongs to.

# def invert_resource_dict(resource_dictionary):
#   # Initialize a "new_dictionary" variable as a dict data type using
#   # empty {} curly brackets.
#     new_dictionary = {}
#     # The outer for loop iterates through each "resource_group" and
#     # associated "resources" in the "resource_dictionary" items.
#     for resource_group, resources in resource_dictionary.items():
#         # The inner for loop iterates over each "resource" value in
#         # the list of "resources" for one "resource_group" key at a time.
#         for resource in resources:
#             # The if-statement checks if the current "resource" value has
#             # been appended as a key to the "new_dictionary" yet.
#             if resource in new_dictionary:
#                 # If True, then append the "resource_group" as a value to the
#                 # "resource", which is now the key.
#                 new_dictionary[resource].append(resource_group)
#             # If False (else), then add the "resource" as a new key with the
#             # "resource_group" as a value for that key.
#             else:
#                 new_dictionary[resource] = [resource_group]
#     # Return the new dictionary once the outer for loop has completed
#     # all iterations.
#     return(new_dictionary)
#
#
# print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
#         "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# # Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}

