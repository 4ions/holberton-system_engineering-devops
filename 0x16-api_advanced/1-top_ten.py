#!/usr/bin/python3
""" Reddit API """
import requests


def top_ten(subreddit):
    '''Get top 10 hot posts'''
    headers = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get('http://reddit.com/r/{}/hot.json'
                            .format(subreddit),
                            headers=headers)
    children = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not children:
        return None

    for data in children[0:10]:
        print(data.get('data', {}).get('title'))
