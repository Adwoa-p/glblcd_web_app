from flask import Flask,render_template
from markupsafe import escape
import os
from flask_sqlalchemy import SQLAlchemy


#configuring sqlalchemy

app = Flask(__name__)
current_path = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(current_path,'data.sqlite')
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False


db = SQLAlchemy(app) #to help us communicate with the database

#model or entity
class Student(db.Model): 
    __tablename__ = 'Student'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    gender = db.Column(db.Text)


    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


@app.route("/")
def index():
    return "<h1> Getting started with Flask and Databases </h1>"
