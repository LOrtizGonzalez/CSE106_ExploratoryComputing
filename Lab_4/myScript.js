var calc_str = "", str = "", last_action = "";
var dec = false; //flag checks to see if decimal has been added already
var clear = false; //to clear current input or clear the whole operation.

function buttonClicked(val) {
    var len = str.length;
    if(len < 9) { //will keep the length of number entered at no more than 9 digits.
        str += val;
    }
    //console.log(str.length);
    document.getElementById("calc_display").innerHTML = str;
}

function decimalClicked() {
    var len = str.length;
    if (len < 9 & dec == false) {
        str += ".";
        dec = true;
    }
    document.getElementById("calc_display").innerHTML = str;
}

function arithmeticButtonClicked(sign) {
    document.getElementById("calc_display").innerHTML = str;
    if (last_action.length != 0){ //if size if >1, means that an arithmetic symbol is already in the string and the num string can be inputted
        last_action += str;       //before moving on.
        //console.log(last_action); //FOR TESTING PURPOSES
    }
    if (sign == '=') {
        if (str.length < 1) { //when you click '=' back-to-back, will continue to do the last operation
            calc_str += last_action;
        }
        else {
            calc_str += str; 
            str = "";
        }
        console.log("last command",last_action); //FOR TESTING PURPOSES
        console.log("current calcs",calc_str); //FOR TESTING PURPOSES
        var solution = eval(calc_str);
        document.getElementById("calc_display").innerHTML = solution;
    }
    else {
        last_action = sign;
        //console.log(last_action); //FOR TESTING PURPOSES
        calc_str += str;
        str = "";
        document.getElementById("calc_display").innerHTML = eval(calc_str); //-----
        calc_str += sign;
        console.log(calc_str); //FOR TESTING PURPOSES
    }
}

function clearFunction() {
    if (clear == true) {
        calc_str = "";
        str = "";
        last_action = "";
        clear = false;
        console.log(str, "second clear", calc_str, "---", last_action);
        document.getElementById("calc_display").innerHTML = 0;
    }
    else {
        str = "";
        clear = true;
        console.log(str, "first clear ", calc_str)
        document.getElementById("calc_display").innerHTML = 0;
    }
}
