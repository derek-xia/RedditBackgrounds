dependencies:
requests
os
ctypes
praw (don't forget to put praw.ini secret code etc)
pillow

need to do:
add error messages
add more domains to download from
set a image size / aspect ratio range
add a list of url ids so that it doesn't repeat the same images


6/13/17
added config file for inputs for list of subreddits to choose from
added counter in that file that loops across the subreddits in order, not random
added a random way to pick posts from top 50 in subreddit

4/20/17
added i.redd.it
random subreddit selection