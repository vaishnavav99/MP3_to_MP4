from flask import Blueprint, render_template,request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
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
    return "Success"