#!/usr/bin/python3

"""
Run this with:

python3 -m http.server --cgi
"""

import cgitb
cgitb.enable(format="text")

from helper import get_input, json

# user_input = get_input()

test_data = {
  "firstName": "John",
  "lastName": "Smith",
  "age": 27
  }

# Will give you JSON output in the console
print(json.dumps(test_data))

'''
if user_input:
    print("User-input", user_input)
else:
    print(test_data)
'''