# Course 2 - Week 5 - TESTS

# Software testing is a process of evaluating computer code to determine whether or not it does what you expect it to do.

# Simple Tests
# Manual vs Automated Test
# test cases

# Unit Tests
# the most common type, for small, isolated parts of code

# use the FROM keyword in interpreter
# from filename import function_name
# use the UNITTEST module
# use the TestCase class
# class TestRearrange(unittest.TestCase):
# def test_basic(self):
#     testcase = "Lovelace, Ada"
#     expected = "Ada Lovelace"
#     self.assertEqual(rearrange_name(testcase), expected)
# unittest.main()
# don't forget to add the unittest.main() in the unit test file

# adding different scenarios
# EDGE cases -- are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically work with


# Other Tests Concepts
# Black Box vs White Box (transparent)
# Smoke Test
# Test Suite
# Load testing verifies the behavior of the software remains consistent under conditions of significant load.
# Regression test -- Regression testing is a type of software test used to confirm that a recent program or code change has not adversely affected existing features, by re-executing a full or partial selection test cases.
# Test Driven Dev (TDD)

# Errors & Exceptions
# Try-Except construct
# Raising our OWN errors : USE RAISE ERROR_NAME
# example:
# def validate_num(minlen):
#     if minlen < 1:
#         raise ValueError("number must be at least 1")
#     return "OK!"


# validate_num(0)
# when ran, the output is
# ValueError: number must be at least 1
# the ASSERT keyword is used to produce a message when a conditional is false.
# The assert keyword is used when debugging code.
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
# example:
# x = "hello world"

# # if condition returns True, then nothing happens:
# assert x == "hello world"

# # if condition returns False, AssertionError is raised:
# assert x == "goodbye world"

# the AssertRaises function inside the unittest module
# pass the Error first, then the Function, then the params

# Summary of Erros and Exceptions
# Raise allows you to throw an exception at any time.
# Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
# The standard library documentation is kind of unclear.
# Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.

# In the try clause, all statements are executed until an exception is encountered.
# Except is used to catch and handle the exception(s) that are encountered in the try clause.
# Other interesting Exception handling readings:
# https://doughellmann.com/posts/python-exception-handling-techniques/


# Jupyter notebook activity notes
# unittest.main(argv = ['first-arg-is-ignored'], exit = False)
# import unittest

# class TestCompiler(unittest.TestCase):

#     def test_basic(self):
#         testcase = "The best preparation for tomorrow is doing your best today."
#         expected = ['b', 'a', 'a', 'b', 'a']
#         self.assertEqual(LetterCompiler(testcase), expected)


# Lab notes
# Revised Guess() function
# def Guess(participants):
#     my_participant_dict = {}
#     for participant in participants:
#         my_participant_dict[participant] = random.randint(1, 9)
#     try:
#         if my_participant_dict['Larry'] == 9:
#             return True
#     except:
#         return None
