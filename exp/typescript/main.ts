export {}

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

// Any type, for when the value's type is uncertain
let a: any = 'Whatever';
console.log(a) // Whatever
a = 5;
console.log(a) // 5

// The problem with the any type is that the compiler throws no warnings for the below situations, which may eventually error out during execution

console.log(a.name);
// console.log(a.toUpperCase()); // TypeError: a.toUpperCase is not a function
// console.log(a());

let un: unknown = 'Whatever';
console.log(un) // Whatever
un = 5;
console.log(un) // 5

console.log((un as number).toExponential()); // 5e+0

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

// console.log('ab c', abc.age) // Property 'age' does not exist on type unknown

if (hasAge(abc)) {
    console.log(abc.age) // no warning
}

let g = 20;
// g = 'whatever'; // type 'whatever` is not assignable to type number

let multi: string | number;
multi = 5;
multi = '5';


function multiplier(a: number, b?: number): string {
    let multi: string;
    b ? multi = `${a * b}` : multi = `${a}`;
    return multi;
};

console.log(multiplier(5, 4)); // 20
console.log(multiplier(5)); // 20
// intellisense shows us the variable types and the return value type


// with default parameter
function multiple(a: number, b: number = 2): string {
    return `${a * b}`
};
console.log(multiple(5, 5)); // 25
console.log(multiple(5)); // 10

// in the example below, the `Animal` interface is the type supplied to the `AnimalAndSound` function.

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
