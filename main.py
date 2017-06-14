import windows
import test_requests
import reddit_scraper
from random import randint
import os
import time

if os.path.isfile("subreddits.cfg"):
    subreddits = []
    data = 0

    readf = open("subreddits.cfg", "r")
    linearray = readf.readlines()
    readf.close()

    with open("subreddits.cfg", "w") as f:
        for line in linearray:
            if (data == 1) and ("Index:" not in line):
                modline = line.replace(" ", "")
                modline = modline.rstrip()
                subreddits += modline.split(",")
            elif data == 2:
                subreddits.pop()
                index = int(line)
                if index >= len(subreddits)-1:
                    index = -1
                f.write(str(index+1))
                break
            elif "Subreddits:" in line:
                data = 1
            elif "Index:" in line:
                data = 2
            f.write(line)
    f.closed

else:
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
