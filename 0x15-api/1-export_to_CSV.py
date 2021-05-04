#!/usr/bin/python3
""" Export to csv """


import csv
import requests
from sys import argv

if __name__ == '__main__':

    u_id = int(argv[1])
    name = ""
    resp = requests.get('https://jsonplaceholder.typicode.com/todos/')
    res_users = requests.get('https://jsonplaceholder.typicode.com/users')

    for user in res_users.json():
        if user.get('id') == u_id:
            name = user.get('username')
    with open('{}.csv'.format(u_id), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for each in resp.json():
            if each.get('userId') == u_id:
                writer.writerow([u_id, name,
                                each.get('completed'), each.get('title')])
