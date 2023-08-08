# Troubleshooting is the process of identifying, analyzing, and solving problems.
# Debugging is the process of identifying, analyzing, and removing bugs in a system.
# Debuggers

# Reproduction case

# Steps:
# Gather all avail info
# Finding Root Cause

# ltrace
# wireshark
# tcpdump

# iotop
# iostat
# vmstat
# iftop
# nice

# heisenbug -- aka the observer effect

# Week 2
# A profiler is a tool that measures the resources that our code is using, giving us a better understanding of what's going on.
# gprof for C
# cProfile for Python

# Testing the speed of the py and sh
# use the TIME command
# pprofile3
# kcachegrind

# I/O Bound
# CPU Bound

# SQLite
# full pledged SQL
# memcached

# Concurrency in Python
# "From concurrency" import futures
# futures module has Executor
# ThreadPoolExecutor -- threads
# ProcessPoolExecutor -- uses processes in parallel computing

# Python concurrency:
# threading
# asyncio
# multiprocessing


# WEEK 3 - Crashing Programs

# Check logs
# memtest86 to check RAM
# linux:varlog
# win:event viewer

# linux: Strace
# win: process monitor
# mac: Dtruss

# A WRAPPER is a function or program that provides a compatibility layer between two functions or programs.
# A CONTAINER allows the application to run in its own environment without interfering with the rest of the system.

# A PBD file is used to generate debugging symbols using Microsoft compilers.
# Dr. Memory can assist in finding out if invalid operations are occurring in a program running on Windows or Linux.

# ulimit -c unlimited
# is used to create a core file that stores information related to a crash.

# gdb
# gdb command will debug a core dump and stop where the failure was recorded.
# backtrace -- The backtrace command can be used to show a summary of the function calls that were used to the point where the failure occurs.

# Debugging Python
# pdb3 filename.py
# utf8-sig

# QUIZ
# breakpoints!
# ram replacement!
# off-by-one!
# printf!
# core files!

# WEEK 4 - Managing Computer Resources
# A memory leak, happens when a chunk of memory that's no longer needed is not released.
# C & C++ uses Garbage collector to manage memory alloc
