# CPU Bound
# sudo apt install python3-pip
# pip3 install psutil

# python3
# import psutil

# psutil.cpu_percent()
# psutil.disk_io_counters()
# psutil.net_io_counters()


# Basics rsync command
# rsync [Options] [Source-Files-Dir] [Destination]

# DailySync.py
#!/usr/bin/env python3

# from multiprocessing import Pool
# import multiprocessing
# import subprocess
# import os

# home_path = os.path.expanduser('~')
# src = home_path + "/data/prod/"
# dest = home_path + "/data/prod_backup/"

# if __name__ == "__main__":
#     pool = Pool(multiprocessing.cpu_count())
#     pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))
