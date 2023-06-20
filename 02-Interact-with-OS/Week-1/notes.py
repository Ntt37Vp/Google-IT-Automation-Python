# Course 2 - Using Python to Interact with the Operating System (Week 1)


# Getting System Ready
    # PyPi
    # pip

# Use the SHEBANG line for your py scripts
    #!/usr/bin/env python3

# Update Permission to run
    # chmod +x filename.py


### Example 1 - Disk Usage ###
# import shutil
#
# du = shutil.disk_usage("/")
# # print(du)
#
# usage = (du.free / du.total) * 100
# print("Free disk is {:.2f}% ".format(usage))


### Example 2 - CPU Usage ###
import psutil

print(psutil.cpu_percent(0.1))
