# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql@127.0.0.1:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

app.config.from_object(Config)

db = SQLAlchemy(app)

redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

@app.route('/')
def index():
    redis_store.set('name', 'banzhang')
    name = redis_store.get('name')

    print(name)
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)