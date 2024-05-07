#!/usr/bin/python3
"""
function to print top 10
"""


import requests


def top_ten(subreddit):
    """
    fucntion to query the reddit api
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    r = requests.get(url, allow_redirects=False)
    if r.status_code < 300:
        r_json = r.json()
        children = r_json.get('data').get('children')
        for child in children:
            print(child.get('data').get('title'))
    else:
        print('None')
