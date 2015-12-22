from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    context = {'name':'Calciflask', 'title_desc': 'Addition', 'num1':num1, 'num2':num2, 'result':(num1 + num2), 'operator':'+'}
    return render_template('operation.html', **context)

@app.route('/sub/<int:num1>/<int:num2>')
@app.route('/sub/<int:num1>/<float:num2>')
@app.route('/sub/<float:num1>/<int:num2>')
@app.route('/sub/<float:num1>/<float:num2>')
def sub(num1, num2):
    context = {'name':'Calciflask', 'title_desc': 'Subtraction', 'num1':num1, 'num2':num2, 'result':(num1 - num2), 'operator':'-'}
    return render_template('operation.html', **context)

@app.route('/mult/<int:num1>/<int:num2>')
@app.route('/mult/<int:num1>/<float:num2>')
@app.route('/mult/<float:num1>/<int:num2>')
@app.route('/mult/<float:num1>/<float:num2>')
def mult(num1, num2):
    context = {'name':'Calciflask', 'title_desc': 'Multiplication', 'num1':num1, 'num2':num2, 'result':(num1 * num2), 'operator':'x'}
    return render_template('operation.html', **context)

@app.route('/div/<int:num1>/<int:num2>')
@app.route('/div/<int:num1>/<float:num2>')
@app.route('/div/<float:num1>/<int:num2>')
@app.route('/div/<float:num1>/<float:num2>')
def div(num1, num2):
    context = {'name':'Calciflask', 'title_desc': 'Division', 'num1':num1, 'num2':num2, 'result':(num1 / num2), 'operator':'/'}
    return render_template('operation.html', **context)

@app.route('/')
def index():
    name = 'Calciflask'
    return render_template('index.html', name=name, num1=20, num2=10)

app.run(debug=True, port=5000)
