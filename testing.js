// Hello World !!
/*Hello world*/


console.log("Hello World");
var number = 9;
console.log(number);

// part 1
var a;          // unasignned variables
var b = 2;     // asigned variable

a = 5;
console.log(a);

console.log("All the mathematical operations are similar in js to python");

console.log("");

// typeof key word

let number1 = 89;

console.log(typeof number1);

// Converting string to number

const exp = "30";

const test = parseInt(exp); /* you can also use //const test = +exp; to convert
this happens when you use +exp Nan shortform means "Not a Number" */

console.log(test)

/*
There Exsist three types
    => Syntax Error
    => Runtime Error
    => Logical Error (MOST COMMON TYPE OF ERROR)
*/

console.log("Check Line 42 ONCE") // throw new Error("Any Thing You Wanna spam out")

// Try catch Finally

try {
    console.log(1);
    console.log(test);
    console.log(2);
} catch (error) {
    console.log(error.message);           // .message here just prints the error in normal message rather than in red
} finally {                              // finally is always executed no matter wats the problem
    console.log("completed execution");
}

