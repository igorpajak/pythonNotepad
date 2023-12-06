'''
Write a Python program that uses regular expressions 
to match email addresses.
'''

import re

def match_mail_addresses(text: str):
    pattern = r'^[a-z]*@[a-z]*\.com'
    match = re.match(pattern, text)
    if match:
        return True
    else: 
        return False

mail = match_mail_addresses("igorpajak@gmail.com")
print(mail)