### Debug a problem with a Cloud Deployment and Fix it ###

# Intro/Details:
    # web server: ws01
    # Error 500 (Internal Server Error!)

# Error detection
    # Open the website served by ws01 by typing the external IP address of ws01 in a web browser. 

# What you'll do:
    # Understand what http status code means
    # Learn how to check port status with the netstat command
    # Learn how to manage services with the systemctl command
    # Know how to monitor system resources and identify the root cause of an issue

# Connect to the VM

# Debug the issue
    # systemctl is a utility for controlling the systemd 
    # run
        # sudo systemctl status apache2
        # sudo systemctl restart apache2
        # sudo systemctl status apache2

    # sudo netstat -nlp
    
    # Jot down the PID of the python3 program in your local text editor, which will be used later in the lab.

    # ps -ax | grep python3

    # cat /usr/local/bin/jimmytest.py
    # sudo kill [process-id]
    # sudo systemctl --type=service | grep jimmy
    # sudo systemctl stop jimmytest && sudo systemctl disable jimmytest
    # sudo netstat -nlp

    # sudo systemctl start apache2