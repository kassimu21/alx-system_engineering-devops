#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""

import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for getting hot posts in a subreddit
    url = "https://www.reddit.com/r/{subreddit}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Extract the JSON data from the response
        data = response.json()

        # Check if the subreddit exists
        if 'data' in data and 'children' in data['data']:
            # Iterate over the first 10 posts and print their titles
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print("None - Subreddit not found")
    else:
        print("None - Error fetching data")

# Example usage
top_ten("python")
