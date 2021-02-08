#%%
from flask import Flask,request ,jsonify,render_template
from flask_cors import CORS
import pandas as pd


app=Flask(__name__)
CORS(app)


@app.route('/',methods=['GET','POST'])
def index():

    return render_template('index.html')

SerName='0.0.0.0'
ipPort=8080
debug=True

if __name__=='__main__':
    app.run(host=SerName,port=ipPort,debug=debug)


