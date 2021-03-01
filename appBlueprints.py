from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from flask import Blueprint

from apRoute import apRoute


app = Flask(__name__)

@app.route('/')
def index():
        return "Hello index"

#測試 Route
app.register_blueprint(apRoute)

if __name__=='__main__':
    #app.config.from_pyfile('config.py') # from instance     
    app.config.from_object('config')
    SerName=app.config['HOST']
    ipPort=app.config['PORT']
    app.secret_key=app.config['SECRET_KEY']

    app.run(host=SerName,port=ipPort,threaded=True)
