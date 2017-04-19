import windows
import test_requests
import reddit_scraper

subreddits = ["architectureporn", "earthporn", "cityporn"]

for sub in subreddits:
    link = reddit_scraper.get_page(sub)
    if link is not None:
        break

if link is None:
    print("No images on reddit :(")
    raise SystemExit
print(link)
test_requests.save_pic(link)
windows.set_desktop()
