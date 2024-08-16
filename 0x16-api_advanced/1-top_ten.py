#!/usr/bin/python3
"""Use the Request mod to get hot posts frm Reddit APIs."""
import requests


def top_ten(subreddit):
    """
    Outputs/prints the titles of the first 10 hot posts on a subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/artaxjay)"
    }
    params = {
        "limit": 10
    }
    res = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    results = res.json().get("data")
    [print(child.get("data").get("title")) for child in 
                            results.get("children")]
