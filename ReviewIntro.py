## Single line comments start with a number symbol.
## First of all, remember to import your libraries.

import datetime

""" Multiline strings can be written
    using three "s, and are often used
    as documentation.
"""

## Printing a message
print("Hello World!")

## Variables in Python are dynamically typed. 
## That means you don't need to declare the type of the variable. 
## But also, you can change the type of the variable later in the code. 
name = "Breno"
age = 31

## Print variables
print("My name is " + name + " and I am " + str(age) + " years old.")

## Dynamic age calculation based on birth date
birth_date = "1993-06-22"

## Convert birth date to datetime object
birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

## Calculate age considering months and days
today = datetime.datetime.now()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

## Print calculated age and line break
print("My name is " + name + " and I am " + str(age) + \
      " years old. This was calculated dynamically based on my birth date.")

## Using conditional statements
## Calculate if today is weekday or weekend
if today.weekday() < 5:
    print("Today is a weekday.")
else:
    print("Today is a weekend.")

# String operations examples
print("Hello world!"[0])      # First character: 'H'
print("Hello world!"[-1])     # Last character: '!'
print("Hello world!"[0:5])    # First five characters: 'Hello'

## Using f-strings (formatted string literals)
cat_name = "Atena"
print(f"My cat's name is {cat_name}.")
print(f"{cat_name} is {len(cat_name)} characters long.")