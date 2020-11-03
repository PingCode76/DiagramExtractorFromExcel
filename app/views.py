from flask import Flask, render_template, url_for, request, jsonify

from .utils import MainDraw

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    MainDraw()
    return render_template('result.html')

@app.errorhandler(405)
def method_not_allowed(e):
    msg = f"The requested method '{request.method}' is not allowed."
    return jsonify(error=msg), 405

#if __name__ == "__main__":
#    app.run()