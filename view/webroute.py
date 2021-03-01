from flask import Blueprint,render_template

app2 = Blueprint('api', __name__)

@app2.route('/blue')
def show():
        return "Hello Blueprint app2"

@app2.route('/demo')
def index():
    
    return render_template('index.html')