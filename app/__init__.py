from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from sqlalchemy import or_, and_

# model
from sqlalchemy.dialects.mysql import BIGINT

# views
from flask import render_template, jsonify, request

# grab
import grab, time, datetime, os, json, re, random, string, requests, transliterate, lxml, hashlib

app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)
admin = Admin(app, url="/ask_admin")
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.fun import *
from app.models import *
from app.fun_script import *
from app.admin import *
from app.views import *

if __name__ == '__main__':
    manager.run()