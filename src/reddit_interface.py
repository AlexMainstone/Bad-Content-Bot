import praw
from urllib.request import urlretrieve
from getpass import getpass
from os import mkdir

#TODO this needs work, clean it and improve it.
def downloadFromSub(c_id, c_secret, upassword, agent, uname, sub, num_posts=10, posts_checked=100):
    reddit = praw.Reddit(client_id=c_id, client_secret=c_secret, password=upassword, user_agent="scraper", username=uname)
    mkdir("../tmp/posts")
    numberofimages = 0
    for submission in reddit.subreddit(sub).hot(limit=posts_checked):
        if "imgur.com/" not in submission.url:
            continue
        if 'http://imgur.com/a/' in submission.url:
            continue
        filename = submission.url.rsplit('/', 1)[-1]
        if '.' not in filename:
            continue
        numberofimages += 1
        print("DOWNLOADED: " + submission.url)
        urlretrieve(submission.url, "../tmp/posts/"+filename)
        if(numberofimages == num_posts):
            break

def inputDownloadFromSub():
    c_id = input("Enter your Reddit client ID: ")
    c_secret = input("Enter your Reddit client Secret: ")
    uname = input("Username: ")
    upassword = getpass("Password: ")
    subreddit = input("Subreddit: /r/")
    downloadFromSub(c_id, c_secret, upassword, "scraper", uname, subreddit)
