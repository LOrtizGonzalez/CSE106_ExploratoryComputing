var baseURL = "http://127.0.0.1:5000";

function getGrades() {
    var xhttp = new XMLHttpRequest();
    var url = baseURL + "/grades";
    console.log("in xmlgetGrades")//console.log(url)
    xhttp.open("GET", url, true);
    xhttp.onload= function() {
        const rep = JSON.parse(this.responseText);
        for(objs in rep){ console.log(objs);
            document.getElementById("allGrades").innerHTML += `<tr><td>${objs}</td><td>${rep[objs]}</td></tr>`
        }
    };
    xhttp.send();
}

function searchStudent() {
    var val = document.getElementById("name").value;
    var url = baseURL + "/grades/"; //will be used when sending request
    
    url += val
    console.log("in xmlsearchStudent")//console.log(url);
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", url,true);
    xhttp.onload = function() {
        if(xhttp.status != 404) {
            var rep = JSON.parse(this.responseText);
            document.getElementById("searchReply").innerHTML = "Grade: " + rep[val];
        }
        else {
            document.getElementById("searchReply").innerHTML = "Student record does not exist."
        }
    }
    xhttp.send();
}

function createStudent() {
    var url = baseURL;
    let name1 = document.getElementById("newStudentName").value;
    let grade1 = document.getElementById("newStudentGrade").value;
    
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", url + "/grades");
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = {
        name : name1,
        grade : eval(grade1)
    };
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function() {
        const rep = JSON.parse(this.responseText);
        document.getElementById("createHeader").innerHTML = "Student " + name1 + " was created.";
    };
}

function editGrades() {
    var name1 = document.getElementById("editGrade").value;
    var grade1 = document.getElementById("updatedGrade").value;
//console.log(name1, grade1)
    var xhttp = new XMLHttpRequest();
    xhttp.open("PUT", baseURL + "/grades/" + name1, true);
    //console.log(baseURL+"/grades/"+name1)
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = {
        grade : Number(grade1)
    };
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function () {
        let rep = JSON.parse(this.responseText);
        //rep = JSON.parse(rep);
        Object.entries(rep).forEach(([key,value]) => {
            if(key == name1) {
                document.getElementById("Updated").innerHTML = key + ":" + value;
            }
        });
    };
}


function deleteStudent() {
    let val = document.getElementById("delete_Student").value;
    console.log(val);
    var url = baseURL + "/grades/" + val;
    console.log(url);
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", url, true);
    xhttp.onload = function() {
        if(xhttp.status != 404) {
            var xtp = new XMLHttpRequest();
            xtp.open("DELETE", url, true);
            xtp.onload = function() {
                document.getElementById("deletedStudent").innerHTML = "Deleted " + val;
            }
            xtp.send();
        }
        else {
            document.getElementById("deletedStudent").innerHTML = "No Student Record Found."
        } 
    };
    xhttp.send();
}