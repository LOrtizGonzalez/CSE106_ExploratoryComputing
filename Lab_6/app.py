import logging
from flask import Flask, abort, jsonify, render_template, url_for, redirect, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/grades')
def viewGrades():
    with open("static/data.json", "r") as file:
        string = ""
        for row in file:
            string += row.strip()
    currGrades = json.loads(string) # Loading data into new dictionary in json format
    response = jsonify(currGrades)
    #print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/grades/<name>")
def studentGrade(name):
    with open("static/data.json", "r") as file:
        string = ""
        for row in file:
            string += row.strip()
    studentGrade = json.loads(string)
    if name in studentGrade:
        response = jsonify({name : studentGrade[name]})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        abort(404)

@app.route("/grades", methods = ["POST"])
def createStudent():
    with open("static/data.json", "r") as file: # Grabbing data from json file
        string = ""
        for row in file:
            string += row.strip()
    studentGrade = json.loads(string)
    studentGrade[request.json["name"]] = request.json["grade"]
    with open("static/data.json", "w") as file:    
        json_dump = json.dumps(studentGrade, indent = 4)
        #print(json_dump) #for testing purposes
        file.write(json_dump)
    return studentGrade
    
@app.route("/grades/<name>", methods = ["PUT"])
def editGrade(name):
    studentGrade = json.load(open("static/data.json"))
    if name in studentGrade:
        newSub = request.get_json()
        studentGrade[name] = newSub['grade']
        add_json = open("static/data.json", 'w')
        json.dump(studentGrade, add_json)
        add_json.close()
        return studentGrade

@app.route("/grades/<name>", methods = ["DELETE"])
def deleteStudent(name):
    studentGrade = json.load(open("static/data.json"))
    if name in studentGrade:
        del studentGrade[name]
        add_json = open("static/data.json", 'w')
        json.dump(studentGrade, add_json)
        add_json.close()
        return studentGrade
    

if __name__ == '__main__':
    app.run(debug=True)
    #main()


