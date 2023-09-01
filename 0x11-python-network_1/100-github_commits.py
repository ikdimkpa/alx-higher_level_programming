#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge
Please list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” You must use the GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    res = requests.get(url)

    history_of_commits = res.json()
    for commit in history_of_commits[:10]:
        sha = commit.get("sha")
        author_of_commit = commit["commit"]["author"]["name"]
        print("{}: {}".format(sha, author_of_commit))
