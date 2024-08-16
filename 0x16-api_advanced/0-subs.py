#!/usr/bin/python3
"""Use the Request module to get total Subreddit Subcribers from Reddit APIs."""
import requests


def number_of_subscribers(subreddit):
    """If successful, get total subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/artaxjay)"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    results = res.json().get("data")
    return results.get("subscribers")
