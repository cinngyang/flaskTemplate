# coding=utf-8
#%%
from flask import Flask,request ,jsonify,render_template,session,url_for,redirect
<<<<<<< HEAD
from flask import Blueprint # 將路由抽出
from flask_cors import CORS # Cross Origin Resource Sharing
import os, jwt #JSON Web Token 改用 flask-jwt-extended
=======
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user
from flask_cors import CORS
from flask_wtf.csrf import validate_csrf,CsrfProtect
>>>>>>> dc4dde6668c131c5c55638b80a095ccc88bd8ab0
import pandas as pd
import plotly as py #Chart
import json

<<<<<<< HEAD
from view.webroute import app2 # Routing File
import DataSource as myds #DataModel


#  取得目前文件資料夾路徑
pjdir = os.path.abspath(os.path.dirname(__file__))
print(pjdir)

=======

from myLib import Lexform
import DataSource as myds


csrf = CsrfProtect()
# login manager
login_manager = LoginManager()
login_manager.login_view = 'login'
>>>>>>> dc4dde6668c131c5c55638b80a095ccc88bd8ab0
app=Flask(__name__)

# 安全性設置
CORS(app)
#csrf token
csrf.init_app(app)
login_manager.init_app(app)




class User(UserMixin):    
    """ 繼承 userMixin 特殊權限處理 如 is_administrator """     

    pass
    


#Data
rawData=myds.ChartData()
app.register_blueprint(app2,url_prefix='/api')

# @app.route('/login/',methods=['GET','POST'])
# def login():
#     #設置session
#     session['username'] = 'chin'
#     session['logged_in']=True #寫入session    
#     print('write session')
#     return redirect(url_for('index'))


<<<<<<< HEAD
=======

@login_manager.user_loader 
def user_loader(mail):    
    """
    flask_login 可以隨時取到目前的使用者 id  
    :param email:官網此例將 email當id使用，賦值給予user.id  
    """     

    user = User() 
    user.id=mail    

    return user 
>>>>>>> dc4dde6668c131c5c55638b80a095ccc88bd8ab0

@app.route("/")
def index():
    return render_template('Demo.html')

<<<<<<< HEAD
@app.route('/Demo',methods=['GET','POST'])
def wrsession():    
=======
@app.route('/',methods=['GET','POST'])
@login_required 
def index():
>>>>>>> dc4dde6668c131c5c55638b80a095ccc88bd8ab0

    if current_user.is_active:
        'Logged in as: ' + current_user.id + 'Login is_active:True'
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

<<<<<<< HEAD
    return render_template('Demo.html',elements=elements)
=======
>>>>>>> dc4dde6668c131c5c55638b80a095ccc88bd8ab0

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

@app.route('/login/',methods=['GET','POST'])
def login():

    form = Lexform.LoginForm() 
        
    if request.method == 'POST':   
        # check csrf token
        try:
            validate_csrf(form.csrf_token.data)
            username = form.username.data
            pwd=form.password.data
            
            user = User()
            #  設置id就是 email  
            user.id = username  
            #  這邊，透過login_user來記錄user_id，如下了解程式碼的login_user說明。  
            login_user(user)  
            #  登入成功，轉址               
        
            return redirect(url_for('index'))

        except ValidationError:
            flash('CSRF token error.')
        
    return render_template('login.html', form=form)
    
    # #設置session
    # session['username'] = 'chin'
    # session['logged_in']=True #寫入session        
    # elements=rawData.HtmlItem()
    # return render_template('Grid.html',elements=elements)
    # #return redirect(url_for('index'))


@app.route('/logout') 
def logout():
    """ 
    logout\_user會將所有的相關session資訊給pop掉 
    """ 
    logout_user() 
    return redirect(url_for('login'))

@app.route('/<Project>/<Function>/<Action>',methods=['GET','POST','PUT'])
<<<<<<< HEAD
def dipatch(Project,Function,Action):
    # 動態分配路由 傳入一個 Class 決定 Return  
=======
def dipathc(Project,Function,Action):
    # 動態 Routing
>>>>>>> dc4dde6668c131c5c55638b80a095ccc88bd8ab0
    msg={}
    msg["Project"]=Project
    msg["Function"]=Function
    msg["Action"]=Action
    
    return  jsonify(msg)



<<<<<<< HEAD
    app.run(host=SerName,port=ipPort,threaded=True)
=======

# handle login failed
@app.errorhandler(401)
def page_not_found(e):

    return redirect(url_for('login'))

    if __name__=='__main__':
        #app.config.from_pyfile('config.py') # from instance     
        app.config.from_object('config')
        SerName=app.config['HOST']
        ipPort=app.config['PORT']
        app.secret_key=app.config['SECRET_KEY']

        app.run(host=SerName,port=ipPort,threaded=True)
>>>>>>> dc4dde6668c131c5c55638b80a095ccc88bd8ab0



