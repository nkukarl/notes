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

###constructor
The `constructor` method is a special method for creating and initialising an object created with a `class`. If a class contains more than one occurrence of a `constructor` method, a syntax error will be thrown.

[Reference](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes)

###getter
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

[Reference](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Functions/get)
