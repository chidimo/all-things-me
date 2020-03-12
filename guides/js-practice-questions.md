# Eloquent JavaScript questions and answers

## Chapter 2: Program structure

 Write a program that uses console.log to print all the numbers from 1 to 100, with two exceptions. For numbers divisible by 3, print "Fizz" instead of the number, and for numbers divisible by 5 (and not 3), print "Buzz" instead.

When you have that working, modify your program to print "FizzBuzz" for numbers that are divisible by both 3 and 5 (and still print "Fizz" or "Buzz" for numbers divisible by only one of those).

```javascript
function fizzBuzz() {
  for (let i = 1; i <= 100; i ++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log(`FizzBuzz:  ${i}`)
    } else if (i % 3 === 0) {
        console.log(`Fizz: ${i}`)
    } else if (i % 5 === 0) {
        console.log(`Buzz: ${i}`)
    } else {
        console.log(i)
    }
  }
}
fizzBuzz()
```

Write a loop that makes seven calls to console.log to output the following triangle:

```cmd
  #
  ##
  ###
  ####
  #####
  ######
  #######
```

```javascript
let tree = ""
for (let i = 0; i <= 7; i += 1) {
    tree += "#"
    console.log(tree)
}
```

Write a program that creates a string that represents an 8×8 grid, using newline characters to separate lines. At each position of the grid there is either a space or a "#" character. The characters should form a chessboard.

Passing this string to console.log should show something like this:

```cmd
  #-#-#-#-#
  -#-#-#-#
  #-#-#-#-#
  -#-#-#-#
  #-#-#-#-#
  -#-#-#-#
  #-#-#-#-#
  -#-#-#-#
```

When you have a program that generates this pattern, define a binding size = 8 and change the program so that it works for any size, outputting a grid of the given width and height.

```javascript
function makeGrid(width, height) {

  // vertical
  for (let j = 1; j <= height; j ++) {
    if (j % 2 === 0) { // set the start string
      st = ""
    }else {
      st = "#"
    }
    // Horizontal lines
    for (let i = 1; i <= width; i ++) {
      if (i % 2 === 0) {
          st = st + "#"
      }else {
          st = st + "-"
      }
    }
    console.log(st)
  }
}
makeGrid(8, 8)
```

## Chapter 3: Functions

We’ve seen that `%` (the remainder operator) can be used to test whether a number is even or odd by using `% 2` to see whether it’s divisible by two. Here’s another way to define whether a positive whole number is even or odd:

```cmd
  Zero is even.
  One is odd.
  For any other number N, its evenness is the same as N - 2.
```

Define a recursive function `isEven` corresponding to this description. The function should accept a single parameter (a positive, whole number) and return a Boolean.

```javascript
isEven = (n) => {
  if (n === 0) {return true}
  if (n === 1) {return false}
  if (n < 0) {return isEven(-n)}
  return isEven(n - 2)
}
console.log(isEven(50)); // → true
console.log(isEven(75)); // → false
```

You can get the Nth character, or letter, from a string by writing "string"[N]. The returned value will be a string containing only one character (for example, "b"). The first character has position 0, which causes the last one to be found at position string.length - 1. In other words, a two-character string has length 2, and its characters have positions 0 and 1.

Write a function countBs that takes a string as its only argument and returns a number that indicates how many uppercase “B” characters there are in the string.

Next, write a function called countChar that behaves like countBs, except it takes a second argument that indicates the character that is to be counted (rather than counting only uppercase “B” characters). Rewrite countBs to make use of this new function.

```javascript
countBs = (string) => {
  Bcounter = 0
  for (let i = 0; i < string.length; i++){
    if (string[i] === "B") {
      Bcounter += 1
    }
  }
  return Bcounter
}

countChar = (string, letter) => {
  charCounter = 0
  for (let i = 0; i < string.length; i++){
    if (string[i] === letter) {
      charCounter += 1
    }
  }
  return charCounter
}

countBsV2 = (string) => {
  return countChar(string, "B")
}

console.log(countBs("BBCBBB")); // → 2
console.log(countChar("kakkerlak", "k")); // → 4
```

Write a range function that takes two arguments, start and end, and returns an array containing all the numbers from start up to (and including) end.

```javascript
range = (start, end) => {
  if (start > end) {
    return "Start cannot be greater than end."
  };
  let arr = [];
  for (let i = start; i <= end; i++) {
    arr.push(i)
  }
  return arr
}
```

Next, write a sum function that takes an array of numbers and returns the sum of these numbers. Run the example program and see whether it does indeed return 55.

```javascript
sum = array_of_numbers => {
  s = 0;
  for (let number of array_of_numbers) {
    s += Number(number)
  }
  return s
}
```

As a bonus assignment, modify your range function to take an optional third argument that indicates the “step” value used when building the array. If no step is given, the elements go up by increments of one, corresponding to the old behavior. The function call range(1, 10, 2) should return [1, 3, 5, 7, 9]. Make sure it also works with negative step values so that range(5, 2, -1) produces [5, 4, 3, 2].

```javascript
range = (start, end, step) => {
  if (!step){ step = 1 } // set default step value

  if ((start > end) && (step > 0)) {
    return "Start cannot be greater than end when step is positive."
  }
  if ((start < end) && (step < 0)) {
    return "Start cannot be less than end when step is negative."
  }

  let arr = [];
  if (step > 0) {
    for (let i = start; i <= end; i+=step) {
      arr.push(i)
    }
  }
  else {
    for (let i = start; i >= end; i+=step) {
      arr.push(i)
    }
  }
  return arr
}

console.log(range(1, 10)); // → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
console.log(range(5, 2, -1)); // → [5, 4, 3, 2]
```

Arrays have a reverse method that changes the array by inverting the order in which its elements appear. For this exercise, write two functions, `reverseArray` and `reverseArrayInPlace`. The first, `reverseArray`, takes an array as argument and produces a new array that has the same elements in the inverse order. The second, `reverseArrayInPlace`, does what the reverse method does: it modifies the array given as argument by reversing its elements. Neither may use the standard reverse method.

```javascript
function reverseArray(array) {
  // Reverse an array. Reversed array is a new array item.
  let arr = []
  for (i = array.length-1; i >= 0; i--) {
    arr.push(array[i])
  }
  return arr
}

function reverseArrayInPlace(array) {
  // Reverse an array in place by looping over half length of the array
  let l = array.length
  iteration_length = Math.floor(array.length/2)

  for (let i = 0; i < iteration_length; i++) {
    first = array[i], second = array[l-1-i], temp_first_holder = array[i]
    array[i] = array[l-1-i] // reassign position i
    array[l-1-i] = temp_first_holder // reassign counterpart of i from RHS
  }
  return array
}
```

Write a function `arrayToList` that builds up a `list` structure like the one shown above when given `[1, 2, 3]` as argument. Also write a `listToArray` function that produces an array from a list.

Add a helper function prepend, which takes an element and a list and creates a new list that adds the element to the front of the input list, and `nth`, which takes a list and a number and returns the element at the given position in the list (with zero referring to the first element) or undefined when there is no such element.

If you haven’t already, also write a recursive version of `nth`.

```javascript
arrayToList = (array) => {
  r = {value: array[array.length-1], rest: null}
  for (let i = array.length-2; i >= 0; i--) {
        r = {value: array[i], rest: r}
      }
    return r
}
console.log(arrayToList([10, 20, 30])); // → { value: 10, rest: { value: 20, rest: { value: 30, rest: null } } }

listToArray = (list) => {
    let array = []

    while (true) {
        array.push(list.value)
        if (list.rest === null) { break }
        list = list.rest
    }
    return array
}

prepend = (element, list) => {
    // Add a new element to the front of the input list
    new_list = {value: element, rest: list}
    return new_list
}

nth = (list, position) => {
    // returns list element at position
    // assume position is a positive integer

    if (!position) { return undefined }
    if (position < 0) { return undefined }

    for (i = 0; i <= position; i++) {
        if (list.rest === null) { // check if we've reached the last element of the list
            // check if the required position is greater than the index of the
            // last element of the list
            if (position > i) {
                return undefined
            }
        }
        value = list.value
        list = list.rest // when we reach the end of the list, this evaluates to null
    }
    return value
}

console.log(nth(arrayToList([10, 20, 30]), 1)); // -> 20
console.log(prepend(50, t))
}
```

## Deep comparison

The `==` operator compares objects by identity. But sometimes you’d prefer to compare the values of their actual properties.

Write a function `deepEqual` that takes two values and returns `true` only if they are the same value or are objects with the same properties, where the values of the properties are equal when compared with a recursive call to `deepEqual`.

To find out whether values should be compared directly (use the `===` operator for that) or have their properties compared, you can use the `typeof` operator. If it produces `object` for both values, you should do a deep comparison. But you have to take one silly exception into account: because of a historical accident, `typeof` null also produces `object`.

The `Object.keys` function will be useful when you need to go over the properties of objects to compare them.

```javascript
// Your code here.
function deepEqual(object1, object2) {
    if (object1 === object2) { equality = true }
    // two null objects are not equal to each other
    let o1 = (typeof object1 == "object") && (object1 != null)
    let o2 = (typeof object2 == "object") && (object2 != null)

    if (o1 && 02) {
        // perform deep comparison
        obj_1_keys = Object.keys(object1)
        obj_2_keys = Object.keys(object2)

        // key length check
        if (obj_1_keys.length == obj_2_keys.length) {
            equality = true
        }
        else {
            return false
        }

        // check properties
        for (prop of obj_1_keys) {
            if (obj_2_keys.includes(prop)) {
            }
            else {
                return false
            }
        }

        // property values check: if both values are objects, do a recursive check
        for (key in object1) {
            a = object1[key]
            b = object2[key]

            // check if these values are objects
            let a1 = (typeof a == "object") && (a != null)
            let b1 = (typeof b == "object") && (b != null)
            if (a1 && b1) {
                console.log("recursing for objects ", a, "and ", b)
                return deepEqual(a, b)
            }

            else {
                if (object1[key] == object2[key]) {
                    equality = true
                }
                else {
                    return false
                }
            }
        }
    }
    else {
        equality = true
    }
    return equality
}

// a more concise version: not finished yet
function deepEqual(a, b) {
    if (a === b) { equality = true }
    // two null objects are not equal to each other

    if (a == null || b == null || typeof a != "object" || typeof b != "object") { return false }

    // perform deep comparison
    keysA = Object.keys(a), keysB = Object.keys(b)

    // key length check
    if (keysA.length == keysB.length) {
        equality = true
    }
    else { return false }

    // check properties
    for (prop of keysA) {
        if (keysB.includes(prop)) {
        }
        else { return false }
    }

    // property values check: if both values are objects, do a recursive check
    for (key in a) {
        a1 = a[key], b1 = b[key]
        // check if these values are objects
        if (a1 == null || b1 == null || typeof a1 != "object" || typeof b1 != "object") { return false }
        console.log("recursing for objects ", a1, "and ", b1)
        return deepEqual(a1, b1)
    }
    return equality
}

let obj = {here: {is: "an"}, object: 2};

console.log(deepEqual(obj, obj)); // → true
console.log("*".repeat(50))
console.log(deepEqual(obj, {here: 1, object: 2})); // → false
console.log("*".repeat(50))
console.log(deepEqual(obj, {here: {is: "an"}, object: 2})); // → true
console.log("*".repeat(50))
console.log(deepEqual(obj, {here: {is: "ann"}, object: 2})); // → false
```

## Chapter 5

Use the `reduce` method in combination with the `concat` method to “flatten” an array of arrays into a single array that has all the elements of the original arrays.

```javascript
let arrays = [[1, 2, 3], [4, 5], [6]];
console.log(arrays.reduce( (a, b) => a.concat(b) )) // → [1, 2, 3, 4, 5, 6]
```

Write a higher-order function `loop` that provides something like a for loop statement. It takes a value, a test function, an update function, and a body function. Each iteration, it first runs the test function on the current loop value and stops if that returns false. Then it calls the body function, giving it the current value. Finally, it calls the update function to create a new value and starts from the beginning.

When defining the function, you can use a regular loop to do the actual looping.

```javascript
function loop(value, test_func, update_func, body_func) {
  console.log("Loop called")
  for (let i = value; i >= 0; i--) {
    if (!test_func(i)) {return}
    else {
        body_func(i)
    }
    update_func(i)
  }
}

loop(3, n => n > 0, n => n - 1, console.log);
// → 3
// → 2
// → 1
```

Analogous to the `some` method, arrays also have an `every` method. This one returns `true` when the given function returns `true` for every element in the array. In a way, some is a version of the `||` operator that acts on arrays, and every is like the `&&` operator.

Implement `every` as a function that takes an array and a predicate function as parameters. Write two versions, one using a loop and one using the some method.

```javascript
function every(array, test) {
    // implementation 1: loop
    r = true
    for (let element of array) {
        if (test(element)) {
            r = true
        }
        else {
            return false
        }
    }
    return r
}

function every(array, test) {
  // implementation 2: using some
    r = []
    for (let element of array) {
        if (test(element)) {
            r.push(true);
        }
        else {
            r.push(false);
        }
    }
    if (r.some(t => t == false)) {
        return false
    }
    else {
        return true
    }
}
console.log(every([1, 3, 5], n => n < 10)); // → true
console.log(every([2, 4, 16], n => n < 10)); // → false
console.log(every([], n => n < 10)); // → true
```

Write a function that computes the dominant writing direction in a string of text. Remember that each script object has a direction property that can be "ltr" (left to right), "rtl" (right to left), or "ttb" (top to bottom).

The dominant direction is the direction of a majority of the characters that have a script associated with them. The `characterScript` and `countBy` functions defined earlier in the chapter are probably useful here.
