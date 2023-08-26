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
# built-in email module

# We'll start by using the email.message.EmailMessage class to create an empty email message.
# in python cli
# >>> from email.message import EmailMessage
# >>> message = EmailMessage()
# >>> print(message)
# >>> sender = "me@example.com"
# >>> recipient = "you@example.com"
# >>> message['From'] = sender
# >>> message['To'] = recipient
# >>> print(message)
# >>> message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
# >>> print(message)
# >>> body = """Hey there!
# ...
# ... I'm learning to send emails using Python!"""
# >>> message.set_content(body)


# Adding Attachments
# >>> import os.path
# >>> import mimetypes
# >>> attachment_path = "/tmp/example.png"
# >>> attachment_filename = os.path.basename(attachment_path)
# >>> mime_type, _ = mimetypes.guess_type(attachment_path)
# >>> print(mime_type)


# >>> mime_type, mime_subtype = mime_type.split('/', 1)
# >>> print(mime_type)
# >>> print(mime_subtype)


# The SMTPLIB module #
# Let's create a smtplib.SMTP object and try to connect to the local machine.
# >>> mail_server = smtplib.SMTP('localhost')
# >>> mail_server = smtplib.SMTP_SSL('smtp.example.com')
# mail_server.set_debuglevel(1)
# >>> import getpass
# >>> mail_pass = getpass.getpass('Password? ')
# Password?
# >>> mail_server.login(sender, mail_pass)
# (235, b'2.7.0 Accepted')


### Generating PDFs ###

# using ReportLab
# >>> from reportlab.platypus import SimpleDocTemplate
# >>> report = SimpleDocTemplate("/tmp/report.pdf")
# >>> from reportlab.platypus import Paragraph, Spacer, Table, Image
# >>> from reportlab.lib.styles import getSampleStyleSheet
# >>> styles = getSampleStyleSheet()
# >>> report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
# >>> report.build([report_title])

# adding tables
# >>> table_data = []
# >>> for k, v in fruit.items():
# ...   table_data.append([k, v])
# ...
# >>> print(table_data)
# [['elderberries', 1], ['figs', 1], ['apples', 2], ['durians', 3], ['bananas', 5], ['cherries', 8], ['grapes', 13]]

# >>> report_table = Table(data=table_data)
# >>> report.build([report_title, report_table])


# # or something like this
# >>> from reportlab.lib import colors
# >>> table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
# >>> report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
# >>> report.build([report_title, report_table])

# # Adding Graphics to our PDFs
# >>> from reportlab.graphics.shapes import Drawing
# >>> from reportlab.graphics.charts.piecharts import Pie
# >>> report_pie = Pie(width=3*inch, height=3*inch)

# >>> report_pie.data = []
# >>> report_pie.labels = []
# >>> for fruit_name in sorted(fruit):
# ...   report_pie.data.append(fruit[fruit_name])
# ...   report_pie.labels.append(fruit_name)
# ...
# >>> print(report_pie.data)
# [2, 5, 8, 3, 1, 1, 13]
# >>> print(report_pie.labels)
# ['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']
