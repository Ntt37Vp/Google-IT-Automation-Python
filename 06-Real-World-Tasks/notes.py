### Week 1 - Manipulating Images ###
# PyPi
# Pillow
# import yaml

# For example, if we wanted to resize an image and save the new image with a new name, we could do it with:
# from PIL import Image
# im = Image.open("example.jpg")
# new_im = im.resize((640, 480))
# new_im.save("example_resized.jpg")

# In this case, we're using the resize method that returns a new image with the new size, and then we save it into a different file.
# Or, if we want to rotate an image, we can use code like this:
# im = Image.open("example.jpg")
# new_im = im.rotate(90)
# new_im.save("example_rotated.jpg")

# This method also returns a new image that we can then use to create the new rotated file.
# Because the methods return a new object, we can even combine these operations into just one line that rotates, resizes, and saves:
# im = Image.open("example.jpg")
# im.rotate(180).resize((640, 480)).save("flipped_and_resized.jpg")


### Week 2 - Interacting with Web Services ###
# Data serialization is the process of taking an in-memory data structure, like a Python object,
# and turning it into something that can be stored on disk or transmitted across a network.

# interacting w/ JSON
# import json
# with open('people.json', 'w') as people_json:
#     json.dump(people, people_json, indent=2)

# A Python object can be converted it into a JSON string by using the json.dumps() method.
# Use the indent parameter to define the numbers of indents
# The load() method does the inverse of the dump() method. It deserializes JSON from a file into basic Python objects.
# The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file.


# interacting w/ YAML (Yet Another Markup Language)
# import yaml
# with open('people.yaml', 'w') as people_yaml:
#     yaml.safe_dump(people, people_yaml)


## the REQUESTS module ##
# import requests
#
# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)

# requests.methodname(params)
# methods:
# get
# post
# delete
# head
# patch
# put
# request
# raise_for_status() -- will raise HTTPError exception only if response was not OK

# Web Frameworks
# Django
# Flask


### Week 3 - Sending Emails ###
# SMTP and MIME are the email standards

# from email.message import EmailMessage
# message = EmailMessage()
# print(message)


# Sending using smtplib module
