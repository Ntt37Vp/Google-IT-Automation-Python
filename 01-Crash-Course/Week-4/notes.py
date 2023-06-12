# Course 1 Week 4 - Strings, Lists & Dicts

# Strings are Arrays
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

#     string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)

#     string.split(delimiter) - Returns a list of substrings that were separated by whitespace or a delimiter

#     string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.

#     delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter 

