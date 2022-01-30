#!/usr/bin/python3

import cgitb
cgitb.enable()

from helper import get_input, json

user_input = get_input()

test_data = {
  "firstName": "John",
  "lastName": "Smith",
  "age": 27
  }

print(test_data)

if user_input:
    print("User-input", user_input)
else:
    print(test_data)