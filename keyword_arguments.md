#Keyword arguments

`*args` and `*kwargs` are common idioms of Python for using the `*` and `**` notation. These specific variable names are not required (e.g., you can use `*foos` and `**bars`), but generally recommended.

The `*args` will give you all function parameters as a tuple:

```
def foo(*args):
    print args

foo(1, 2, 3)
```
output:
```
(1, 2, 3)
```

The `*kwargs` will give you all keyword arguments except for those corresponding to a formal parameter as a dictionary:
```
def foo(*kwargs):
    print kwargs

foo(a=1, b=2, c=3)
```
output:
```
{a=1, b=2, c=3}
```

Both idioms can be mixed with normal arguments to allow a set of fixed and some variable arguments:
```
def 
```