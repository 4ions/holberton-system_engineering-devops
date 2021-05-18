#!/us/bin/python3
""" recursive in python """ 

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Return a list containing the titles """
    headers = {'User-agent': 'Unix:0-subs:v1'}
    data = requests.get('http://reddit.com/r/{}/hot.json'.format(subreddit),
                        headers=headers).json().get('data', None)
    if data is None:
        return None
    hot_list += data.get('children', [])
    if data.get('after', None) is not None:
        recurse(subreddit, hot_list, data.get('after', None))
    return hot_list