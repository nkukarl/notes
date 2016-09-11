#Keyword arguments

`*args` and `*kwargs` are common idioms of Python for using the `*` and `**` notation. These specific variable names are not required (e.g., you can use `*foos` and `**bars`), but generally recommended.

The `*args` will give you all function parameters as a tuple:

```python
def foo(*args):
    print args

foo(1, 2, 3)
```
output:
```python
(1, 2, 3)
```

The `*kwargs` will give you all keyword arguments except for those corresponding to a formal parameter as a dictionary:
```python
def foo(*kwargs):
    print kwargs

foo(a=1, b=2, c=3)
```
output:
```python
{a=1, b=2, c=3}
```

Both idioms can be mixed with normal arguments to allow a set of fixed and some variable arguments:
```python
def foo(*args, **kwargs):
    print args
    print kwargs

foo(1, 2, 3, a=4, b=5, c=6)
```
output:
```python
(1, 2, 3)
{a=1, b=2, c=3}
```

*NOTE* `foo(1, 2, a=4, 3, b=5, c=6)` would cause a syntax error `SyntaxError: non-keyword arg after keyword arg`

Another usage of `*` is to unpack argument list when calling a function

```python
def foo(a, b):
    print a
    print b

c = [1, 2]
foo(*c)
```
output:
```python
1
2
```

Source: [Stackoverflow](http://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-python-parameters)
