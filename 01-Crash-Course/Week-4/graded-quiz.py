# 1 -
# def format_address(address_string):
#     house_number = ""
#     street_name = ""
#
#     # Separate the house number from the street name.
#     address_parts = address_string.split()
#
#     for address_part in address_parts:
#         # Complete the if-statement with a string method.
#         if address_part.isnumeric():
#             house_number = address_part
#         else:
#             street_name += address_part + " "
#     # Remove the extra space at the end of the last "street_name".
#     street_name = street_name.rstrip()
#
#     # Use a string method to return the required formatted string.
#     return "House number {} on a street named {}".format(house_number, street_name)
#
#
# print(format_address("123 Main Street"))
# # Should print: "House number 123 on a street named Main Street"
#
# print(format_address("1001 1st Ave"))
# # Should print: "House number 1001 on a street named 1st Ave"
#
# print(format_address("55 North Center Drive"))
# # Should print "House number 55 on a street named North Center Drive"


# 2 -
# def string_words(string):
#     # Complete the return statement using both a string operation and
#     # a string method in a single line.
#     return len(string.split())
#
#
# print(string_words("Hello, World")) # Should print 2
# print(string_words("Python is awesome")) # Should print 3
# print(string_words("Keep going")) # Should print 2
# print(string_words("Have a nice day")) # Should print 4

# 3 -
# def sort_distance(distances):
#     distances.sort() # Sort the list
#     distances.sort(reverse = True) # Reverse the order of the list
#     return distances
#
#
# print(sort_distance([2,4,0,15,8,9]))
# # Should print [15, 9, 8, 4, 2, 0]


# 4 - List Compre
# def even_numbers(first, last):
#     return [x for x in range(first, last) if x % 2 == 0]
#
#
# print(even_numbers(4, 14))  # Should print [4, 6, 8, 10, 12]
# print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
# print(even_numbers(2, 7))  # Should print [2, 4, 6]

# 5
# def endangered_animals(animal_dict):
#     result = ""
#     # Complete the for loop to iterate through the key and value items
#     # in the dictionary.
#     for animal, count in animal_dict.items():
#         # Use a string method to format the required string.
#         result += "{}\n".format(animal)
#     return result
#
#
# print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger


# 6
# guests = ["Adam", "Camila", "David", "Jamal", "Charley", "Titus", "Raj", "Noemi", "Sakira", "Chidi"]
#
#
# def setup_guests(guest_list):
#     # loop over the guest list and add each guest to the dictionary with
#     # an initial value of 0
#     result = {}  # Initialize a new dictionary
#     for guest in guest_list:  # Iterate over the elements in the list
#         result[guest] = 0  # Add each list element to the dictionary as a key with
#         # the starting value of 0
#     return result
#
#
# print(setup_guests(guests))
# # Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}


# 7
def setup_gradebook(old_gradebook):
  # Use a dictionary method to create a new copy of the "old_gradebook".
  new_gradebook = old_gradebook.copy()
    # Complete the for loop to iterate over the new gradebook.
  for student in new_gradebook:
    # Use a dictionary operation to reset the grade values to 0.
    new_gradebook[student] = 0
  return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}




# 8
# genre='transcendental'
# print(genre[:-8])
# print(genre[-7:9])

# 9
# music_genres = ["rock", "pop", "country"]
# music_genres.append("blues")
# print(music_genres)

# 10
# teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
# print(teacher_names.values())

