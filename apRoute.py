import DataSource as myds
from flask import Flask,request ,jsonify,render_template,session,url_for,redirect,Blueprint 
import pandas as pd
import plotly as py
import json


#Data
rawData=myds.ChartData()


apRoute = Blueprint('apRoute', __name__,template_folder='templates')


@apRoute.route('/Plotly/',methods=['GET','POST'])
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