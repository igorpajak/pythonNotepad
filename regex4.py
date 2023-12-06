'''
Write a Python program that uses regular expressions 
to replace all occurrences of a substring with another substring.
'''

import re

def new_substring(text: str, old_text: str, new_text: str):
    new_sub = re.sub(old_text, new_text, text)
    return new_sub

text = "I'm a not much experienced programmer"
print(new_substring(text, "not", "very"))
