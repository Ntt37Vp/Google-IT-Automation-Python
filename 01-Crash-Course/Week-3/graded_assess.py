# 1 - Fill in the blanks to print the numbers 1 through 7.
number = 1 # Initialize the variable
while number <= 7: # Complete the while loop condition
    print(number, end=" ")
    number += 1 # Increment the variable

# Should print 1 2 3 4 5 6 7 

###############################

#  2 - Find and correct the error in the for loop below.  The loop should check each number from 1 to 5 and identify if the number is odd or even.  
for number in range(1, 6):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Should print:
# odd
# even
# odd
# even
# odd

###############################

# 3 - Fill in the blanks to complete the function “digits(n)” to count how many digits the given number has. For example: 25 has 2 digits and 144 has 3 digits. 

# import math

# def digits(n):
#     count = 0
#     if n == 0:
#       count += 1
#     while n > 0: # Complete the while loop condition
#         # Complete the body of the while loop. This should include 
#         # performing a calculation and incrementing a variable in the
#         # appropriate order.  
#         count += 1
#         n = math.floor(n / 10) 
#     return count
    
# print(digits(25))   # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000)) # Should print 4
# print(digits(0))    # Should print 1

###############################

# 4 - Fill in the blanks to complete the “multiplication_table” function. This function should print a multiplication table, where each number is the result of multiplying the first number of its row by the number at the top of its column. Complete the range sequences in the nested loops so that “multiplication_table(1, 3)” will print:

def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop+1): 
         # Complete the inner loop range
        for y in range(start, stop+1):
            # Prints the value of "x" multiplied by "y" 
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above


###############################

# 5 - Fill in the blanks to complete the “divisible” function. This function should count the number of values from 0 to the “max” parameter that are evenly divisible (no remainder) by the “divisor” parameter. Complete the code so that a function call like “divisible(100,10)” will return the number “10”.
def divisible(max, divisor):
    count = 0 # Initialize an incremental variable
    for x in range(max): # Complete the for loop
        if x % divisor == 0:
            count += 1 # Increment the appropriate variable
    return count

print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4
print(divisible(144, 17)) # Should be 9
##############################
# 6 - Fill in the blanks to complete the “all_numbers” function. This function should return a space-separated string of all numbers, from the starting   “minimum” variable  up to and including the “maximum” variable that's passed into the function. Complete the for loop so that a function call like “all_numbers(3,6)” will return the numbers “3 4 5 6”.  
def all_numbers(minimum, maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # numbers up to and including the "maximum" value.
    for i in range(minimum, maximum + 1): 

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string = return_string + str(i) + " "

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2,6))  # Should be 2 3 4 5 6
print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1,1)) # Should be -1 0 1
print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
print(all_numbers(0,0))  # Should be 0


###############################
# 7 - What happens when the Python interpreter executes a loop where a variable used inside the loop is not initialized?
# Will produce NameError
##############################
# 8 - How many numbers will this loop print?  Your answer should be only one number.
for sum in range(5):
    sum += sum
    print(sum)
##############################
# 9 - What is the final value of "y" at the end of the following nested loop code? Your answer should be only one number.
for x in range(10):
    for y in range(x):
        print(y)
#############################
# 10 -The following code causes an infinite loop. Can you figure out what’s incorrect and how to fix it?
def count_to_ten():
  # Loop through the numbers from first to last 
  x = 1
  while x <= 10:
    print(x)
    x = 1


count_to_ten()
# Should print:
# 1
# 2
# 3 
# 4
# 5
# 6
# 7
# 8 
# 9
# 10
#############################