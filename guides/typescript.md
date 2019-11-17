
# `typescript`

The `tsc` line below converts the `.ts` file into a module. It is placed at the top of the file.

```typescript
exports = {}
```

It compiles to

```javascript
"use string"
exports.__esModule = true;
```

## Variable declarations: `let` vs `const`

`let` declarations can be made without a value, `const` declarations must have a value.
`const` cannot be re-assigned.

## Variable types: `boolean`, `number`, and `string`

Variable types are declared with an colon `:` followed by the variable type. There are two main benefits to using type declarations: `static type checking` and `Intellisense`

```typescript
let isBeginner: boolean = true;
let name: string = 'Chidi Orji';
let age: number = 33;
let sentence: string = `My name is ${name}.
I am ${age} years old.
I am a typescript beginner.`;
let n: null = null;
let u: undefined = undefined

// array types
let ages: number[] = [31, 33, 50] // array type
let ages2: Array<number> = [31, 33, 50] // array type syntax 2

// mixed type arrays (tuple type)
let person:[string, number] = ['Chidi', 33]
// this has a lot of limitations as the value must match the type declaration exactly, both in length and order

// enum type (for a set of numberic values)
enum Color {Red, Green, Blue}
enum Color2 {Red = 10, Green, Blue} // starts the enumeration at value 10
let c: Color = Color.Blue
let c2: Color2 = Color2.Blue
console.log(c) // 2
console.log(c2) // 12
console.log(sentence);
```

### types `any` and `unknown`

`any` type is used for when the value's type is uncertain

```typescript
let a: any = 'Whatever';
console.log(a) // Whatever
a = 5;
console.log(a) // 5
```

The problem with the `any` is that the compiler throws no warnings for the below situations, which may eventually error out during execution

```typescript
console.log(a.name); // undefined
console.log(a.toUpperCase()); // TypeError: a.toUpperCase is not a function
console.log(a()); // TypeError: a is not a function
```

for type `unknown`, we can't access any properties, neither can it be called or constructed

```typescript
let un: unknown = 'Whatever';
console.log(un) // Whatever
un = 5;
console.log(un) // 5
```

all of the below throws a warning

```typescript
console.log(un.name); // Property 'name' does not exist on type 'unknown'
console.log(un.toUpperCase()); // Property 'toUpperCase' does not exist on type 'unknown'
console.log(un()); // Cannot invoke an expression whose type lacks a call signature. Type '{}' has no compatible call signatures.
```

We can use `type assertion` to convince the compiler that we know better

```typescript
let un: unknown = 'Whatever';
console.log(un) // Whatever
un = 5;
console.log(un) // 5
console.log((un as number).toExponential()); // 5e+0
```

It is possible to have user-defined type guards. i.e functions that check for certain types in objects

```typescript
function hasAge(obj: any): obj is { age: number } {
    return !!obj &&
        typeof obj === 'object' &&
        "age" in obj;
}
let abc: unknown = 'Whatever';
console.log(abc) // Whatever
abc = 5;
console.log(abc) // 5
console.log((abc as number).toExponential()); // 5e+0
console.log('ab c', abc.age) // Property 'age' does not exist on type unknown

if (hasAge(abc)) {
    console.log(abc.age) // no warning
}
```

### `type` inference

If we `declare` and `initialize` a variable without an explicit type declaration, `typescript` infers the type for us. Thus, subsequently reassigning the variable will error out if the type does not match that of the originally set value.

```typescript
// this case is fine
let a;
a = 5;
a = 'string'

// inference at work below
let g = 20;
g = 'whatever'; // type 'whatever` is not assignable to type number
```

### specifying multiple `types`; union operator

This is achieved using the pipe `|` character. We can use this to restrict the possible types.

```typescript
let multi = string | number;
multi = 5;
multi = '5';
```

## Functions

1. Intellisense shows us the variable types and the return value type
1. Every function parameter is assumed to be required. Calling a function without a parameter throws an error;
1. Optional parameters are specified with `?` at the end of the parameter name e.g. `name?: string`. Optional parameters must come *after* required parameters
1. Default parameters are set like this `variable: type = value`

```typescript
function multiplier(a: number, b: number): string {
    return `${a * b}`
};
console.log(multiplier(5, 4)); // 20

// with optional parameter
function multiplier2(a: number, b?: number): string {
    let multi: string;
    b ? multi = `${a * b}` : multi = `${a}`;
    return multi;
};
console.log(multiplier2(5)); // 5

// with default parameter
function multiplier3(a: number, b: number = 2): string {
    return `${a * b}`
};
console.log(multiplier3(5, 5)); // 25
console.log(multiplier3(5)); // 10
```

## Interface

These make it possible to specify an `object` as a type. In the example below, the `Animal` interface is the type supplied to the `AnimalAndSound` function.

```typescript

interface Animal {
    name: string;
    sound: string;
    nickname?: string; // optional
}

function AnimalAndSound(animal: Animal) {
    return `${animal.name} makes sound ${animal.sound}`
};

console.log(AnimalAndSound({ name: 'goat', sound: 'bleat'})) // goat makes sound bleat
console.log(AnimalAndSound({ name: 'donkey', sound: 'bray'})) // donkey makes sound bray
```

## Classes and Access Modifiers

1. `access modifiers` are basically keywords that set the a11y of `properties` and `methods` in a class. They are `public`, `private`, and `protected`. By default every class member is public.
1. A `private` class member cannot be accessed from outside it's containing class. This also applies its child classes.
1. A `protected` class member cannot be accessed from outside its containing class but can be accessed from within its child classes.

```typescript
class Child {
    childName: string;

    constructor(name: string) {
        this.childName = name;
    };

    runToSchool () {
        console.log(`${this.childName} is running to school`)
    }
}

let child1 = new Child('Chidiebere');
console.log(child1.childName); // Chidiebere
child1.runToSchool(); // Chidiebere is running to school

class SeniorChild extends Child {
    // recieves a name which is passed to the parent class for initialization
    constructor(seniorChildName: string) {
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
```

## Casting an object to an `interface`

This is just a demo I quickly copied from an angular component to demo how to

1. set a function return type
1. cast object to interface (two ways).

```typescript
import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http'
import 'rxjs/add/operator/map';
import { Observable } from 'rxjs/Observable'

import { Album } from './album'

@Injectable()
export class ProductService {

  private _albumUrl = '../assets/album.json';
  constructor(private _http: Http) { }
  getAlbum(id: number): Observable<Album> {
    // return this._http.get(this._albumUrl).map((response: Response) => response.json() as Album)
    return this._http.get(this._albumUrl).map((response: Response) => <Album> response.json()) // alternative way
  }

}

```
