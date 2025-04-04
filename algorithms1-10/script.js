//001 - print the message "You have to do algorithms every day to learn!".
function algorithm1(){
    var commitment = "You have to do algorithms every day to learn!";
    alert(commitment);
}
//002 - type your name.
function algorithm2(){
    var name = prompt("Type your name");
    alert("Olá " + name);
}
//003 - Create an algorithm that prints the product between 28 and 43

function algorithm3(){
    var num1 = 28;
    var num2 = 43;
    var product = num1 * num2;
    console.log("O product between " + num1 + " and " + num2 + " is " + product);
}

//004 - Create an algorithm that prints the arithmetic average between the numbers 8, 9 and 7.

function algorithm4(){
    var num1 = 8;
    var num2 = 9;
    var num3 = 7;
    
    var averenge = (num1 + num2 + num3) / 3;
    console.log("The avereng between " + num1 + ", " + num2 + " and " + num3 + " is " + averenge);

}

//005 - read a interger and print. 

function algorithm5(){
    var interNum = prompt("tyope an integer");
    console.log("The namber is: " + interNum);
}

//006 - Read an integer and print its successor and predecessor.

function algorithm6(){
    var num = parseInt(prompt("Type an interger"));
    var successor = num + 1;
    var predecessor = num - 1;
    console.log("The successor and predecessor de " + num + " is " + successor + " and " + predecessor);

}

//007 - Read two integers and print the sum. Before the result, it should appear the message: Sum.

function algorithm7(){
    var num1 = parseInt(prompt("Type an interger"));
    var num2 = parseInt(prompt("Type another interger"));
    var sum = num1 + num2;
    console.log("Sum = " + sum);
}


function algorithm8(n){
    var output = [];
    if(n === 1){
        output = [0];
    }else if (n === 2){
        output = [0,1];
    }else{
        output = [0, 1];
        
        for (var i = 2; i < n; i++) {
            output.push(output[output.length - 2] + output[output.length - 1]);
        }
        return output;
    }
}
/*function algorithm8(weight, height){
    var x = Math.pow(height, 2)
    var y = weight / x;
    
    return Math.round(y);
    
}
var x = algorithm8(65, 1.8);
console.log(x)*/

algorithm8(6);