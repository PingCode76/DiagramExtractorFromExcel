from flask import Flask
from flask import Flask, render_template
from flask import Flask, url_for

#from .utils import find_content

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

#@app.route('/index/') ( définir plusieurs routes pour une vue )
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/')
def result():
    #param = request.args.get('param')
    return render_template('result.html',
                            #param=param,
                            user_name='Sacha',
                            user_image=url_for('static', filename='tmp/cover_111823112767411.jpg'))

@app.route('/result/<result_id>/')
def resultId():
    #result_id = request.args.get('result_id')
    return render_template('result.html',
                            #result_id=result_id,
                            user_name='Sacha',
                            user_image=url_for('static', filename='tmp/cover_111823112767411.jpg'))
    # or return '%s' % content_id
    # use utils.py function : description = find_content(gender).descripti


if __name__ == "__main__":
    app.run()