from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import secrets


app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert',methods=['POST'])
def convert():
    file=request.files['input']

    x= secrets.token_hex(20)+'.mp3'
    filePath = "./file/"+secure_filename(x)
    file.save(filePath)
    return "Sucess"

if __name__=='__main__':
    app.run(debug=True)