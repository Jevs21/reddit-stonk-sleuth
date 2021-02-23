import sys
import os
import praw
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

class Post():
    def __init__(self, title, auth, url, date, content, score, source):
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




def main():
    reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent="StonkScript by u/evs21",
                     username=USERNAME)

    interactions = []

    submissions = reddit.subreddit("baystreetbets").hot(limit=10)
    for sub in submissions:
        
        for c in sub.comments:
            new_int = [sub.author, c.author]
            new_int.sort()
            interactions.append(new_int)

        new_post = Post(
            sub.title, 
            sub.author.name, 
            sub.permalink, 
            sub.created_utc, 
            sub.selftext, 
            sub.score, 
            "baystreetbets",
            interactions
        )
    
    

    #     dd_posts.append(new_post)
    #     print(new_post)
        
    
    # for dd in sorted(dd_posts, key=lambda post: post.date, reverse=True):
    #     print(dd, "\n")



if __name__ == '__main__':
    main()
    
