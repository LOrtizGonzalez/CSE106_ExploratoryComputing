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
    print(response)
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
    


# def main():
#     file = open("data.json", 'r')
#     data = file.read()
#     file.close()
#     grades = json.loads(data)
#     for key,value in grades.items():
#         print(key,value)


if __name__ == '__main__':
    app.run(debug=True)
    #main()


