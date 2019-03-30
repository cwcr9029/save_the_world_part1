from flask import Flask, render_template, request
from rsa_pin import power, encrypt

app = Flask(__name__)

@app.route('/',methods=('GET','POST'))
def hello_world():
    return render_template('index.html')

@app.route('/encrypt',methods=('GET','POST'))
def encrypted():
    if request.method == 'POST':
        password = request.form['pwd']
        message, public, private = encrypt(password)
    return render_template('encrypt.html',message=message,public=public,private=private)
