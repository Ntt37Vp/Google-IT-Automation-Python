# Course 2 Week 3 - RegEx
# Using re module
# REMEMBER TO ALWAYS rawstring r WHEN DEALING WITH REGEX IN PYTHON

import re


# RegEx 
    # A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
    # RegEx can be used to check if a string contains the specified search pattern.

# Regex functions
    # re.search -- returns the first matching value
    # re.findall -- returns all possible values
    # re.split
    # re.sub
    # re.match


# txt = "The rain in Spain [12345] que sera whatever"
# regex = r"\[(\d+)\]"
# result= re.search(regex, txt)
# print(result[1]) 

# Basic matching with GREP
    # for example, search word 'thon' in dict 
    # grep thon /usr/share/dict/words

# SPECIAL (Reserved) characters
    # . dot matches any char (wildcard type)
    # ^ crets starts with
    # $ dollar ends with

# Basic RegEx
    # print(re.search(r"p.ng", "penguin"))
    # output is
    # <re.Match object; span=(0, 4), match='peng'>

# Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
# def check_aei (text):
#     result = re.search(r"a.e.i", text)
#     return result != None

# print(check_aei("academia")) # True
# print(check_aei("aerial")) # False
# print(check_aei("paramedic")) # True


# Wildcards and Char classes using bracket []
# allow letters a to z, A to Z, 0 to 9
    # [a-z]
    # [A-Z]
    # [0-9]

# Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.

# def check_punctuation (text):
#   result = re.search(r"[,.:;?!]", text)
#   return result != None

# print(check_punctuation("This is a sentence that ends with a period.")) # True
# print(check_punctuation("This is a sentence fragment without a period")) # False
# print(check_punctuation("Aren't regular expressions awesome?")) # True
# print(check_punctuation("Wow! We're really picking up some steam now!")) # True
# print(check_punctuation("End of the line")) # False

# Search for a Char that is NOT a letter use [^a-zA-Z]
    # print(re.search(r"[^a-zA-Z]", "!@0123!A"))
    # output is
    # <re.Match object; span=(0, 1), match='!'>

# Search for either using | pipe
    # print(re.search(r"cat|dog", "I like cats."))
    # <re.Match object; span=(7, 10), match='cat'>


## REPITITION QUALIFIERS
# ex: Find "Py" followed by any number of char then ends with n
    # print(re.search(r"py.*n", "pygmalion"))
    # <re.Match object; span=(0, 9), match='pygmalion'>
    
# Python implementation of repitition uses plus + and question ?
    # + (plus) One or more occurrences
    # ? (question) Zero or one occurrences


# Escaping characters using the back slash \
    # \W Returns a match where the string DOES NOT contain any word characters
    # \s Returns a match where the string contains a white space character


# Advanced RegEx
# Capturing Groups using parenthesis ()
# example, capture LastName, FirstName
# result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
## print(result)
## <re.Match object; span=(0, 13), match='Lovelace, Ada'>
# using groups() method
# print(result.groups())
# print(result[0])
# print(result[1])
# print(result[2])
# fullname = "{} {}".format(result[2], result[1])
# print(fullname)

## let's create a function to see it in action!
# def rearrange_name(name):
#     result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
#     if result is None:
#         return name
#     else:
#         return "{} {}".format(result[2], result[1])


# print(rearrange_name("Lovelace, Ada"))
# print(rearrange_name("Ada Lovelace"))
# print(rearrange_name("Kennedy, John F."))
# print(rearrange_name("John F. Kennedy"))


# More repetitive qualifiers
    # numeric repetition qualifiers using curly brackets {}
    # example, to match a string with 5 letters
    # print(re.findall(r"[a-zA-Z]{5}", "the quick brown fox jumps over the lazy dog"))
    # # output is
    # ['quick', 'brown', 'jumps']


# Special sequences Quicklist
    # \b Returns a match where the specified characters are at the beginning or at the end of a word
    # \d Returns a match where the string contains digits (numbers from 0-9)
    # \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)



# Splitting and Replacing
    # example, split or separate sentences that ends with period, question mark and exclamation
    # word_list = re.split(r"[.?!]", "One sentence. Another one? And last one!")
    # print(word_list)
    # output is
    # ['One sentence', ' Another one', ' And last one', '']

    # to include the captured punctuation use the parenthesis
    # word_list2 = re.split(r"([.?!])", "One sentence. Another one? And last one!")
    # print(word_list2)
    # output is
    # ['One sentence', '.', ' Another one', '?', ' And last one', '!', '']

    # The SUB() function
    # The sub() function replaces the matches with the text of your choice:
    # example, let's replace the email address with REDACTED

    # message = re.sub(r"[\w.%+-]+@[\w.-]+", "<REDACTED>", "Received an email from des_nuts69@myemail.com")
    # print(message)
    # output is
    # Received an email from <REDACTED>

