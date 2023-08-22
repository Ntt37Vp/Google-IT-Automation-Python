### Week 1 - Manipulating Images ###
# PyPi
# Pillow

# For example, if we wanted to resize an image and save the new image with a new name, we could do it with:
from PIL import Image
im = Image.open("example.jpg")
new_im = im.resize((640, 480))
new_im.save("example_resized.jpg")

# In this case, we're using the resize method that returns a new image with the new size, and then we save it into a different file.
# Or, if we want to rotate an image, we can use code like this:
im = Image.open("example.jpg")
new_im = im.rotate(90)
new_im.save("example_rotated.jpg")

# This method also returns a new image that we can then use to create the new rotated file.
# Because the methods return a new object, we can even combine these operations into just one line that rotates, resizes, and saves:
im = Image.open("example.jpg")
im.rotate(180).resize((640, 480)).save("flipped_and_resized.jpg")


### Week 2 - Interacting with Web Services ###
