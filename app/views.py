from flask import Flask, render_template, url_for, request, jsonify

from .utils import MainDraw

app = Flask(__name__)
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    MainDraw()
    return render_template('result.html')
