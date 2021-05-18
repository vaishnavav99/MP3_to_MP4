from flask import Blueprint, render_template,request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os, sys
from moviepy.editor import *
import secrets
from . import db

main = Blueprint('main', __name__,static_folder='static',template_folder='templates')


@main.route('/')
def index():
    return render_template('index.html')
    

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
    
@main.route('/profile',methods=['POST'])
def profile_post():
    file=request.files['input']
    x= secrets.token_hex(20)+'.mp3'
    filePath = "./file/"+secure_filename(x)
    file.save(filePath)
    audio = AudioFileClip(filePath)
    image = VideoFileClip('./file/2.mp4').set_duration(audio.duration) 
    video = image.set_audio(audio)
    outfile = f"{os.path.splitext('1')}_with_image.mp4" # 1.
    video.write_videofile(outfile, fps=1)
    return outfile
