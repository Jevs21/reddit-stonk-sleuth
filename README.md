# reddit-stonk-sleuth
A program to find people pumping stocks on reddit

## Installation
`pip3 install -r requirements.txt`

Create a file in the root directory named `.env`:
```
CLIENT_ID=F4Kkd2NudL
CLIENT_SECRET=ntUh5sV8oNla33FFb6kHhG
USER_NAME=pm_me_nudes
PASS_WORD=mydogsname
``` 

Fill with your own information (if that wasn't obvious)

## Running
`python3 main.py`

## TODO

Core Function:
- Provide a reddit username and return a reputation score

Reputation Score Metrics:
- Comment (post) Karma
- Link Karma
- Length of account existance
- Has varified account email
- Is a mod of a subreddit
- Consistent account usage
- Amount of posts on investing subredits
    - Karma on posts
    - Diversity of topics of posts
    - Quality of Posts
        - length?
        - NLP?