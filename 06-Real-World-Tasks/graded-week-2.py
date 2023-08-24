### Week 2 - Graded Lab -   Process Text Files with Python Dictionaries and Upload to Running Web Service ###

# For this lab, a Django web server corpweb is already configured under /projects/corpweb directory.
# You can check it out by visiting the external IP address of the corpweb VM.
# The external IP address can be found in the connection details panel.
# Enter the corpweb external IP address in a new separate browser tab.

# In this section, you'll write a Python script that will upload the feedback automatically without having to turn it into a dictionary.
# cd /data/feedback
# ls
# Use the cat command to view these files. For example:
# cat 007.txt

# They're all written in the same format (i.e. title, name, date, and feedback).

# Now, navigate back to the home directory and create a Python script named run.py using the following command:
# cd ~
# nano run.py

# add shebang
#! /usr/bin/env python3
# import os
# import requests

# List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
# Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.
#

# You should now have a list that contains all of the feedback files from the path /data/feedback. Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
# Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
# Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.
# Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on. You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.

# Save the run.py script file by pressing Ctrl-o, the Enter key, and Ctrl-x.

# chmod +x ~/run.py
# ./run.py

#######################


import os
import requests

'''
List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.
'''
dir = "/data/feedback/"
for file in os.listdir("/data/feedback/"):
    '''
    You should now have a list that contains all of the feedback files from the path /data/feedback. 
    Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
    '''
    format = ["title", "name", "date", "feedback"]

    '''
    Now, you need to have a dictionary with keys and their respective values (content from feedback files). 
    This will be uploaded through the Django REST API.
    '''
    content = {}

    with open('{}/{}'.format(dir, file), 'r') as txtfile:
        counter = 0
        for line in txtfile:
            line = line.replace("\n", "")
            content[format[counter]] = line.strip('\n')
            counter += 1

    '''
    Use the Python requests module to post the dictionary to the company's website. 
    Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. 
    Replace <corpweb-external-IP> with corpweb's external IP address.
    '''
    response = requests.post("http://35.225.95.53/feedback/", json=content)

    '''
    You can print the status_code and text of the response objects to check out what's going on. 
    You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
    '''
    if not response.ok:
        raise Exception("POST failed! | Status code: {} | File: {}".format(
            response.status_code, file))
    print("Feedback added!")
