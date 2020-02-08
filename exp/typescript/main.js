"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
exports.__esModule = true;
var isBeginner = true;
var name = 'Chidi Orji';
var age = 33;
var sentence = "My name is " + name + ".\nI am " + age + " years old.\nI am a typescript beginner.";
var n = null;
var u = undefined;
// array types
var ages = [31, 33, 50]; // array type
var ages2 = [31, 33, 50]; // array type syntax 2
// mixed type arrays (tuple type)
var person = ['Chidi', 33];
// this has a lot of limitations as the value must match the type declaration exactly, both in length and order
// enum type (for a set of numberic values)
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
var Color2;
(function (Color2) {
    Color2[Color2["Red"] = 10] = "Red";
    Color2[Color2["Green"] = 11] = "Green";
    Color2[Color2["Blue"] = 12] = "Blue";
})(Color2 || (Color2 = {})); // starts the enumeration at value 10
var c = Color.Blue;
var c2 = Color2.Blue;
console.log(c); // 2
console.log(c2); // 12
console.log(sentence);
// Any type, for when the value's type is uncertain
var a = 'Whatever';
console.log(a); // Whatever
a = 5;
console.log(a); // 5
// The problem with the any type is that the compiler throws no warnings for the below situations, which may eventually error out during execution
console.log(a.name);
// console.log(a.toUpperCase()); // TypeError: a.toUpperCase is not a function
// console.log(a());
var un = 'Whatever';
console.log(un); // Whatever
un = 5;
console.log(un); // 5
console.log(un.toExponential()); // 5e+0
function hasAge(obj) {
    return !!obj &&
        typeof obj === 'object' &&
        "age" in obj;
}
var abc = 'Whatever';
console.log(abc); // Whatever
abc = 5;
console.log(abc); // 5
console.log(abc.toExponential()); // 5e+0
// console.log('ab c', abc.age) // Property 'age' does not exist on type unknown
if (hasAge(abc)) {
    console.log(abc.age); // no warning
}
var g = 20;
// g = 'whatever'; // type 'whatever` is not assignable to type number
var multi;
multi = 5;
multi = '5';
function multiplier(a, b) {
    var multi;
    b ? multi = "" + a * b : multi = "" + a;
    return multi;
}
;
console.log(multiplier(5, 4)); // 20
console.log(multiplier(5)); // 20
// intellisense shows us the variable types and the return value type
// with default parameter
function multiple(a, b) {
    if (b === void 0) { b = 2; }
    return "" + a * b;
}
;
console.log(multiple(5, 5)); // 25
console.log(multiple(5)); // 10
function AnimalAndSound(animal) {
    return animal.name + " makes sound " + animal.sound;
}
;
console.log(AnimalAndSound({ name: 'goat', sound: 'bleat' })); // goat makes sound bleat
console.log(AnimalAndSound({ name: 'donkey', sound: 'bray' })); // donkey makes sound bray
var Child = /** @class */ (function () {
    function Child(name) {
        this.childName = name;
    }
    ;
    Child.prototype.runToSchool = function () {
        console.log(this.childName + " is running to school");
    };
    return Child;
}());
var child1 = new Child('Chidiebere');
console.log(child1.childName); // Chidiebere
child1.runToSchool(); // Chidiebere is running to school
var SeniorChild = /** @class */ (function (_super) {
    __extends(SeniorChild, _super);
    // recieves a name which is passed to the parent class for initialization
    function SeniorChild(seniorChildName) {
        return _super.call(this, seniorChildName) || this;
    }
    SeniorChild.prototype.playSports = function () {
        console.log(this.childName + " is a senior child and plays sports");
    };
    return SeniorChild;
}(Child));
var senior = new SeniorChild('Eze');
console.log(senior.childName); // Eze
senior.runToSchool(); // Eze is running to school
senior.playSports(); // Eze is a senior child and plays sports
