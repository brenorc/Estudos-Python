# Let's just make a variable
some_var = 5

# if statement:
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # This elif clause is optional.
    print("some_var is smaller than 10.")
else:                  # This is optional too.
    print("some_var is indeed 10.")


# for loop
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

for i in range(1,4):
    print(i) # it will print 1,2,3

# loop through a list and get the index and value
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

# Iterating over a string
name = "Oie"
for letter in name:
    print(letter)

# List comprehension
squares = []
for x in range(10):
    squares.append(x ** 2)
# We can simplify by doing this:
squares = [x ** 2 for x in range(10)]

print(squares)

[x for x in range(10) if x % 2 == 0]
# Output: [0, 2, 4, 6, 8]

["even" if x % 2 == 0 else "odd" for x in range(5)]
# Output: ['even', 'odd', 'even', 'odd', 'even']