#%%
from flask import Flask,request ,jsonify,render_template,session,url_for,redirect
from flask import Blueprint # 將路由抽出
from flask_cors import CORS # Cross Origin Resource Sharing
import os, jwt #JSON Web Token 改用 flask-jwt-extended
import pandas as pd
import plotly as py #Chart
import json

from view.webroute import app2 # Routing File
import DataSource as myds #DataModel


#  取得目前文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))
print(pjdir)

app=Flask(__name__)
CORS(app)


rawData=myds.ChartData()
app.register_blueprint(app2,url_prefix='/api')

# @app.route('/login/',methods=['GET','POST'])
# def login():
#     #設置session
#     session['username'] = 'chin'
#     session['logged_in']=True #寫入session    
#     print('write session')
#     return redirect(url_for('index'))



@app.route("/")
def index():
    return render_template('Demo.html')

@app.route('/Demo',methods=['GET','POST'])
def wrsession():    

    elements=rawData.HtmlItem()
    name=session.get('username')
    logged_in=session.get('username')
    
    print(f"name:{name} logged_in:{logged_in}")

    return render_template('Demo.html',elements=elements)

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
def dipatch(Project,Function,Action):
    # 動態分配路由 傳入一個 Class 決定 Return  
    msg={}
    msg["Project"]=Project
    msg["Function"]=Function
    msg["Action"]=Action
    
    return  jsonify(msg)


if __name__=='__main__':
    # app.config.from_pyfile('config.py') # from instance     
    app.config.from_object('config')
    SerName=app.config['HOST']
    ipPort=app.config['PORT']
    app.secret_key=app.config['SECRET_KEY']

    app.run(host=SerName,port=ipPort,threaded=True)



