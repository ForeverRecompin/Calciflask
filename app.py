from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    name = 'Calciflask'
    return render_template('add.html', name=name, num1=num1, num2=num2)

@app.route('/sub/<int:num1>/<int:num2>')
@app.route('/sub/<int:num1>/<float:num2>')
@app.route('/sub/<float:num1>/<int:num2>')
@app.route('/sub/<float:num1>/<float:num2>')
def sub(num1, num2):
    name = 'Calciflask'
    return render_template('sub.html', name=name, num1=num1, num2=num2)

@app.route('/mult/<int:num1>/<int:num2>')
@app.route('/mult/<int:num1>/<float:num2>')
@app.route('/mult/<float:num1>/<int:num2>')
@app.route('/mult/<float:num1>/<float:num2>')
def mult(num1, num2):
    name = 'Calciflask'
    return render_template('mult.html', name=name, num1=num1, num2=num2)

@app.route('/div/<int:num1>/<int:num2>')
@app.route('/div/<int:num1>/<float:num2>')
@app.route('/div/<float:num1>/<int:num2>')
@app.route('/div/<float:num1>/<float:num2>')
def div(num1, num2):
    name = 'Calciflask'
    return render_template('div.html', name=name, num1=num1, num2=num2)

@app.route('/')
def index():
    name = 'Calciflask'
    return render_template('index.html', name=name, num1=20, num2=10)

app.run(debug=True, port=5000)
