from flask import Flask,render_template
from markupsafe import escape
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#configuring sqlalchemy

app = Flask(__name__)
current_path = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(current_path,'data.sqlite')
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False


db = SQLAlchemy(app) #to help us communicate with the database
Migrate(app,db)

#model or entity
class Student(db.Model): 
    __tablename__ = 'Student'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    gender = db.Column(db.Text)
    allowance = db.Column(db.Integer)


    def __init__(self,name,age,gender,allowance):
        self.name = name
        self.age = age
        self.gender = gender
        self.allowance = allowance

# to get data from the db
    def __repr__(self):
        return f"{self.name},{self.age},{self.gender},{self.allowance}"


@app.route("/students")
def get_all_students():
    students_from_database = Student.query.all()
    return render_template('index.html', students=students_from_database)

@app.route("/students/<name>")
def delete_students(name):
    Student.query.filter(Student.name == name ).delete(synchronize_session=False)
    remaining_students = Student.query.all()
    db.session.add_all(remaining_students)
    db.session.commit()
    return render_template('index.html', students=remaining_students)
