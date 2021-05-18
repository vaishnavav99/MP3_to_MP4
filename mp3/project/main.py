from flask import Blueprint, render_template,request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import secrets
from . import db
import os, sys
from moviepy.editor import *

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
    x= secrets.token_hex(20)
    y=x+'.mp3'
    filePath = "./file/"+secure_filename(y)
    file.save(filePath)
        
    audio = AudioFileClip(filePath)
    image = VideoFileClip('./2.mp4').set_duration(audio.duration) 

    video = image.set_audio(audio)
    z=x+'.mp4'
    outfile = "./file/"+z

    video.write_videofile(outfile, fps=1)
    return outfile