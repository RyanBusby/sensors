import sys, os

from datetime import datetime

from flask import Flask, render_template, request, redirect, jsonify, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
pword = os.getenv('birdhouse_pword')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:{}@localhost:5432/birdhouse'.format(pword)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Temp(db.Model):
    __tablename__ = 'temp'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)

class Humid(db.Model):
    __tablename__ = 'humid'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)

class Infared(db.Model):
    __tablename__ = 'infared'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    value = db.Column(db.Boolean, nullable=False)

class SolarVolts(db.Model):
    __tablename__ = 'solarvolts'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)
