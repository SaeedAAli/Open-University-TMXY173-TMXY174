"""
Functions allow you to encapsulate reusable blocks of code, making your programs more modular and maintainable
"""
from os import name


def greet():
    print("Hello world")

greet()

for i in range(10):
    greet()
####################################################

#– 5.1.2 Parameters and return value
def add(a:int, b: int):
    return a + b

result = add(3, 5)
print(result)

# Arguments are values that passed into a functions parameter during runtime, essentially what's in between the brackets after defining a function

#5.1.3 Importing modules
# What is importing modules, well it's essentially that if a function is contained in another code file, you cannot call it. To use a function from another file, you must import file as a module Exmaple below
import math
import random
print(math.sqrt(49)) # -> what this does is that it square roots the number


# Activity 5.1 practical

def greet_user(name):
    print(f"Hello, {name}! Welcome.")

greet_user("Alex")

def square(a:float):
    return a

eren = square(math.sqrt(11))
print(eren)


import random
def generator(number: int, number2: int) -> int:
    return random.randint(number, number2)

randomizer = generator(1, 10)
print(randomizer)

#5.1.4 Default parameters and keyword arguments
"""
def greet(name='Guest'):
    print(f"Hello, {name}!")
 
greet() # Output: Hello, Guest!
greet('Alice') # Output: Hello, Alice!

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}")
 
describe_pet(pet_name='Whiskers', animal_type='cat')

"""

#5.1.5 Variable Scope
# The context within which a variable is accessible, such as local or global
# And a Global variable are defined outside functions and that are accessible throughout the program.
# And you have local variables which are defined inside a function meaning they are local to that function and cannot be accessed outside it. this allows the same variable name to be used more than once acorss a project, storing locally relevant information in each case.

"""
#5.2 Object Oriented Programming.
#Key definitions of OOP: A programming paradigm in which a system is modelled as a collection of objects, each of which can contain attributes and methods. This allows the development of efficient and reusable code.

# What is an object: An instance of a class containing data and methods that operate on that data.

# What is an attribute, a variable associated with an object or class that stores data. Some attributes may only be accessed or modified via methods.

# What is a method, a function that is associated with a object and can access and modify the object's data.

"""

#5.2.1 Defining classes and creating objects from classes

# Class: a blueprint for creating objects, encapsulating data and methods.


class Dog:
    def __init__(self, name, breed):
        self.name = breed
        self.breed = breed

def bark(self):
    return f'{self.name} says woof!'