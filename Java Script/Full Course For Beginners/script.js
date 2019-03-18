/**
 * * Here are differents scripts for learning JavaScript.
 */

// Prints on the browser console.
console.log("Hello World!");

/**
 * Data types.
 * undefined, null, boolean, string, symbol, number and object.
 */

var myName = "Juan" // Would be used on the whole program.

myName = 17

let ourName = "Manuel" // Would be used in a scope.

const pi = 3.1416 // Never will be changed.

/**
 * Operators
 * +, -, *, /, %
 */

var a = 3;
var b = 4;
var c = 5;

a += 12;
b -= -2;
c *= a;
b /= 2;
a = b % c;


/**
 * Literals
 * \'   single quote
 * \""  double quote
 * \\   backslash
 * \n   new line
 * \r   carriage return
 * \t   tabulation
 * \b   backspace
 * \f   form feed
 */

var myString = "\tMy first string on JavaScript\n";

var quote = "I'm a \"double quoted\" string inside a \"double quotes\"";

// Or I can do this.
var secondQuote = 'I\'m a "double quoted" string inside a "double quotes"';

// Or this.
var thirdQuote = `I'm a "double quoted" string inside a "double quotes"`;

/**
 * Strings
 */

var firstName = "Juan";
var secondName = "Manuel";
var name = firstName + secondName;

var nameLength = name.length; // return the length of the name.

console.log(name[0]); // Prints the first letter of the name (J).

// Also we can change a string with the previously way.
var newVar = "Jello World!";

newVar[0] = "H";

/**
 * Functions
 */

function wordBlanks(myNoun, myAdjective, myVerb, myAdverb) {
    var result = ""
    result += "The " + myAdjective + " " + myNoun + " " + myVerb + " to the store " + myAdverb
    return result
}

console.log(wordBlanks("dog", "big", "ran", "quickly."))
console.log(wordBlanks("bike", "slow", "flew", "slowly."))

/**
 * Arrays
 */

var ourArray = ["Juan", 17];

var multiDimensionalArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

var anotherArray = [];

anotherArray.push(90)
anotherArray.push(78)
anotherArray.push(12)
anotherArray.push(56)
anotherArray.push(34)

anotherArray.sort() // [12, 34, 56, 78, 90]
anotherArray.pop() // [12, 34, 56, 78]
anotherArray.shift() // [34, 56, 78]
anotherArray.unshift("I have unshifted this") // ["I have unshifted this", 34, 56, 78]