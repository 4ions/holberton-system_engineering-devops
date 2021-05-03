#!/usr/bin/python3
""" Module of API """

import requests
from sys import argv

id_employed = int(argv[1])
name = ""

response = requests.get('https://jsonplaceholder.typicode.com/todos/')
response_users = requests.get('https://jsonplaceholder.typicode.com/users')

for users in response_users.json():
    if users.get('id') == id_employed:
        name = users.get('name')

complet = []
for data in response.json():
    if data.get('userId') == id_employed and data.get('completed'):
        complet.append(data.get('title'))

counter = 0
for count in response.json():
    if count.get('userId') == id_employed:
        counter += 1

print("Employee {} is done with tasks({}/{}):"
      .format(name, len(complet), counter))

for each in complet:
    print("\t {}".format(each))
