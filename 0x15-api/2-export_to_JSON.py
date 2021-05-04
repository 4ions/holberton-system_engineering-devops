#!/usr/bin/python3
""" Export to csv """


import json
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

    dic = []
    for each in resp.json():
        new_dict = {}
        new_dict['task'] = each.get('title')
        new_dict['completed'] = each.get('completed')
        new_dict['username'] = name
        dic.append(new_dict)

    json_dict = {}
    json_dict[u_id] = dic
    with open('{}.json'.format(u_id), 'w') as jsonfile:
        json.dump(json_dict, jsonfile)
