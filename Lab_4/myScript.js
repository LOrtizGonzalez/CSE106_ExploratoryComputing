var calc_str = "", str = "", last_action = "";
var dec = false; //flag checks to see if decimal has been added already
var clear = false; //to clear current input or clear the whole operation.
var number = 0;

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
        console.log(last_action);
    }
    if (sign == '=') {
        if (str.length < 1) { //when you click '=' back-to-back, will continue to do the last operation
            calc_str += last_action;
        }
        else {
            calc_str += str; 
            str = "";
        }
        console.log("last command",last_action);
        console.log("current calcs",calc_str);
        var solution = eval(calc_str);
        document.getElementById("calc_display").innerHTML = solution;
    }
    else {
        last_action = sign;
        console.log(last_action);
        calc_str += str;
        str = "";
        document.getElementById("calc_display").innerHTML = eval(calc_str); //-----
        calc_str += sign;
        console.log(calc_str);
    }
}

    function clearFunction() {
        if (clear == true) {
            calc_str = "";
            str = "";
            last_action = "";
            clear = false;
            document.getElementById("calc_display").innerHTML = 0;
        }
        else {
            str = "";
            clear = true;
            document.getElementById("calc_display").innerHTML = 0;
        }

    }


    //str = "";
    // if (sign == '+') {
    //     // calc_str += str;
    //     str = "";
    //     calc_str += sign;
    //     console.log(calc_str);
    // }
    // else if (sign == '-') {
    //     str = "";
    //     calc_str += sign;
    //     console.log(calc_str);
    // }
    // else if (sign == 'x') {
    //     str = "";
    //     calc_str += '*';
    //     console.log(calc_str);
    // }
    // else if (sign == '/') {
    //     calc_str += sign;
    //     console.log(calc_str);
    // }
    // else {
    //     // calc_str += str;
    //     console.log(calc_str);
    //     console.log(str);
    //     var solution = eval(calc_str);
    //     console.log(solution);
    //     document.getElementById("calc_display").innerHTML = solution;
    // }
    


// var equations = "12+1*2-2/.5";
// console.log(eval(equations));