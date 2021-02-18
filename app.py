# coding=utf-8
#%%
from flask import Flask,request ,jsonify,render_template,session,url_for,redirect
from flask_cors import CORS
import pandas as pd
import plotly as py
import json

import DataSource as myds


app=Flask(__name__)
CORS(app)


rawData=myds.ChartData()

@app.route('/login/',methods=['GET','POST'])
def login():
    #設置session
    session['username'] = 'chin'
    session['logged_in']=True #寫入session    
    print('write session')
    return redirect(url_for('index'))


@app.route('/',methods=['GET','POST'])
def index():    

    elements=rawData.HtmlItem()
    name=session.get('username')
    logged_in=session.get('username')
    
   # print(f"name:{name} logged_in:{logged_in}")

    return render_template('index.html',elements=elements)

@app.route('/Plotly/',methods=['GET','POST'])
def LineBar():
    
    # 測試 Server Size 傳入Data , Clinet 繪圖
    df=rawData.LinChat()
    xRaw=df.loc[:,'Month'].tolist()
    Qty=df.loc[:,'Qty'].tolist()
    Ratio=df.loc[:,'Ratio'].tolist()
    SerData ={'x': xRaw, 'Qty': Qty, 'Ratio': Ratio}


    pie = { 'values': [100, 50, 30, 20],'labels': ['香蕉', '蘋果', '水梨', '草莓'],
        'type': 'pie'}

    graphs = [
        dict( data=[pie],
            layout=dict(width='50%',height='50%'))]
    # 序列化
    graphJSON = json.dumps(graphs, cls=py.utils.PlotlyJSONEncoder)
    
    return render_template('ChartPlyLieBar.html',SerData=SerData,graphJSON =graphJSON )

@app.route('/<Project>/<Function>/<Action>',methods=['GET','POST','PUT'])
def dipathc(Project,Function,Action):
    msg={}
    msg["Project"]=Project
    msg["Function"]=Function
    msg["Action"]=Action
    
    return  jsonify(msg)


if __name__=='__main__':
    #app.config.from_pyfile('config.py') # from instance     
    app.config.from_object('config')
    SerName=app.config['HOST']
    ipPort=app.config['PORT']
    app.secret_key=app.config['SECRET_KEY']

    app.run(host=SerName,port=ipPort,threaded=True)



