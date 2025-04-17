## Python Collections Review

# Lists - ordered, mutable, allows duplicates
fruits = ["apple", "banana", "orange", "apple"]
print("\nLists:")
print(f"Original list: {fruits}")
fruits.append("grape")        # Add item
print(f"After append: {fruits}")
fruits.remove("apple")        # Remove first occurrence
print(f"After remove: {fruits}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"Sliced list: {fruits[1:3]}")  # Items from index 1 to 2

# Tuples - ordered, immutable, allows duplicates
coordinates = (10, 20)
print("\nTuples:")
print(f"Coordinates: {coordinates}")
x, y = coordinates           # Tuple unpacking
print(f"X: {x}, Y: {y}")

# Sets - unordered, mutable, no duplicates
numbers = {1, 2, 2, 3, 4, 4, 5}
print("\nSets:")
print(f"Set (notice no duplicates): {numbers}")
numbers.add(6)              # Add item
print(f"After adding 6: {numbers}")
numbers.remove(1)           # Remove item
print(f"After removing 1: {numbers}")

# Dictionaries - key-value pairs, unordered, mutable
person = {
    "name": "Breno",
    "age": 31,
    "city": "São Paulo"
}
print("\nDictionaries:")
print(f"Original dictionary: {person}")
person["email"] = "example@email.com"  # Add new key-value pair
print(f"After adding email: {person}")
print(f"Name: {person['name']}")
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")

# List comprehension
squares = [x**2 for x in range(5)]
print("\nList Comprehension:")
print(f"Squares of numbers 0-4: {squares}")

# Dictionary comprehension
square_dict = {x: x**2 for x in range(5)}
print("\nDictionary Comprehension:")
print(f"Number-square pairs: {square_dict}")