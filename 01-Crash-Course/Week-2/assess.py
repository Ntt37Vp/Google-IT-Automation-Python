def clothing_type(temp):
    if temp > 65:
        clothing = "T-Shirt"
    elif 65 >= temp > 50:
        clothing = "Sweatshirt"
    elif 32 < temp <= 50:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing


print(clothing_type(72))  # Should print T-Shirt
print(clothing_type(55))  # Should print Sweatshirt
print(clothing_type(65))  # Should print Sweatshirt
print(clothing_type(50))  # Should print Jacket
print(clothing_type(45))  # Should print Jacket
print(clothing_type(32))  # Should print Heavy Coat
print(clothing_type(0))  # Should print Heavy Coat


##############################

def complementary_color(color):
    if color == "blue":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "red":
        complement = "green"
    else:
        complement = "unknown"
    return complement


print(complementary_color("blue"))  # Should print orange
print(complementary_color("yellow"))  # Should print purple
print(complementary_color("red"))  # Should print green
print(complementary_color("black"))  # Should print unknown
print(complementary_color("Blue"))  # Should print unknown
print(complementary_color(""))  # Should print unknown

############################################

def make_positive(number):
    if number < __:
        result = ___ * -1
    else:
        result = __
    return result


print(make_positive(-4))   # Should print 4
print(make_positive(0))    # Should print 0
print(make_positive(-.25)) # Should print 0.25
print(make_positive(5))    # Should print 5
