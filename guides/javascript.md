# JavaScript Understanding the weird parts

## `syntax parser`, `execution context`, and `lexical environment`

A `syntax parser` is simply a program that reads the code you have written (`JavaScript` or whichever) and determines what it does and if its grammar is valid. They could be written in any language.

Some notable `syntax parser`s  are [esprima](https://github.com/jquery/esprima), which is written in `typescript` (a sort of `JavaScript`), [UglifyJS](https://github.com/mishoo/UglifyJS), and [Js/CC](https://github.com/abrobston/jscc), which are both written in `JavaScript`.

Esprima has a live [environment](https://esprima.org/demo/parse.html) where you can view a live syntactic analysis of any code as you type. There are also checkboxes to toggle on and off the location of every `token` in the program.

> A `token` is every single grammatical entity in the written code, except the comments.

Click this [URL](https://esprima.org/demo/parse.html?code=%2F%2F%20Life%2C%20Universe%2C%20and%20Everything%0Alet%20a%20%3D%205%3B%0Aconst%20b%20%3D%207%0Avar%20c%20%3D%20a%20*%20b%3B%0A%0Aconst%20f%20%3D%20name%20%3D%3E%20%7B%0A%09console.log(%60Hello%20%24%7Bname%7D%60)%0A%7D%0A) to see a demo program, it's syntactic analysis and the generated tokens.

The `parser` class of Esprima is located [here](https://github.com/jquery/esprima/blob/master/src/parser.ts).

`lexical environment` is where code is *physically* written in your `JavaScript` file. It's the space where you can locate the written code. In the code snippet below, the lexical environment of variable `a` is the whole file, while the lexical environment of variable `b` is inside the function.

```javascript
const a = 5;

function () {
    const b = 7;
}
```

`execution context` is a wrapper that manages the running code. It manages all the lexical environments that spring up during the execution of your code.

## `Global execution context`

1. When `JavaScript` code is executed, a parent (global) `execution context` is created.
1. The `JavaScript` engine creates

    1. a `global object`
    1. a special variable called `this` as part of that execution context

Inside a browser, the global object is the `window` object.

In `JavaScript`, `global` means, *not inside a function*.

### Hoisting

The `JavaScript` `execution context` is created in two phases:

1. Creation phase - During this phase, the following are set up in memory:

    1. `Global object`
    1. `this`
    1. an outer environment
    1. memory space for global `variables` and `functions`

1. The process of setting up this `memory space` is called `hoisting`. During this process, all variables are set to `undefined`.
1. Execution phase - This is when variable assignments happen.
1. `undefined` is a special `value` that means, *available, but not set yet*. This is what makes the following possible.

```javascript
console.log(name) // undefined
var name = 'somebody'
console.log(name) // somebody
```

## Execution phase

Every function creates a new `execution context`, which is put on the `execution stack`. It runs through the `create` phase, then the `execution` phase

## Functions, context, and variable environment

Where created variables `live` and how they relate to each other in memory.

### `Scope`

Where we're able to `see/access` a variable.

`JavaScript` has only `global` scope and `function` scope.

### `scope chain`

Every execution context has a reference to it's outer environment. This outer reference points to the `lexical environment`. i.e. where the function is *physically* located in the code file.

## `scope`, `ES6`, and `let`

`let` allows the `JavaScript` engine to use `block scoping`. This means that, although the variable is still placed in memory and set to `undefined` during creation phase, you're not allowed to *use* it until the line of code that declares them is run during the execution phase.

```javascript

const a = 4;
const b = 2;
console.log('before conditional', c) // Uncaught ReferenceError: c is not defined
if (a > b) {
    let c;
    console.log('before assignment', c) //undefined
    c = 25
    console.log('after assignment', c) // 25
}
console.log('after conditional', c) // Uncaught ReferenceError: c is not defined
```

## Event queue (`asynchronicity`)

A *list* that sits inside the `JavaScript` engine. It contains notifications to events that might be happening.

When the browser has an `event` that the `JavaScript` engine might be interested in, such event gets placed in the `event queue`.

The `event queue` is not touched *until* the call stack is empty. At this point the `JavaScript` engine looks at the `EQ` and if it sees an event there it checks to see if it needs to respond to that event.

`asynchronous callback` is simply something that is run in response to an event. `JavaScript` continuously watch the `EQ`.

## Types in `JavaScript`

`JavaScript` has dynamic typing. This means that the `JavaScript` engine is not told what type of data a variable is. It figures it out during execution.

A `primitive` type is a type of data that represents a single value. i.e. something that is not an object. They are

1. `undefined`
1. `null`
1. `boolean`
1. `number` - `JavaScript` has only one number type, and it's a floating point number.
1. `string`
1. `symbol`

An `operator` is actually a function that is written with `infix` notation.

`operator associativity` means in what order are operators called. i.e RTL (Right associativity) or LTR (Left associativity). This is important when the operators have the same `precedence`.

`coercion`: converting a value from one type to another.

<https://developer.mozilla.org/nl/docs/Web/JavaScript/Equality_comparisons_and_sameness>

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence>

## Functions as objects

An `expression` is a unit of code that results in a `value`.

```javascript
a = 3; // returns 3, so it's an expression
2 + 2; // returns 4, so it's an expression
```

1. In `JavaScript`, all functions are objects, having a `name` and `code` properties.
1. `function expression`s return a value.
1. `funcution statement`s just `perform` an action.

## By `reference` vs by `value`

Primitives interact by `value`.

```javascript
// by value. b gets the value of 3, but this 3 is in a distinct position in memory
// changing a doesn't affect b
let a = 3;
let b = a;
```

All objects interact by `reference`.

```javascript
// by reference. d simply points to the same location in memory where { x: 5 } sits.
let c = { x: 5 };
let d = c;
```

## `this` keyword

The `this` keyword points to the `object` inside which it is directly defined. It points to the global object when a function is defined in global scope, but points to the parent object when the function is a method of an object.

```javascript
const b = {
    name: 'b object',
    logArrow: () => {
        // here, this points to the global object
        console.log('this from arrow function ', this)
    },
    log: function() {
        console.log('this from function keyword', this) // this points to the b object

        const weird = function() {
            // we actually expect this to point to it's parent function's object
            // but that is not the case with javascript
            // here, this points to the global object
            // it is not directly sitting inside the b object
            console.log('weird this', this) // Window{...}
        }
        weird();
    }
}

b.log(); // this from function keyword {object: "b object", log: f}
b.logArrow(); // this from arrow function Window{...}
```

### Overcoming the weird behaviour of `this`

```javascript
const b = {
    name: 'b object',

    log: function() {
        // set a variable to 'this'.
        // since objects work by reference, this new variable also points
        // to the same location in memory as the 'this' object.
        // so we use this new variable everywhere we intend to use 'this'
        const self = this;
        console.log('this ', self) // 'this' points to the b object

        const not_weird = function() {
            console.log("not_weird 'this'", self) // Window{...}

            // now we can mutate the parent object
            self.last = "another name"
            console.log("not_weird 'this'", self) // not_weird this {name: "b object", log: ƒ, last: "another name"}

            self.name = "b name changed";
            console.log("not_weird 'this'", self) // not_weird this {name: "b name changed", log: ƒ, last: "another name"}
        }
        not_weird();
    }
}

b.log();
```

## Function `statement` vs function `expression`

1. A function statement must have a name. It is put into memory during the `creation` phase.
1. A function expression name is optional but is kept mostly anonymous because the name can't be used anyway. It is not put into memory, rather it is created on the fly during the `execution` phase.
1. To use a standalone as standalone, it could be wrapped in parenthesis. Only an `expression` is possible inside a parenthesis.
1. An expression is something that returns a value. e.g `(3 + 4)` returns 4. Statements never go inside parenthesis e.g `(if (whatever))`

```javascript
// function statement
function greet(name) {
    console.log('hello ' + name)
}

// function expression
const greeting = function(name) {
    console.log('hello ' + name)
}

// function expression without a LHS.
(function(name) {
    console.log('hello ' + name)
})
```

## Closures

When an `execution context` closes in all the variables it should normally have access to (including those in it's outer environment), even after the enclosing execution context has left the `call stack`

```javascript
greeting = (salutation) => {
    return (name) => {
        console.log(`${salutation} ${name}`)
    }
}

const x = greeting('good morning');
// the salutation variable is closed in by the return anonymous function
// simply because such variable is in its scope chain
x('friend')
```

### Closure with `var`

#### standalone `var`

It is important to note that the functions being pushed to the array are *NOT* being executed, thus no `execution context` (which closes in the variables) is created. Therefore, by the time these functions are called, `i` has already reached the value 3 and that is the value each of these functions see.

```javascript
const VARFuncs = () => {
    const funcs = [];
    for (var i = 0; i < 3; i++) {

        funcs.push(
            () => {
                console.log(`VARFuncs i is ${i}`)
            }
        )
    };
    return funcs;
}

const varFuncs = VARFuncs();

varFuncs[0](); // VARFuncs i is 3
varFuncs[1](); // VARFuncs i is 3
varFuncs[2](); // VARFuncs i is 3
```

#### `var` with `IIFE`

Here we make use of an `IIFE`, which creates an `execution context`. It is this `execution context` which closes in the value of `i`

```javascript
const VARFuncsCLOSED = () => {
    const funcs = [];
    for (var i = 0; i < 3; i++) {
        funcs.push(
            ((j) => (
                () => {
                    console.log(`VARFuncsCLOSED i is ${j}`);
                }
            ))(i));
    };
    return funcs;
}

const varFuncsClosed = VARFuncsCLOSED();

varFuncsClosed[0](); // VARFuncsCLOSED i is 0
varFuncsClosed[1](); // VARFuncsCLOSED i is 1
varFuncsClosed[2](); // VARFuncsCLOSED i is 2
```

### Closure with `let`

Because let is block scoped, the functions see the current value of i
when they are run

```javascript
const LETFuncs = () => {
    const funcs = [];
    for (let i = 0; i < 3; i++) {

        funcs.push(
            () => {
                console.log(`LETFuncs i is ${i}`)
            }
        )
    };
    return funcs;
}

const letFuncs = LETFuncs();
letFuncs[0](); // LETFuncs i is 0
letFuncs[1](); // LETFuncs i is 1
letFuncs[2](); // LETFuncs i is 2
```

## `call`, `apply`, and `bind`

All functions have access to a `call()`, `apply()`, and `bind()` methods

`bind` method creates a `copy` of a function and sets the `this` variable to the object that was passed to the `bind` method.

`call` methods simply `executes` the function (doesn't create a copy) and also allows setting the `object` that the `this` variable should point to, in addition to taking variables.

`apply` method works the same as `call` method, with only one difference: it takes a single array argument (inside of which could be any number of arguments).

`function currying` means creating a copy of a function, but with some preset parameters.

```javascript

const multiply = (a, b) => (
    a * b
);

// a is permanently set to 5
const multiplyByFive = multiply.bind(this, 5)


console.log(multiply(5, 4)) // 20
console.log(multiplyByFive(9)) // 45
```

## Reflection and extends

`reflection` means that an object can `look` at itself, listing and changing it's properties and methods. This helps us use the `extend` pattern.

`Object` - a collection name/value pairs

## Building `objects`

Building a `JavaScript` object happens in three steps.

1. Create an `object`.
1. Give it `properties` and `methods`
1. Set its `prototype`.

There are various ways to create objects in `JavaScript`. They are

1. With a `function constructor`, via the `new` keyword.
1. `Object.create` method.
1. `ES6` classes

### With a `function constructor`, via the `new` keyword.

`new` is an `operator` that creates an empty `object`. Consider the function definition below.

```javascript
function Person () {
  console.log(this);
  this.firstname = 'Chidi';
  this.lastname = 'Orji';
};
```

Let's invoke the function in the usual way. In this case the enclosing context is the `global` (`window` in the browser) object, therefore, `this` points to the `global` object.

```javascript
Person(); // Window {}
console.log(window.firstname) // 'Chidi'
console.log(window.lastname) // 'Orji'
```

Now let's invoke the function with the `new` keyword.

```javascript
const person = new Person(); // this: Person {}
console.log(person); // Person { firstname: 'Chidi', lastname: 'Orji' }
```

In this case, the `new` `operator` does several things.

1. It creates an empty object, `Person {}`.
1. Sets the `this` variable of the enclosing `execution context` to that empty object which it just created. That is why `console.log(this)` will eventually output `Person {}`
1. It now invokes the function and attaches the `firstname` and `lastname` properties to it.
1. Since no other object is returned from the function, the `JavaScript` engine retuns the `Person {}` `object` that it has created to the `p` variable. If any other `object` were returned by the `Person` function, that is what the `p` variable would assume.

```javascript
function Person () {
  this.firstname = 'Chidi';
  this.lastname = 'Orji';
  return {'Return me': 'Aiit boss.'}
};

const p = new Person();
console.log('Created ', p); // Created  { 'Return me': 'Aiit boss.' }
```

Arguments could be passed if desired.

```javascript
function Person (firstname, lastname) {
  console.log('this ', this);
  this.firstname = firstname;
  this.lastname = lastname;
  // return {'Return me': 'Aiit boss.'}
};

// Person();

const p = new Person('Chidi', 'Orji');
const p2 = new Person('Chidimma', 'Nwaigwe');
console.log('Created: ', p); //Created: Person { firstname: 'Chidi', lastname: 'Orji' }
console.log('Created2: ', p2); // Created2: Person { firstname: 'Chidimma', lastname: 'Nwaigwe' }
```

`function constructor` is a function that is used to construct objects using the `new` keyword. The `this` variable points to a new empty object and that object is returned automatically.

#### `function constructor` and `.prototype`

Every function has a name (could be anonymous), code to be exectuted, and a `prototype` property. The `prototype` property starts off as an empty `object`. Additional properties and methods can always be added to that object.

```javascript
function FunctionPrototype () {
  console.log('FunctionPrototype invoked')
}

console.log(FunctionPrototype.prototype) // FunctionPrototype {}
console.log(typeof FunctionPrototype.prototype) // object
console.log(FunctionPrototype.__proto__) // function () { [native code] }
console.log(FunctionPrototype.__proto__.__proto__) // {}
```

To use a function as a `function constructor` means to use the function in creating `object`s.

When creating objects with a `function constructor`, the `object`'s `prototype` is set automatically.

The `prototype` property on a function is *NOT* the prototype of the function. It is used *ONLY* by the `new` operator. It's the `prototype` of any `object` created if the function is being used as a `function constructor`. The function's own prototype is in the `.__proto__` property.

```javascript
function Person (firstname, lastname) {
  console.log('*this*', this);
  this.firstname = firstname;
  this.lastname = lastname;
  // return {'Return me': 'Aiit boss.'}
};

const p = new Person('Chidi', 'Orji');
console.log(p); // Person { firstname: 'Chidi', lastname: 'Orji' }
console.log(p.__proto__) // Person {}
console.log(Person.prototype) // Person {}
console.log(Person.prototype === p.__proto__) // true

Person.prototype.getFullName = function() {
  return `Mr/Mrs ${this.firstname} ${this.lastname}`
}

console.log(p.getFullName()) // Mr/Mrs Chidi Orji
console.log(p.__proto__) // Person { getFullName: [Function] }
console.log(Person.prototype) // Person { getFullName: [Function] }
```

#### `new` and functions

In the event that a function intended as a function constructor is invoked without the `new` operator, the `JavaScript` engine has no way of warning us about it. In that case, errors could creep into our code. So as a convention, function contructor names begin with a capital letter.

### Built in `function constructor`s

`JavaScript` has a number of built in function constructors that follow the capitalized first letter convention.

```javascript
const five = new Number('5')
console.log(five) // Number {5}
console.log(typeof five) // object
console.log(typeof Number('5')) // number
console.log(Number.prototype === five.__proto__) // true

const today = new Date('2019', '07', '17');
console.log(today); // Sat Aug 17 2019 00:00:00 GMT+0100 (West Africa Standard Time)
console.log(typeof today) // object
console.log(typeof Date()) // number
console.log(Date.prototype === today.__proto__); // true

const s = new String('Some string');
console.log(s); // String {"Some string"}
console.log(typeof s) // object
console.log(typeof String('Some string')) // number
console.log(String.prototype === s.__proto__); // true
```

Additional methods can always be added to any prototype. for example.

```javascript
Number.prototype.isEven = function() {
    // this refers to the object created with new
    return this.valueOf() % 2 === 0
}

const three = 3;
const six = 6;
console.log(three.isEven()) // false
console.log(six.isEven()) // true
```

When assigning primitive values, be aware that using the `new` operator creates an object, not a `primitive`.

#### Arrays and `for ... in`.

Arrays are actually objects, with the array indices as `key`s, and the values as their value. This is why `computed` member access works. This is the basis of the `for ... in` operation on arrays.

```javascript
const arr = [ 'Dog', 'Cat', 'Mouse']; // a shorthand for new Array()
for (let p in arr) {
  console.log(`${p}: ${arr[p]}`)
}

// output

0: Dog
1: Cat
2: Mouse
```

`0`, `1`, and `2` are the keys while `Dog`, `Cat`, and `Mouse` are the values.

But this fact presents some problems.

```javascript
console.log(Array.prototype) // {} not empty
console.log(typeof Array.prototype) // object
```

```javascript
Array.prototype.coolFeature = 'coolFeature'

const arr = [ 'Dog', 'Cat', 'Mouse'];
for (let p in arr) {
  console.log(`${p}: ${arr[p]}`)
}

// output
0: Dog
1: Cat
2: Mouse
coolFeature: coolFeature
```

We see that extending the `Array` prototype results in unintended consequences when using `for ... in` to loop over arrays. Thus, the safeway to loop over arrays is to use the standard `for (let i = 0; i < arr.length; i ++ )`

### `Object.create()` method

This method creates a new empty object and sets its prototype (`__proto__`) to the object that was passed in.
I could then add in my own properties as desired while having my created object's prototype intact.

```javascript
const person = {
  firstname: 'defaultFirst',
  lastname: 'defaultLast',
  salute: function () {
    return `Hi! ${this.firstname}`
  }
}

const me = Object.create(person)
console.log(me) // {}
console.log(me.salute()) // Hi! defaultFirst
console.log(me.__proto__) // {firstname: "defaultFirst", lastname: "defaultLast", salute: ƒ}
console.log(me.__proto__ === person) // true


// override properties
me.firstname = 'Chidi'
me.lastname = 'Orji'
console.log(me) // { firstname: 'Chidi', lastname: 'Orji' }
console.log(me.salute()) // Hi! Chidi

// override methods
me.salute = function () {
  return 'Hi my Gee!!!'
}
console.log(me.salute()) // Hi my Gee!!!
```

### `ES6` classes

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes>

Objects can also be created using `ES6` classes. Any property or method preceded by `this.` is added to the instance object directly, while any other one is added to the object's `__proto__`

1. Instance properties must be defined inside of class methods
1. Static class-side properties and prototype data properties must be defined outside of the ClassBody declaration

```javascript
class Child {
    constructor(name) {
        console.log('*this*', this) // *this* Child {}
        this.childName = name;
    };

    runToSchool () {
        console.log(`${this.childName} is running to school`)
    };
}

Child.prototype.washPlates = 'I wash plates'

let child = new Child('Chidiebere');
console.log(child.childName); // Chidiebere
console.log(child.washPlates); // I wash plates
child.runToSchool(); // Chidiebere is running to school
console.log(Child.__proto__) // ƒ () { [native code] }

console.log(child.__proto__)

        { washPlates: "I wash plates"
        constructor: class Child
        runToSchool: ƒ runToSchool()
        __proto__: Object }


class SeniorChild extends Child {
    // name is passed to Child for initialization
    constructor(seniorChildName) {
        // *this* SeniorChild {}
        super(seniorChildName);
    }

    playSports () {
        console.log(`${this.childName} is a senior child and plays sports`)
    }
}

let senior = new SeniorChild('Eze');
console.log(senior.childName) // Eze
senior.runToSchool(); // Eze is running to school
senior.playSports(); // Eze is a senior child and plays sports
console.log(senior.__proto__)

        Child {
            constructor: class SeniorChild
            playSports: ƒ playSports()
            __proto__: {
                washPlates: "I wash plates"
                constructor: class Child
                runToSchool: ƒ runToSchool()
                __proto__: Object
            }
        }

console.log(SeniorChild.__proto__)

    class Child {
        constructor(name) {
            console.log('*this*', this) // *this* Child {}
            this.childName = name;
        };

        runToSchool () {
            console.log(`${this.childName} is running to…
```

## Odds and Ends

1. `Object.prototype.toString.call([]) // [Object Array]`

## React 15.3 internals

Three building blocks of react:

1. native DOM elements
1. virtual React elements: an in-memory representation of what you'd like a given DOM element (or tree of elements) to look like for a particular render
1. components
