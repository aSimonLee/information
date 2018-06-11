# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@127.0.0.1:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'

app.config.from_object(Config)

db = SQLAlchemy(app)



@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)