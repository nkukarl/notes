from functools import partial

def foo(a, b, c):
	print a, b, c

# create partial function, let b=1 and c=2
p_foo = partial(foo, b=1, c=2)

# for p_foo, only provide one argument, 3 is assigned to a
p_foo(3)

# provide two arguments, explicitly mention b=4 to overwrite b=1
# in the definition of p_foo
p_foo(3, b=4)

# similar as above
p_foo(3, c=5)

# TypeError: foo() got multiple values for keyword argument 'b'
p_foo(3, 2)
