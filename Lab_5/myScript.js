function getGrades() {
    var xhttp = new XMLHttpRequest();
    var url = "https://amhep.pythonanywhere.com/grades";
    xhttp.open("GET", url, true);
    xhttp.onload= function() {
        const rep = JSON.parse(this.responseText);
        for(objs in rep){ console.log(objs);
            document.getElementById("allGrades").innerHTML += `<tr><td>${objs}</td><td>${rep[objs]}</td></tr>`
        }
    };
    xhttp.send();
} 
//getGrades();

function searchStudent() {
    var val = document.getElementById("name").value;
    var url = "https://amhep.pythonanywhere.com/grades/"; //will be used when sending request
    
    url += val
    console.log(url);
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
    var url = "https://amhep.pythonanywhere.com/";
    let name1 = document.getElementById("newStudentName").value;
    let grade1 = document.getElementById("newStudentGrade").value;
    
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", url + "/grades");
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = {
        "name" : name1,
        "grade" : eval(grade1)
    };
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function() {
        const rep = JSON.parse(this.responseText);
        // document.getElementById("createHeader").innerHTML = "Student " + name1 + " " + rep[name1] + " was created.";
        document.getElementById("createHeader").innerHTML = "Student " + name1 + " was created.";
    };
}

function editGrades(name) {
    let val = document.getElementById("editGrade").value;
    //console.log(val);
    var xhttp = new XMLHttpRequest();
    var url = "https://amhep.pythonanywhere.com/grades/" + val;
    //console.log(url);
    xhttp.open("GET", url);
    xhttp.onload = function() {
        if(xhttp.status != 404) {
            const payload = {
                grade: eval(document.getElementById("updatedGrade").value)
            }
            var xtp = new XMLHttpRequest();
            xtp.open("PUT", url, true);
            xtp.setRequestHeader("Content-Type", "application/json");
            xtp.onload = function() {
                if(xtp.status != 404) {
                    const rep = JSON.parse(this.responseText);
                    document.getElementById("Updated").innerHTML = "Updated " + val + " with new Grade: " + rep[val];
                }
            }
            xtp.send(JSON.stringify(payload));
        }
        else {
            document.getElementById("Updated").innerHTML = "Student does not exist."
        }
    };
    xhttp.send();
}

function deleteStudent() {
    let val = document.getElementById("delete_Student").value;
    console.log(val);
    var url = "https://amhep.pythonanywhere.com/grades/" + val;
    //console.log(val); 
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