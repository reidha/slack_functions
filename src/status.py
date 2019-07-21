import json
import os
import requests


def update_status(text: str, emoji: str) -> requests.models.Response:
    data = {
        "token": os.environ['SLACK_USER_TOKEN'],
        "user": os.environ['SLACK_USER_ID'],
        "profile": json.dumps({
            "status_text": text,
            "status_emoji": emoji
        })
    }
    res = requests.post("https://slack.com/api/users.profile.set", params = data)
    return res

if __name__ == '__main__':
    res = update_status("Testing", ":octocat:")
    print(res)
