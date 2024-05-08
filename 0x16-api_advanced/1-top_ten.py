#!/usr/bin/python3
'''This module prints the 10 hot posts title from Reddit API.'''
import requests


def top_ten(subreddit):
    '''Fetches and outputs the 10 hottest posts title of a subreddit.'''
    reddit_url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    set_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    set_params = {
        "limit": 10
    }
    res = requests.get(reddit_url, headers=set_headers, params=set_params,
                       allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    parsed_res = res.json().get("data")
    [print(i.get("data").get("title")) for i in parsed_res.get("children")]
