#import logging
from flask import Flask, abort, jsonify, render_template, url_for, redirect, request
import json

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
app = Flask(__name__)
#CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.sqlite"
db = SQLAlchemy(app)

class Students(db.Model):
    __tablename__ = "Students"

    name = db.Column(db.String, primary_key=True)
    grade = db.Column(db.Float, nullable=False)

    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade


def makeToDictionary(): # To be able to return in dictionary form to front-end
    data = Students.query.all()
    q = {}
    for row in data:
        q[row.name] = row.grade
    return q


@app.route('/')
def index():
    db.create_all() # Needed to create table
    return render_template("index.html")

@app.route('/grades')
def viewGrades():
    return json.dumps(makeToDictionary())

@app.route("/grades/<sname>")
def studentGrade(sname):
    student = Students.query.filter_by(name=sname).first()
    if(student is not None):
        return ({sname:student.grade})
    else:
        return abort(404)

@app.route("/grades", methods = ["POST"])
def createStudent():
    student = request.json['name']
    grade = request.json['grade']
    newStudent = Students(student, grade)
    db.session.add(newStudent)
    db.session.commit()
    return ({student:grade})
   
    
@app.route("/grades/<sname>", methods = ["PUT"])
def editGrade(sname):
    newGrade = request.json['grade']
    editStudent = Students.query.filter_by(name = sname).first()
    if editStudent is not None:
        editStudent.grade = newGrade
        db.session.commit()
        return ({sname:editStudent.grade})
   

@app.route("/grades/<sname>", methods = ["DELETE"])
def deleteStudent(sname):
    delStudent = Students.query.filter_by(name = sname).first()
    if delStudent is not None:
        db.session.delete(delStudent)
        db.session.commit()
        return sname
    else:
        return abort(404)
    

if __name__ == '__main__':
    app.run(debug=True)
    #main()