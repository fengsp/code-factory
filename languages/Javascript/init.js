myglobal = "fsp";
var mg = "mg";


console.log(myglobal);
console.log(mg);
console.log(this.myglobal);
console.log(this.mg);
console.log(this);


function sum(x, y) {
    result = x + y;
    return result;
}


try {
    console.log(result);
} catch(e) {
    console.log(e);
}
r = sum(1, 2);
console.log(r);
console.log(result);


function test() {
    var pre_one = 'pre_one',
        pre_two = 'pre_two',
        one = 'one',
        two = 'two',
        dict = {},
        list = [],
        i,
        j;
}
test();


myarray = [];
myarray.push('1');
myarray.push('2');
myarray.push(3);
for (var i = 0, max = myarray.length; i < max; i++) {
    console.log(myarray[i]);
}


var looper = function(iterable) {
    var i = 0,
        callback = arguments[1]?arguments[1]:console.log,
        max;
    for (i = 0, max = iterable.length; i < max; i++) {
        callback(iterable[i]);
    }
}


function callback(value) {
    console.log('console: ' + value);
}


looper(myarray);
looper(myarray, callback);


var man  = {
    hands: 2,
    legs: 2,
    heads: 1
};


if (typeof Object.prototype.clone === "undefined") {
    Object.prototype.clone = function() {};
}


for (var i in man) {
    console.log(i, ":", man[i]);
    if (man.hasOwnProperty(i)) {
        console.log(i, ":", man[i]);
    }
}


var day = new Date().getDay();
switch(day) {
case 0:
    console.log("Sunday");
    break;
case 1:
    console.log("Monday");
    break;
case 2:
    console.log("Tuesday");
    break;
case 3:
    console.log("Wednesday");
    break;
case 4:
    console.log("Thursday");
    break;
case 5:
    console.log("Friday");
    break;
case 6:
    console.log("Saturday");
    break;
default:
    console.log("WTF");
    break;
}
