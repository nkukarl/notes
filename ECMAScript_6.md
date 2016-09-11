#let

###`let` replaces `var`
```javascript
let a = 5;
console.log(a);
```
Output:
```
5
```

###Scope of `let`
Surrounding curly braces define the scope
```javascript
let a = 5;
console.log(a);
function func() {
    let a = 3;
    console.log(a);
}
func();
console.log(a);
```
Output:
```
5
3
5
```
*Note:* If `let a = 3;` is removed, the 2nd `console.log(a);` cannot find `a`. Hence it will look for `a` in the next hierarchy and the output would then be
```
5
5
5
```

###Invisible `{}`
```javascript
let a = 5;
console.log(a);
if (1 === 1) {
    let a = 3;
    console.log(a);
}
console.log(a);
```
Output:
```
5
3
5
```
*Note:* For `if` statement with a single line of code between the curly braces, the curly braces can be omitted. However, the scope is still defined by the 'invisible' curly braces.

#Arrow functions

###Arrow functions replace the traditional way of defining functions.
Traditional way:
```javascript
function circleArea(r) {
    var PI = 3.14;
    return PI * r * r;
}
```
Now:
```javascript
let circleArea = (r) => {
    const PI = 3.14;
    return PI * r * r;
}
```

###Syntax explanation:
- `let <function name> = (<arg1>, <arg2>, ...) => {<function body>}`
- If there is only one argument, `()` can be omitted
- If there is only one statement in `<function body>`, `{}` can be omitted
- Use `const` when defining constants (avoid using `var`)

#Template literals

###Construct strings
```javascript
let name = 'John';
let age = 5;
```
Traditional way:
```javascript
console.log('Hi, my name is ' + name + ' and I am ' + age + ' years old.');
```
Now:
```javascript
console.log('Hi, my name is ${name} and I am ${age} years old.');
```

###Add line break
```javascript
console.log('template literals make it easier to add
new lines');
```
Output:
```
template literals make it easier to add
new lines
```

#Spread operator

###Spread an array into multiple variables
```javascript
let addNumbers = (a, b, c) => {
    console.log(a + b + c);
}
let nums = [3, 4, 5];
```
Traditional way:
```javascript
addNumbers(nums[0], nums[1], nums[2]);
```
Now:
```javascript
addNumbers(...nums);
```

###Combine two arrays
```javascript
let a = ['red', 'green', 'black', 'yellow']
let b = ['cyan', 'purple', 'magenta']
let c = ['red', 'green', ...b, 'black', 'yellow']
console.log(c);
```
Output:
```
['red', 'green', 'cyan', 'purple', 'magenta', 'black', 'yellow']
```

#Class

###Syntax
```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    displayName() {
        console.log(this.name);
    }
    displayAge() {
        console.log(this.age);
    }
}
let john = new Person('John', 25);
john.displayName();
let jane = new Person('Jane', 18);
jane.displayAge();
```
Output:
```
John
18
```

###Inheritance
```javascript
class Engineer extend Person {
    constructor(name, age, skill) {
        super(name, age);
        this.skill = skill
    }
    displaySkill() {
        console.log(this.skill);
    }
}
let jack = new Engineer('Jack', 40, 'CORBA');
jack.displaySkill();
```
Output:
```
CORBA
```

#Generators

```javascript
function* myGenerator() {
    yield 'red';
    yield 'yellow';
    console.log('Line after yellow here!')
    yield 'green';
}
let mg = myGenerator();
```
Iteratively call
```javascript
console.log(mg.next());
```
Output:
```
Object {value: "red", done: false}
```
```
Object {value: "yellow", done: false}
```
```
Line after yellow here!
Object {value: "green", done: false}
```
```
Object {value: undefined, done: true}
```

Source: [Youtube](http://bit.ly/2cl5i3F)