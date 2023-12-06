'''
Write a Python program that uses regular expressions 
to check if a string contains only lowercase letters.
'''

import re

def if_lowercase(string: str):
    pattern = r'^[a-z]*$'
    match = re.match(pattern, string)
    if match:
        return True
    else:
        return False
    
exp = if_lowercase("abEsadlo")
print(exp)