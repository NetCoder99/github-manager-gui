import os

from flask import Flask, render_template, redirect, request, url_for, flash, session

from logging.config import dictConfig

from flask_cors import CORS

import constants

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] :: %(levelname)s :: %(module)s :: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

template_dir = os.path.join(os.getcwd(), "base", "templates")
static_dir   = os.path.join(os.getcwd(), "base", "static")
app = Flask(__name__,
            template_folder=template_dir,
            static_folder=static_dir)

app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

CORS(app)

@app.route("/favicon.ico")
def favicon():
    return ''

@app.route("/health")
def health():
    return {
        'status'   : 'up',
        'app_name' : constants.APP_NAME,
        'app_version' : constants.APP_VERsION
    }

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    app.logger.info(f'index was called')
    return render_template('index.html', current_user=None)

if __name__ == '__main__':
    app.run(debug=True)