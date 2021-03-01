# coding=utf-8
#%%
from flask import Flask,request ,jsonify,render_template,session,url_for,redirect
from flask_cors import CORS
import pandas as pd
import plotly as py
import json



from myLib import Lexform
import DataSource as myds


app=Flask(__name__)

# 安全性設置
CORS(app)

@app.route('/',methods=['GET','POST'])
def index():

    return render_template('index.html')

@app.route('/base',methods=['GET','POST'])
def base():

    return render_template('base.html')

@app.route('/LineBar',methods=['GET','POST'])
def LineBar():
    return render_template('ChartPlyLieBar.html')

@app.route('/logout',methods=['GET','POST'])
def logout():
    
    return render_template('index.html')

if __name__=='__main__':
    #app.config.from_pyfile('config.py') # from instance     
    app.config.from_object('config')
    SerName=app.config['HOST']
    ipPort=app.config['PORT']
    app.secret_key=app.config['SECRET_KEY']

    app.run(host=SerName,port=ipPort,threaded=True)