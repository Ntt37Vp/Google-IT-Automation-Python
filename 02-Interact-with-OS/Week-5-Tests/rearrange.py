#!/usr/bin/env python3
import re


# Sample script from Week 3 - RegEx

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    else:
        return "{} {}".format(result[2], result[1])


# print(rearrange_name("Lovelace, Ada"))
# print(rearrange_name("Ada Lovelace"))
# print(rearrange_name("Kennedy, John F."))
# print(rearrange_name("John F. Kennedy"))
