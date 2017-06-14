import praw
import test_requests
import windows
from PIL import Image
import sys
import codecs
from random import randint


def get_page(sub):
    index = randint(0, 45)

    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit(sub)
    posts = subreddit.hot(limit=50)
    for i, submission in enumerate(posts):
        if ('http://i.imgur.com/' in submission.url or "https://i.redd.it/" in submission.url) and i >= index:
            test_requests.save_pic(submission.url)
            image_path = windows.find_path()
            if check_pic(image_path):
                sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
                print(submission.title)
                return submission.url

    for submission in subreddit.hot(limit=50):
        if 'http://i.imgur.com/' in submission.url or "https://i.redd.it/" in submission.url:
            test_requests.save_pic(submission.url)
            image_path = windows.find_path()
            if check_pic(image_path):
                sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
                print(submission.title)
                return submission.url


def check_pic(path):
    pic = Image.open(path)
    width, height = pic.size
    if height > width:
        return False
    if height < 2000:
        return False
    return True
