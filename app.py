#%%
from flask import Flask,request ,jsonify,render_template
from flask_cors import CORS
import pandas as pd
import plotly as py
import json

import DataSource as myds


app=Flask(__name__)
CORS(app)


rawData=myds.ChartData()

@app.route('/',methods=['GET','POST'])
def index():

    elements=rawData.HtmlItem()
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




SerName='0.0.0.0'
ipPort=8080
debug=True

if __name__=='__main__':
    app.run(host=SerName,port=ipPort,debug=debug)


