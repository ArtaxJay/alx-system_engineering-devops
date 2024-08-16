#!/usr/bin/python3
"""Use the Request mod to get hot articles from Reddit APIs."""
import requests

def recurse(subreddit, hot_list=[]):
    """Parent function."""

    # Initialize 'after' and 'count' inside the function
    after = ""
    count = 0

    def fetch_posts(subreddit, hot_list, after, count):
        """
        Recursively, gets the titles of the articles on a subreddit.
        """
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/artaxjay)"
        }
        params = {
            "after": after,
            "count": count,
            "limit": 100
        }
        res = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if res.status_code == 404:
            return None

        results = res.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for child in results.get("children"):
            hot_list.append(child.get("data").get("title"))

        if after is not None:
            return fetch_posts(subreddit, hot_list, after, count)
        return hot_list

    return fetch_posts(subreddit, hot_list, after, count)
