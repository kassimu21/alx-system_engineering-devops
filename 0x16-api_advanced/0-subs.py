#!/usr/bin/python3
"""
function to get number of subreddit subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """
    fucntion to query the reddit api
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    r = requests.get(url)
    if r.status_code < 300:
        r_json = r.json()
        subscriber_count = r_json.get('data').get('subscribers')
        return (subscriber_count)
    else:
        return (0)
