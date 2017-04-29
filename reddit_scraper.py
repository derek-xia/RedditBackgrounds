import praw
import test_requests
import windows
from PIL import Image
import sys
import codecs


def get_page(sub):
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit(sub)
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
    if width < 2500:
        return False
    return True
