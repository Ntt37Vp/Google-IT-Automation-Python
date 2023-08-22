### Graded Lab -  Scale and convert images using PIL ###

# Download the file
# curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie

# ls
# unzip images.zip
# ls ~/images

# The images received are in the wrong format:
# .tiff format
# Image resolution 192x192 pixel (too large)
# Rotated 90° anti-clockwise

# The images required for the launch should be in this format:

# .jpeg format
# Image resolution 128x128 pixel
# Should be straight


## Install Pillow ##
# pip3 install pillow

## Write a Python script ##


##
# chmod +x <script_name>.py
# ./<script_name>.py
# ls /opt/icons
