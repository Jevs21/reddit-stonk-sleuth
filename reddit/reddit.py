import os
from datetime import datetime
import asyncpraw as praw
import dotenv
import re

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASS_WORD')

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent="StonkScript by u/evs21",
                     username=USERNAME)

class Edge():
    def __init__(self, src, dest, path):
        self.src = src
        self.dest = dest
        self.path = path
    
    def __repr__(self):
        return f"{self.src.author} -> {self.dest.author}"


class Post():
    def __init__(self, post_type, title, auth, url, date, content, score, source):
        self.post_type = post_type
        self.title = title
        self.author = auth
        self.url = url
        self.date = date
        self.date_obj = datetime.fromtimestamp(date)
        self.content = content
        self.score = int(score)
        self.source = source
    
    def __repr__(self):
        date_str = self.date_obj.strftime("%b %d %I:%M %p")
        return f"{self.title} [{self.score}]\n{date_str}\n/u/{self.author} in {self.source}\nhttps://reddit.com{self.url}"


def get_id_from_message(msg):
    # Example link: https://www.reddit.com/r/Baystreetbets/comments/lq8zwl/are_profits_getting_a_little_too_easy/
    half = msg.split("reddit.com/r/", 1)
    parts = half[1].split("/comments/", 1)
    p_id = parts[1].split("/", 1)[0]
    return p_id


async def get_reputation_from_post(msg):
    post_id = get_id_from_message(msg)
    # interactions = []

    source = "baystreetbets"
    sub = await reddit.submission(post_id)
    await sub.load()
    author = await reddit.redditor(sub.author.name)
    await author.load()
    
    date_obj = datetime.fromtimestamp(author.created_utc)
    time_existed = datetime.now() - date_obj
    ret_str = f"USER: {author.name}\n"
    ret_str += f"Account Age: {time_existed.days} days.\n"
    ret_str += f"Post Karma: {author.comment_karma}\n"
    ret_str += f"Link Karma: {author.link_karma}\n"
    ret_str += f"Is Mod? {author.is_mod}\n"
    
    tickers = {}
    async for submission in author.submissions.new():
        # print(submission.title)
        content = submission.selftext
        if len(content) > 0:
            words = content.split(" ")
            for w in words:
                if re.match("([$]*[A-Z]{2,4}[.]?[A-Z]{0,3})", w):
                    if w in tickers:
                        tickers[w] += 1
                    else:
                        tickers[w] = 0

    ret_str += "Common Ticker Mentions: "
    count = 0
    for key in tickers:
        if tickers[key] > 2:
            count += 1
            ret_str += f" {key}({tickers[key]}) "

    if count == 0:
        ret_str += "None."
    
    return ret_str 

    # dest_post = Post(
    #     "post",
    #     sub.title, 
    #     sub.author.name, 
    #     sub.permalink, 
    #     sub.created_utc, 
    #     sub.selftext, 
    #     sub.score, 
    #     source
    # )
    
    # comments = await sub.comments()
    # for c in comments:
    #     src_post = Post(
    #         "comment",
    #         "",
    #         c.author.name,
    #         c.permalink,
    #         c.created_utc,
    #         c.body,
    #         c.score,
    #         source
    #     )
        
    #     interactions.append(Edge(src_post, dest_post, ""))
    
    # for i in interactions:
    #     print(i)
    
    return f"{sub.author.name} = {rep_score}"

    