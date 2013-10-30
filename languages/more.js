var foo;
var document = Object();
document.documentElement = Object();
if (true) {
    foo = function() {
        return 'first';
    };
} else {
    foo = function() {
        return 'second';
    };
}
console.log(foo());


var contains = (function() {
    var docEl = document.documentElement;

    if (typeof docEl.compareDocumentPosition != 'undefined') {
        return function(el, b) {
            return (el.compareDocmentPosition(b) & 16) !== 0;
        };
    } else if (typeof docEl.contains != 'undefined') {
        return function(el, b) {
            return el !== b && el.contains(b);
        };
    }
    return function (el, b) {
        if (el === b) return false;
        while (el != b && (b = b.parentNode) != null);
        return el === b;
    };
})();


var fsp = {
    x: 10,
    y: 20
};
var a = {
    x: 10,
    calculate: function (z) {
        return this.x + this.y + z;
    }
};
var b = {
    y: 20,
    __proto__: a
};
var c = {
    y: 30,
    __proto__: a
};
b.calculate(30);
c.calculate(40);


function Test(y) {
    this.y = y;
}
Test.prototype.x = 10;
Test.prototype.calculate = function (z) {
    return this.x + this.y + z;
};
var b = new Test(20);
var c = new Test(30);
b.calculate(30);
c.calculate(40);
