# 1 - Fill in the blanks to complete the is_palindrome function. This function checks if a given string is a palindrome. A palindrome is a string that contains the same letters in the same order, whether the word is read from left to right or right to left. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". The function should ignore blank spaces and capitalization when checking if the given string is a palindrome. Complete this function to return True if the passed string is a palindrome, False if not.
# def is_palindrome(input_string):
#     # Two variables are initialized as string date types using empty
#     # quotes: "reverse_string" to hold the "input_string" in reverse
#     # order and "new_string" to hold the "input_string" minus the
#     # spaces between words, if any are found.
#     new_string = ""
#     reverse_string = ""
#
#     # Complete the for loop to iterate through each letter of the
#     # "input_string"
#     for letter in input_string:
#
#         # The if-statement checks if the "letter" is not a space.
#         if letter != " ":
#             # If True, add the "letter" to the end of "new_string" and
#             # to the front of "reverse_string". If False (if a space
#             # is detected), no action is needed. Exit the if-block.
#             new_string += letter
#             reverse_string = letter + reverse_string
#
#     # Complete the if-statement to compare the "new_string" to the
#     # "reverse_string". Remember that Python is case-sensitive when
#     # creating the string comparison code.
#     if new_string.lower() == reverse_string.lower():
#         # If True, the "input_string" contains a palindrome.
#         return True
#
#     # Otherwise, return False.
#     return False
#
# print(is_palindrome("Never Odd or Even"))  # Should be True
# print(is_palindrome("abc"))  # Should be False
# print(is_palindrome("kayak"))  # Should be True


# 2 - Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
# def convert_distance(miles):
#     km = miles * 1.6
#     result = "{} miles equals {:.1f} km".format(miles, km)
#     return result
#
# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

# 3 - If we have a string variable named Weather = "Rainfall", which of the following will print the substring "Rain" or all characters before the "f"?

# 4 - Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."

# def nametag(first_name, last_name):
#     return("{} {}.".format(first_name, last_name[0]))
#
#
# print(nametag("Jane", "Smith"))
# # Should display "Jane S."
# print(nametag("Francesco", "Rinaldi"))
# # Should display "Francesco R."
# print(nametag("Jean-Luc", "Grand-Pierre"))
# # Should display "Jean-Luc G."


# 5 - The replace_ending function replaces a specified substring at the end of a given sentence with a new substring. If the specified substring does not appear at the end of the given sentence, no action is performed and the original sentence is returned. If there is more than one occurrence of the specified substring in the sentence, only the substring at the end of the sentence is replaced. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).
# def replace_ending(sentence, old, new):
#     # Check if the old substring is at the end of the sentence
#     if sentence.endswith(old):
#         # Using i as the slicing index, combine the part
#         # of the sentence up to the matched string at the
#         # end with the new string
#         i = len(old)
#         new_sentence = sentence[:-i] + sentence[-i:].replace(old, new)
#         return new_sentence

#     # Return the original sentence if there is no match
#     return sentence


# print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april"))
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April"))
# # Should display "The weather is nice in April"

############## Practice Quiz -- LISTS #############
# 1 - Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# ___

# print(newfilenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# 2- Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
# def pig_latin(text):
#   say = ""
#   # Separate the text into words
#   words = text.split()
#   for word in words:
#     # Create the pig latin word and add it to the list
#     say += word[1:] + "ay "
#     # Turn the list back into a phrase
#   return say

# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

# 5 - The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, … For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
# def group_list(group, users):
#   members = group + ": " + ", ".join(users)
#   return members

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"


# 6 - The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that.
# def guest_list(guests):
#     for guest in guests:
#         name, age, profession = guest
#         print("{} is {} years old and works as {}".format(name, age, profession))


# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
#            ('Amanda', 25, "Engineer")])

# # Click Run to submit code
# """
# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
# """

##### PRACTICE QUIZ: DICT #####
# 1 receive a dict
def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + '@' + domain)
    return emails


print(email_list({
    "gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
    "yahoo.com": ["barbara.gordon", "jean.grey"],
    "hotmail.com": ["bruce.wayne"]
}))

# 2 - func receives a dict with group names with list of users.
# users can belong to multi group


# def groups_per_user(group_dictionary):
#     user_groups = {}
#     for group, users in group_dictionary.items():
#         for user in users:
#             if user in user_groups:
#                 user_groups[user].append(group)
#             else:
#                 user_groups[user] = [group]
#     return user_groups
#
#
# print(groups_per_user({
#     "local": ["admin", "userA"],
#     "public": ["admin", "userB"],
#     "administrator": ["admin"]
# }))


# 3
# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)


# 4 -

# 5 -
