# flaskTemplate
建置 flask 的樣板網頁<br>

 Route

```python
@app.route('/',methods=['GET','POST','PUT'])
@app.route('/home',methods=['GET','POST','PUT'])
@app.route('/index',methods=['GET','POST','PUT'])
def index():
	#Logic goes here
```

動態 Route

```python
@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    #... Logic goes here
    
```



ja

[flask 教學](https://hackmd.io/@shaoeChen/HJiZtEngG/https%3A%2F%2Fhackmd.io%2Fs%2FSJmhFpXmf)<br>[Flask  Config 配置](https://spacewander.github.io/explore-flask-zh/5-configuration.html)<br>[javascript fetch](https://developer.mozilla.org/zh-TW/docs/Web/API/Fetch_API/Using_Fetch)<br>[The Art of Flask](https://hackersandslackers.com/flask-routes/)<br>

