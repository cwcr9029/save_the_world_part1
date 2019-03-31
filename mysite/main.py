from flask import Flask, render_template, request, flash, g, session
from rsa_pin import power, encrypt
import string
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/',methods=('GET','POST'))
def hello_world():
    return render_template('index.html')

@app.route('/encrypt',methods=('GET','POST'))
def encrypted():
    g.errors = []
    error = False
    if request.method == 'POST':
        password = request.form['pwd']
        print(password[0])
        if password[0]=='0':
            error = True
            g.errors.append('Your pin should not start with 0')
        for char in password:
            if char in string.ascii_letters or char in string.punctuation or len(password)!=6:
                g.errors.append('Your pin needs to be 6 digits long,with digits from 0-9')
                error = True
                break
        if error:
            return render_template('index.html')
        session['password'] = password
        message, public, private = encrypt(password)
        session['message'] = message
        session['public'] = public
        session['private'] = private
    return render_template('decrypt.html',message=session['message'],public=session['public'],private=session['private'])

@app.route('/check',methods=('GET','POST'))
def check():
    if request.method == 'POST':
        answer = request.form['answer']
        if answer ==  session['password']:
            return render_template('right.html')
        else:
            return render_template('wrong.html')

@app.route('/info')
def info():
    return render_template('rsainfo.html')