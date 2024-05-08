#!/usr/bin/python3
'''This module fetches and returns all the hot posts from Reddit API.'''
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    '''Fetches and rets a list of all hot posts title.'''
    reddit_url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    set_headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    set_params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    res = requests.get(reddit_url, headers=set_headers, params=set_params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None

    parsed_res = res.json().get("data")
    after = parsed_res.get("after")
    count += parsed_res.get("dist")
    for i in parsed_res.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
