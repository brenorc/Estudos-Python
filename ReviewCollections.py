############ LISTS ############

## Lists store sequences with order
my_list = []

## You can start with a prefilled list
other_list = [4, 5, 6]

## You can add elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(4)
my_list.append(3)

print("The list is now: ", my_list)

## Remove from the end with pop
my_list.pop()        # => 3 and list is now [1, 2, 4]

print("The list is now: ", my_list)
print("The first element is: ", my_list[0])
print("List in reverse order is: ", my_list[::-1]) 

############ TUPLES ############

## Tuples are like lists but are immutable.
tuple = (1, 2, 3)
tuple[0]      # => 1

"""
tuple[0] = 3  # Raises a TypeError
"""

## You can do most of the list operations on tuples too
len(tuple)         # => 3
tuple + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tuple[:2]          # => (1, 2)
2 in tuple         # => True

## You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3

############ DICTIONARIES ############

## Dictionaries store mappings from keys to values
empty_dict = {}

## Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}


## Note keys for dictionaries have to be immutable types. This is to ensure that
## the key can be converted to a constant hash value for quick look-ups.
## Immutable types include ints, floats, strings, tuples.
## invalid_dict = {[1,2,3]: "123"}  # => Yield a TypeError: unhashable type: 'list'

## You can check if a key exists in a dictionary
print("Is the key 'one' in the dictionary? Answer: ", "one" in filled_dict)  # => True

# Adding to a dictionary
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict

print("The dictionary is now: ", filled_dict)

# Get all keys as an iterable with "keys()".
print("The keys are: ", list(filled_dict.keys()))

# Get all values as an iterable with "values()".
print("The values are: ", list(filled_dict.values()))

# Get all key-value pairs as an iterable of tuples with "items()".
print("The key-value pairs are: ", list(filled_dict.items()))


############ SETS ############

## Sets store unique values
empty_set = set()

## Here is a prefilled set
filled_set = {1, 1, 2, 2, 3, 4}  # filled_set is now {1, 2, 3, 4}
print("The set is: ", filled_set)

# Add one more item to the set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
print("The set is now: ", filled_set)

# Remove an item from the set
filled_set.remove(3)  # filled_set is now {1, 2, 4, 5}
print("The set is now: ", filled_set)

# Do set intersection with &
other_set = {3, 4, 5, 6}
print("The intersection of the two sets is: ", filled_set & other_set)  # => {4, 5}

# Do set union with |
print("The union of the two sets is: ", filled_set | other_set)  # => {1, 2, 3, 4, 5, 6}

# Do set difference with -
print("The difference of the two sets is: ", filled_set - other_set)  # => {1, 2}

# Do set symmetric difference with ^
print("The symmetric difference of the two sets is: ", filled_set ^ other_set)  # => {1, 2, 3, 6}