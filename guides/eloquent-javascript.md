# [Eloquent Javascript](https://eloquentjavascript.net)

A function that references bindings from local scopes around it is called a closure

A pure function is a specific kind of value-producing function that not only has no side effects but also doesn’t rely on side effects from other code—for example, it doesn’t read global bindings whose value might change. A pure function has the pleasant property that, when called with the same arguments, it always produces the same value (and doesn’t do anything else). A call to such a function can be substituted by its return value without changing the meaning of the code. When you are not sure that a pure function is working correctly, you can test it by simply calling it and know that if it works in that context, it will work in any context. Nonpure functions tend to require more scaffolding to test.

## Three  notations for defining functions in `javascript`

```javascript
// Notation 1: function keyword used as an expression
let funcName = function(parameter) {
    console.log("Do something")
}

// Notation 2: function keyword used as a statement
// Declare a binding and give it a function as its value
function funcName(parameters) {
    console.log("Do something")
}

// Notation 3. Arrow functions
let funcName = (parameters) => {
    console.log("Do something")
}

// When there is only one parameter, the parenthesis around the arrow function parameter can be omitted
funcName = parameter => {
    console.log("Do something")
}

p = a => a * 5 // assigns the function a => a * 5 to the variable p
```

## Function argument numbers in `javascript` vs `python`

In `javascript` you are allowed to do this

```javascript
let funcName = (a, b, ... z) => {
    console.log("Do something")
}

funcName(a) // call the function with only one parameter
```

But if you try such a thing in `python` you get a `TypeError`.

```python
def func_name(a, b, ... z):
    pass

func_name(a) # call the function with only one parameter leads to the below error

TypeError: func_name() missing n required positional arguments: b, ... z

# To handle multiple arguments in python we use the *args notation
def func_name(*args):
    pass

```

## Functions as arguments in `javascript` vs `python`

In `javascript` you can do

```javascript
funcName = function(a) {
    console.log("Do something")
}

funcName("a") // Call the function

// You could also do it like below
function funcName(a){
    console.log("Do something")
}
funcName("a") // Call the function
```

In `python`, you can achieve something similar, but with different notation

```python
def funcName(a):
    pass

s = funcName # assign the function to a variable
s("a") # call the function
```

## Both `javascript` and `python` functions can return functions

```javascript
let salute = (age) => {
    let showAge = (name) => {
        console.log(`Welcome ${name}`)
        console.log(`Your age is ${age}`)
    }
    return showAge
}

s = salute(32) // returns showAge function
s("chidi")

console.log(s) // returns the showAge function
(name) => {
    console.log("Welcome " + name)
    console.log("Your age is " + age)
}
```

```python
def salute(age):
    def show_age(name):
        print("Welcome ", name)
        print("Your age is ", age)
    return show_age

# Call the function
s = salute(32) # returns the show_age function
s("chidi") # pass the my name argument to the show_age function
```

## Modern array looping construct over elements of an array (also works for strings)

```javascript
// The below loop construct has a shorthand version shown further below
let arr = []

for (let i = 0; i < arr.length; i++) {
  let each = arr[i];
  // Do something with entry
}

for (let each of arr) {
  console.log(`${each} whatever.`);
}
```

Translated to `python`, the above blocks of code look like below

```python
arr = []
for i in range(len(arr)):
    e = arr[i]

for each in arr:
    print(each)
```

## `javascript` array methods (lists in `python`)

1. `push(element)` add element to the end (RHS) of an array. `append` in `python`
1. `pop()` remove element from the end (RHS) of an array. `pop()` in `python`
1. `unshift` add element to the front (LHS) of an array. `insert(0, element)` in `python`
1. `shift()` remove element from the front (LHS) of an array. `pop(0)` in `python`
1. `indexOf(element, start)` search for and returns the index of `element` starting from start to end. Returns -1 if `element` is not found. `start` is optional and indicates where to start the search.
1. `lastIndexOf(element, start)` search for and returns the index of `element` starting from the end of the array. Returns -1 if `element` is not found. `start` is optional and indicates where to start the search.
1. `slice` returns a subset of the array e.g.`console.log([0, 1, 2, 3, 4, 5].slice(2, 4)) → [2, 3]`, `console.log([0, 1, 2, 3, 4, 5].slice(2)) → [2, 3, 4, 5]`
1. `concat` joins two arrays.
1. `array_object.reverse()` reverses an array in place.
1. `findIndex`: syntax `array.findIndex(element)`
1. `includes`: syntax: `array.includes(item)`. Check if item is in array

## Higher Order array functions

1. `forEach` function provides a `for/of` loop as a HOF: `["A", "B"].forEach(l => console.log(l));`
1. `filter`: syntax: `array.filter(filtering-function)`
1. `map`: syntax: `map(array, mapping-function)`
1. `reduce` sometimes called `fold`: syntax: `array.reduce(reducing-function)`
1. `some`: `array.some(test_function)`. Tells if any element of `array` returns `true` for the test_function. Equivalent to `python`'s `any()`.

## `javascript` string properties

Values of type `string`, `number`, and `Boolean` are **not** `objects`, and though the language doesn’t complain if you try to set new properties on them, it doesn’t actually store those properties.

```javascript
console.log("coconuts".slice(4, 7)); // → nut
console.log("coconuts".indexOf("nu")); // → 4
console.log("  okay \n ".trim()); // → okay
console.log(String(6).padStart(3, "0")); // → 006

let sentence = "javascript is good"
sentence.split(" ")// → ["javascript", "is", "good"]

let words = ["I", "love", "python"]
words.join(", ") // → "I, love, python"

"java".repeat(3) // → "javajavajava"
```

For a function to accept any number of arguments we use the `...parameters` notation. `*args` construct in `python` accomplishes something similar.

```javascript
function funcName(...parameters) {
    // access each parameter
    for (let parameter of parameters) {
        console.log()
    }
}
```

Every parameter coming after the `triple-dots` is bound to a single array containing all further arguments. The values of any other parameters that may come before the `triple-dots` are not part of that array. The notation can be used to `unwrap` an array of arguments

```javascript
let names = ["javascript", "python", "ruby", "java"]
console.log(...names) // → javascript python ruby java
console.log(["c++", ...names, "c#"]) // → ["c++", "javascript", "python", "ruby", "java", "c#"]
```

## JSON

`JSON.stringify(argument)` returns a `json`-encoded string representation of its argument.

`JSON.parse(argument)` takes a `json`-encoded string and converts it to the value it encodes.

## Higher order functions

Functions that operate on other functions, either by taking them as arguments or by returning them, are called *higher-order functions*.

Objects, as generic blobs of values, can be used to build all sorts of data structures. A common data structure is the list (not to be confused with array). A list is a nested set of objects, with the first object holding a reference to the second, the second to the third, and so on.

```javascript
let list = {
    value: 1,
    rest: {
        value: 2,
        rest: {
            value: 3,
            rest: null
        }
    }
};
```

The resulting objects form a chain

In the two function definitions below, the function arguments can be accessed in certain ways. In the first version, the `list` argument is not available inside the `for` loop. To get access to it inside the loop I have to sort of rebind it to the function using `this.list = list`, and each time I want to use it inside the for loop I have to use `this.list` But if I remove the `let` keyword behind the loop variable `i`, the list argument becomes available inside the for loop. The code below shows the version without the `let` keyword

```javascript
// Version 1
nth = (list, position) => {
    this.list = list
    for (let i = 0; i <= position; i++) {
        console.log(this.list)
    }
}

// Version 2
nth = (list, position) => {
    for (i = 0; i <= position; i++) {
        console.log(list)
    }
}
```

## `scripts.js` data structure

```javascript
{
  name: "Coptic",
  ranges: [[994, 1008], [11392, 11508], [11513, 11520]],
  direction: "ltr",
  year: -200,
  living: false,
  link: "https://en.wikipedia.org/wiki/Coptic_alphabet"
}
```

## Objects

When you compare objects with JavaScript’s `==` operator, *it compares by identity*: it will produce `true` only if both objects are precisely the same value. Comparing different objects will return `false`, even if they have identical properties. There is no **"deep"** comparison operation built into JavaScript, which compares objects by contents.

A `const` binding to an object can itself not be changed and will continue to point at the same object, but the contents of that object might change. For example

```javascript
const person = {name: "chidi", age: 32}
person.age = 33 // This is allowed
person = {name: "chidi", age: 33} // This is not allowed
```

### Encapsulation

### Methods

1. When a function is called as a method—looked up as a property and immediately called, as in `object.method()`—the binding called `this` in its body automatically points at the object that it was called on.
1. If you want to pass `this` explicitly, you can use a function’s `call` method, which takes the `this` value as its first argument and treats further arguments as normal parameters. `method_name.call(object, method_parameters)`
1. Each function has its own `this` binding whose value depends on the way it is called.
1. You cannot refer to the `this` of the wrapping scope in a regular function defined with the `function` keyword.
1. Arrow functions *do not bind their own `this`* but they can see the `this` binding of the scope around them.

```javascript
// in this version, this.when will return 'always'
function sayHello() {
  this.names.map(name => console.log("I love", name, this.when))
}
sayHello.call({names: ["goat", "dog", "cat"], when:"always"})

// in the below version, this.when will return undefined
function sayHello() {
  this.names.map(function(name) {console.log("I love", name, this.when)})
}
sayHello.call({names: ["goat", "dog", "cat"], when:"always"})
```

### Prototypes

In addition to their property set, most `javascript` objects have a `prototype`, an object that is used as a fallback source of properties for an object.

1. Base object prototype: `Object.prototype`
1. Get an object's prototype: `Object.getPrototypeOf()`
1. Create object with specific prototype: `Object.create(desired_prototype)`

If you put the keyword *new* in front of a function call, the function is treated as a `constructor`. This means that an object with the right prototype is automatically created, bound to `this` in the function, and returned at the end of the function.

Constructors *(all JavaScript functions in fact)* automatically get a property named prototype, which by default holds a plain, empty object that derives from `Object.prototype`.

JavaScript classes are constructor functions with a prototype property

When you add a property to an object, whether it is present in the prototype or not, the property is added to the object itself. If there was already a property with the same name in the prototype, this property will no longer affect the object, as it is now hidden behind the object’s own property.

```javascript
let a = new Map()

a.set('name', "Some name")
a.has('book') // false
```

`Object.keys(<object>)` returns an object's keys.

`object.hasOwnProperty('property_name')` checks if the property is present in an object. It ignores the properties derived from the object's prototype. Use it in place of the `in` operator.

```javascript
console.log({x: 1}.hasOwnProperty("x"));// → true
console.log({x: 1}.hasOwnProperty("toString"));// → false
```

### `let` vs `const`

`let` block scoped; can be reassigned; can’t be redeclared in the same scope
`const` function scoped; must be assigned an initial value; can’t be redeclared in the same scope; can’t be reassigned.
