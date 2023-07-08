import re
import operator

## Exercise 1

# line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"
# re.search(r"ticky: INFO: ([\w ]*) ", line)

# line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
# re.search(r"ticky: ERROR: ([\w ]*) ", line)


## Exercise 2
# fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
# sorted(fruit.items())

# sorted(fruit.items(), key=operator.itemgetter(0))
# sorted(fruit.items(), key=operator.itemgetter(1))
# sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)


## Exercise 3
# nano user_emails.csv
# Full Name, Email Address
# Blossom Gill, blossom@abc.edu
# Hayes Delgado, nonummy@utnisia.com
# Petra Jones, ac@abc.edu
# Oleg Noel, noel@liberomauris.ca
# Ahmed Miller, ahmed.miller@nequenonquam.co.uk
# Macaulay Douglas, mdouglas@abc.edu
# Aurora Grant, enim.non@abc.edu
# Madison Mcintosh, mcintosh@nisiaenean.net
# Montana Powell, montanap@semmagna.org
# Rogan Robinson, rr.robinson@abc.edu
# Simon Rivera, sri@abc.edu
# Benedict Pacheco, bpacheco@abc.edu
# Maisie Hendrix, mai.hendrix@abc.edu
# Xaviera Gould, xlg@utnisia.net
# Oren Rollins, oren@semmagna.com
# Flavia Santiago, flavia@utnisia.net
# Jackson Owens, jackowens@abc.edu
# Britanni Humphrey, britanni@ut.net
# Kirk Nixon, kirknixon@abc.edu
# Bree Campbell, breee@utnisia.net