#Javascript Random Notes

## Hoisting
In Javascript, functions and variables are hoisted. Hoisting is Javascript's behaviour of moving declarations to the top of a scope (the global scope or the current function scope).

```javascript
foo = 2;
var foo;

// is implicitly understood as:

var foo;
foo = 2;

```

An important difference between function declarations and class declarations is that function declarations are hoisted and class declarations are not.

[Reference](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting)

## Class

###Constructor
The `constructor` method is a special method for creating and initialising an object created with a `class`. If a class contains more than one occurrence of a `constructor` method, a syntax error will be thrown.

[Reference](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes)

###Getter
The `get` syntax binds an object property to a function that will be called when that property is looked up. For example,
```javascript
class Polygon {
    constructor(height, width) {
        this.height = height;
        this.width = width;
    }
    area() {
        return this.height * this.width;
    }
}

let p = new Polygon(4, 3);
console.log(p.area());
```

If
```javascript
get area() {
        return this.height * this.width;
    }
```
is used, the last line can be replaced by
```javascript
console.log(p.area);
```

Getters gives you a way to define a property of an object, but they do not calculate the property's value until it is accessed. A getter defers the cost of calculating the value until the value is needed, and if it is never needed, you never pay the cost.

[Reference](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Functions/get)

#ES6

##Constants
`const` defines variables which cannot be re-assigned new content. This only makes the variable itself immutable, not its assigned content.

For example,
```javascript
const p = new Polygon(4, 3);
p = new Polygon(7, 3);
```
will throw a TypeError
```javascript
Uncaught TypeError: Assignment to constant variable.
```

However,
```javascript
const p = new Polygon(4, 3);
p.height = 7;
```
can be correctly executed.

###Default Parameter Values
```javascript
let f = (a = 5, b = 7) => {
    console.log(a + b);
};
f(3, 4);
f(3);
```
Output:
```
7
10
```

###Rest Parameter
```javascript
let f = (a, b, ...c) => {
    console.log(c);
    console.log((a + b) * c.length);
};

f(3, 2, "a", "b", "c");
```
Output:
```
["a", "b", "c"]
15
```

###Spread Operator
```javascript
let str = "foo";
let chars = [...str];
console.log(chars);
```
Output:
```
["f", "o", "o"]

###Destructuring Assignment
```javascript
let list = [1, 2, 3];
let [a, , b] = list;
console.log(`a: ${a}, b: ${b}`);
[a, b] = [b, a];
console.log(`a: ${a}, b: ${b}`);
```
Output:
```
a: 1, b: 3
a: 3, b: 1
```

###Set Data Structures
```javascript
let s = new Set();
let list = [1, 2, 3, 1, 4, 2];

for (let n of list) {
    s.add(n);
}

console.log(s);

for (let k of s.values()) {
    console.log(k);
}
```
Output:
```
Set {1, 2, 3, 4}
1
2
3
4
```

###Map Data Structures
```javascript
let m = new Map();
m.set('a', 11);
m.set('b', 22);
m.set('c', 33);

console.log(m.size);
console.log(m.get('a'));

for (let [k, v] of m.entries()) {
    console.log(`${k} -> ${v}`);
}
```
Output:
```
3
11
a -> 11
b -> 22
c -> 33
```

###Array Element Finding
```javascript
let list = [3, 2, 4, 1, 5];
let ans = list.find(x => x < 7);
```
Output:
```
3
```
**N.B.** Only the first one of the elements (if more than one) that meet the criteria will be returned to ans.

###String Repeating
```javascript
"foo".repeat(4);
```

#Random
### Syntactic Sugar
In computer science, syntactic sugar is syntax within a programming language that is designed to make things easier to read or to express. It makes the language "sweeter" for human use. Things can be expressed more clearly, more concisely, or in an alternative style that some may prefer.

###Semicolons
Javascript is a scripting language where semicolons as statement terminators are optional. However, there is a lot of **FUD** (fear, uncertainty and doubt) around this feature. For example, Javascript code cannot be minified without semicolons.

To be continued...
[Reference](http://es6-features.org/)
