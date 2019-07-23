import json
import os
import random
import requests
import time


TEXT = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
EMOJI = [":mario-jump:", ":octocat:", ":rainbow-flog:", ":mario-dash:", ":thumbsup_all:", ":100:"]


def update_status(text: str, emoji: str) -> requests.models.Response:
    data = {
        "token": os.environ['SLACK_USER_TOKEN'],
        "user": os.environ['SLACK_USER_ID'],
        "profile": json.dumps({
            "status_text": text,
            "status_emoji": emoji
        })
    }
    res = requests.post("https://slack.com/api/users.profile.set", params=data)
    return res


def update_status_randomly() -> requests.models.Response:
    return update_status(random.choice(TEXT), random.choice(EMOJI))

def run(sec: int) -> None:
    while True:
        update_status_randomly()
        time.sleep(sec)


if __name__ == '__main__':
    res = update_status("Testing", ":octocat:")
    print(res)
