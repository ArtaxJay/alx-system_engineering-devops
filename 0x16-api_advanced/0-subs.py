#!/usr/bin/python3
"""A module that queries subreddit on Reddit RESTful API."""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches and returns the total number of
    subscribers on a given subreddit.
    Note: no API authentication needed.
    """
    reddit_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    # set_headers = {
    #    "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    #}
    res = requests.get(reddit_url, headers=set_headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    parsed_res = res.json().get("data")
    return parsed_res.get("subscribers")
