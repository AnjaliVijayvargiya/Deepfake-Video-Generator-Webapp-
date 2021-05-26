import os
import sys
from moviepy.editor import *

def extract_frames(movie, times, imgdir):
    clip = VideoFileClip(movie)
    for t in times:
        imgpath = os.path.join(imgdir, 'img'+str(int(t))+'.png')
        clip.save_frame(imgpath, t)

movie = 'media/'+sys.argv[1]
imgdir = 'media/python/frames'
times = 0.1, 0.63, 0.947, 1.2, 3.8, 6.7

extract_frames(movie, times, imgdir)