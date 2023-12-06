'''
Write a Python program that uses regular expressions 
to find phone numbers in a text string.
'''

import re

def is_correct_number(number: str):
    pattern = r'^\+48[0-9]{9}$'
    match = re.match(pattern, number)
    if match:
        return True
    else:
        return False

phone_num = is_correct_number("+48785530404")
print(phone_num)