import windows
import test_requests
import reddit_scraper
from random import randint
import time

subreddits = ["earthporn", "architectureporn", "cityporn", "cabinporn"]

index = randint(0, len(subreddits)-1)
link = reddit_scraper.get_page(subreddits[index])

if link is None:
    for sub in subreddits:
        link = reddit_scraper.get_page(sub)
        if link is not None:
            break

if link is None:
    print("No images on reddit :(")
    raise SystemExit

print(link, flush=True)
test_requests.save_pic(link)
windows.set_desktop()
time.sleep(3)
