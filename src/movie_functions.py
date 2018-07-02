from moviepy.editor import *
import os
import random

def createPost(filename):
    voice = AudioFileClip("../tmp/tts/"+filename+".wav")
    image = ImageClip("../tmp/posts/"+filename).set_duration(voice.duration)
    image = image.set_audio(voice)
    image = image.set_position("center", "center")
    while image.h > 1080:
        image = image.resize(0.5)
    #clip = CompositeVideoClip([background, image])

    if not os.path.isdir("../tmp/video"):
        os.mkdir("../tmp/video")
    image.write_videofile("../tmp/video/"+filename+".mp4", fps=24, codec='h264_nvenc')

def combineClips(videofile, musicfile):
    videos = []
    background = ImageClip("../res/backgrounds/" + random.choice(os.listdir("../res/backgrounds/")))

    for file in os.listdir(videofile):
        clip = VideoFileClip(videofile+file)
        clip = clip.set_position("center", "center")
        background = background.set_duration(clip.duration)
        backgroundClip = CompositeVideoClip([background, clip])
        videos.append(backgroundClip)

    final = concatenate_videoclips(videos, method="compose")
    
    music = AudioFileClip("../res/music/" + random.choice(os.listdir("../res/music/")))
    while music.duration < final.duration:
        music = concatenate_audioclips([music, AudioFileClip("../res/music/" + random.choice(os.listdir("../res/music/")))])
    music = music.set_duration(final.duration)
    music = music.volumex(0.1)
    music = CompositeAudioClip([final.audio, music])
    final.audio = music
    final.write_videofile("../output.mp4", fps=24, codec='h264_nvenc')
