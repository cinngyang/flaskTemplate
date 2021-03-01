

# Flask setup

[TOC]

Setup up flask web sit in aws ec2 <br>

![架構](../awsProject/img/flask_gunicorn_nginx.png)<p>

Flask Route method

```python
@app.route('/',methods=['GET','POST','PUT'])
@app.route('/home',methods=['GET','POST','PUT'])
@app.route('/index',methods=['GET','POST','PUT'])
def index():
	#Logic goes here
```

動態 Route 搭配 Class 類似 switch function 回傳

```python
@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    #... Logic goes here
    
```

flask 啟動 multi-Threaded

`app.run(threaded=True)`

## gunicorn 

gunicorn VS uWSGI  - 先使用gunicorn  較為簡單, uWSGI  我踩了很多坑 , Nginx 可以提高 Web Server 性能做到反向代理與負載均衡

gunicorn 寫成 pyfile 執行,程式資料夾內建立 wsgi.py , [參數設定文件](https://docs.gunicorn.org/en/latest/settings.html#settings)

執行綁定 port `gunicorn --bind=0.0.0.0:5005 wsgi:app`

直接執行 --daemon 背景執行

```
sudo gunicorn -w 1 -bind 0.0.0.0:8080 run:app --daemon
```

另用config py 檔執行
```python
# wsgi.py
from app import app #import flaks main File
bind = "0.0.0.0:8080"
workers=2 #
```
command  `gunicorn -c wsgi.py wsgi:app`



## nginx + gunicorn

nginx confing 文件 /etc/nginx/sites-enabled/default 

```text
sudo nano /etc/nginx/sites-enabled/wepub
```

WebPub 設定內容 

```text
server {
    listen 80;
    server_name example.org;

    location / {
    proxy_pass http://0.0.0.0:8080; # gunicorn 設定flask port
    }
 }
```

測試語法是否有錯 `sudo nginx -t` 

 啟動 gunicron & nginx

`curl http://127.0.0.1:8080` 

`ps -ef | grep gunicorn`
`ps -ax | grep app.py #檢查 process`

```
sudo /etc/init.d/nginx start
sudo /etc/init.d/nginx reload
sudo /etc/init.d/nginx stop 
sudo nginx -s quit
sudo nginx -s restart
```

------

[flask 教學](https://hackmd.io/@shaoeChen/HJiZtEngG/https%3A%2F%2Fhackmd.io%2Fs%2FSJmhFpXmf)<br>[flask 教學](https://www.maxlist.xyz/?s=flask)<br>[uwsgi & nginx](https://www.maxlist.xyz/2020/06/17/flask-nginx-uwsgi-on-gcp/)<br>[uwsgi 與 ngix 介紹](https://www.maxlist.xyz/2020/05/06/flask-wsgi-nginx/)<br>[uwsgi & gunicorn 簡單安裝](https://zhuanlan.zhihu.com/p/50857407)<br>[Gunicorn 教學](https://andy6804tw.github.io/2020/04/10/gcp-gunicorn/#2-%E9%87%8D%E6%96%B0%E5%95%9F%E5%8B%95vm)

* CORS
* BluePrints 切出 Route

[Flask  Config 配置](https://spacewander.github.io/explore-flask-zh/5-configuration.html)<br>[javascript fetch](https://developer.mozilla.org/zh-TW/docs/Web/API/Fetch_API/Using_Fetch)<br>[The Art of Flask](https://hackersandslackers.com/flask-routes/)<br>

