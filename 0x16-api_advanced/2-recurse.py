#!/usr/bin/python3
"""
function to recursively fetch data
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    function to recursivley fetch data
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    headers = {'User-Agent': 'MyBot'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code == 200:

        data = res.json()['data']

        if data['after'] is not None:
            recurse(subreddit, hot_list, data['after'])

        for post in data['children']:
            hot_list.append(post['data']['title'])

        return hot_list
    else:
        return None
