# Manual Way of Instantiating an object

# class Apple:
#     color = ""
#     flavor = ""
#
#
# washington = Apple()
# washington.color = "red"
# washington.flavor = "sweet"
#
# print(washington.flavor)


### Awesome Way of Doing it ###
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


washington = Apple("red", "sweet")
print(washington.flavor)
