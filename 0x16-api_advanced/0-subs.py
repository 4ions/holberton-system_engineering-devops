#!/usr/bin/python3
""" Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ Number of subscribers """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get('https://reddit.com/r/{}/about.json'
                            .format(subreddit), headers=headers)

    if response.status_code != 200:
        return 0
    return response.json().get('data', {}).get('subscribers', 0)
