# music_video_with_image.py
import os, sys
from moviepy.editor import *

audio = AudioFileClip('./file/1.mp3')
image = VideoFileClip('./file/2.mp4').set_duration(audio.duration) 

video = image.set_audio(audio)
outfile = f"{os.path.splitext('1')}_with_image.mp4" # 1.

video.write_videofile(outfile, fps=1)