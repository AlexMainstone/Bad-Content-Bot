from shutil import rmtree
import os

import movie_functions
import image_to_wav
import reddit_interface

#create directory for temporary data
os.mkdir("../tmp/")

# Prompt user for login, download images from subreddit
reddit_interface.inputDownloadFromSub()

#Process each image
for file in os.listdir("../tmp/posts"):
    image_to_wav.processImage(file)
    movie_functions.createPost(file)

movie_functions.combineClips("../tmp/video/", "../res/music/")

#Delete temporary data
rmtree("../tmp")
