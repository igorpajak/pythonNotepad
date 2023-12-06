'''
Write a Python program that uses regular expressions 
to extract email addresses from a web page.
'''

import re

def extract_email_addresses(html_text):
    pattern = r'<a href="mailto:(\w+@\w+\.\w+)"'
    matches = re.findall(pattern, html_text)
    return matches

html_text = """
<html>
<body>
<a href="mailto:johndoe@example.com">John Doe</a>
<a href="mailto:jane.doe@example.org">Jane Doe</a>
</body>
</html>
"""
email_addresses = extract_email_addresses(html_text)
print(email_addresses)