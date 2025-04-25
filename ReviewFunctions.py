# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # Return values with a return statement

# Calling functions with parameters
add(5, 6)  # => prints out "x is 5 and y is 6" and returns 11

print(add(5, 6)) 

# You can define functions that take a variable number of
# positional arguments
def varargs(*args):
    return args

print(varargs(1, 2, 3))  # => (1, 2, 3)

# There are also anonymous functions
print((lambda x: x > 2)(3))                  # => True
print((lambda x, y: x ** 2 + y ** 2)(2, 1))  # => 5

# You can also use the "map" function to apply a function to each item in a list
print(list(map(lambda x: x ** 2, [1, 2, 3])))  # => [1, 4, 9]