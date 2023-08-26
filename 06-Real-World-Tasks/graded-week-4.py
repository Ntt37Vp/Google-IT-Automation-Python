### Week 4 Graded Lab -  Automate updating catalog information  ###

# What you'll do

#     Write a script that summarizes and processes sales data into different categories
#     Generate a PDF using Python
#     Automatically send a PDF by email
#     Write a script to check the health status of the system

## Part 1 - Fetching supplier data ##
# ls ~/
# sudo chmod +x ~/download_drive_file.sh
# ./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz

# You have now downloaded a file named supplier-data.tar.gz containing the supplier's data.
# Let's extract the contents from this file using the following command:
# tar xf ~/supplier-data.tar.gz

# This creates a directory named supplier-data, that contains subdirectories named images and descriptions.
# ls ~/supplier-data


# The subdirectory images contain images of various fruits, while the descriptions subdirectory has text files containing the description of each fruit. You can have a look at any of these text files using cat command.

# cat ~/supplier-data/descriptions/007.txt


# Working with supplier images
# nano ~/changeImage.py

# TODO : fix script
# Grant executable permissions to the changeImage.py script.
# ./changeImage.py
# check:
# file ~/supplier-data/images/003.jpeg


## Part 2 - Uploading images to web server ##
