import re

# 1 - The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.

# def long_words(text):
#   pattern = r"[a-zA-Z]{7,}"
#   result = re.findall(pattern, text)
#   return result

# print(long_words("I like to drink coffee in the morning.")) # ['morning']
# print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
# print(long_words("I never drink tea late at night.")) # []



# 2 - Extracting the PID using regex
# def extract_pid(log_line):
#     regex = r"\[(\d+)\]"
#     result = re.search(regex, log_line)
#     if result is None:
#         return ""
#     return result[1]

# print(extract_pid("Jun 18 04:07:05 combo su(pam_unix)[31791]: session opened for user cyrus by (uid=0)"))
# print(extract_pid("99 elephants in a [cage]"))


#3 - Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.
def extract_pid(log_line):
    regex = r"\[(\d+)\] ([A-Z])"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
