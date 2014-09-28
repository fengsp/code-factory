/**
 * idiomatic.js
 * https://github.com/rwaldron/idiomatic.js/tree/master/translations/zh_CN
 * 不要使用内部留白，丑死了
 */

if ( condition ) {
    // expression
}

while ( condition ) {
    // exp
}

for ( var i = 0; i < 100; i++ ) {
    // exp
}

for ( var prop in object ) {
    // exp
}

if ( true ) {
    // true
} else {
    // false
}

// 变量
var foo = "bar",
  num = 1,
  undef;

var array = [],
  object = {};

function foo() {
  var bar = "",
    qux;
  
  // 语句置于变量之后
}

function foo( arg1, argN ) {
    
}

foo( arg1, argN );

function square( number ) {
  return number * number;
}

square( 10 );

square( 10, function (square ) {
    // callback
});

var square = function( number ) {
  return number * number;
};

var factorial = function factorial( number ) {
  if ( number < 2 ) {
    return 1;
  }

  return number * factorial( number-1 );
};

function FooBar( options ) {
  this.options = options;
}

var fooBar = new FooBar({ a: "alpha" })
fooBar.options

foo(function() {
  //
});

foo([ "alpha", "beta" ]);
foo({
  a: "alpha",
  b: "beta"
});

foo("bar");

if ( !("foo" in obj) ) {
  //
}

if (condition) {
  //
}

while (condition) {
  //
}

for (var i = 0; i < 100; i++) {
  //
}

if (true) {
  //
} else {
  //
}

//String
typeof variable === "string"
//Number
typeof variable === "number"
//Boolean
typeof variable === "boolean"
//Object
typeof variable === "object"
//Array
Array.isArray( arrayLikeObject )
//Node
elem.nodeType === 1
//null
variable === null
//null or undefined
variable == null
//undefined global
typeof variable === "undefined"
//undefined local
variable === undefined
//Attr
object.prop === undefined
object.hasOwnProperty( prop )
"prop" in object

if (array.length) ...
if (!array.length) ...
if (string) ...
if (!string) ...
// match 0 "" null undefined
if (!foo) ...
// match null undefined
if (foo == null) ...

(function(global) {
  var Module = (function() {
    var data = "secret";

    return {
      bool: true,
      string: "string",
      array: [1, 2, 3, 4],
      object: {
        lang: "en-Us"
      },
      getData: function() {
        return data;
      },
      setData: function(value) {
        return (data = value);
      }
    };
  })();

  global.Module = Module;
})(this);

(function(global) {
  
  function Ctor(foo) {
    this.foo = foo;
    return this;
  }

  Ctor.prototype.getFoo = function() {
    return this.foo;
  };

  Ctor.prototype.setFoo = function(val) {
    return (this.foo = val);
  };

  var ctor = function(foo) {
    return new Ctor(foo);
  };

  global.ctor = ctor;
})(this);
