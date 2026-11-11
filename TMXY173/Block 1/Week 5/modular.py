"""
Functions allow you to encapsulate reusable blocks of code, making your programs more modular and maintainable
"""


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

my_dog = Dog('Buddy', 'Golden Retriever')
print(my_dog.bark())

#The Self keyword is a special reference in Python that always points to the current instance of the class


#The __init__ function is a special built-in function in Python that marks the constructor function


# A constructor is a special method that runs when a new object is created. It sets up the initial state of the object by initialsing attributes
# A instantiation is a process of creating a new instance of an object, typically by calling the constructor

#5.2 Activity Practical

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model =  model
        self.year = year

    def description(self):
        return f'{self.make}, {self.model}, {self.year}'

point = Car('Toyota', 'Corolla', '2007')
print(point.description())


# 5.2.3 Class vs Instance attributes
class Cat:
    species = 'Feline' # Class attribute
    def __init__(self, name):
        self.name = name
cat1 = Cat('Kitty')
cat2 = Cat('Shiraz')

print(cat1.species)
print(cat2.name)


"""
# 1. CLASS (The Blueprint)
# This defines the structure and behavior for all video game characters.
class Character:
    
    # 2. CONSTRUCTOR (The Setup Function)
    # This automatically runs the moment a new character is created.
    def __init__(self, username, character_class):
        
        # 3. ATTRIBUTES (OOP Variables)
        # These store unique data tied directly to each individual instance.
        self.username = username          # A string attribute
        self.character_class = character_class  # Another string attribute
        self.level = 1                    # An integer attribute starting at 1
        self.health = 100                 # A health attribute starting at 100

    # 4. METHODS (OOP Functions)
    # These are functions inside the class that use "self" to interact with the attributes.
    def show_profile(self):
        print(f"--- PROFILE: {self.username} ---")
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health} HP\n")

    def take_damage(self, amount):
        self.health -= amount
        print(f"💥 {self.username} took {amount} damage! Health is now {self.health} HP.")


# ==========================================
# 5. INSTANCES / OBJECTS (The Concrete Items)
# ==========================================

# We use the blueprint to create two completely separate characters in memory.
player1 = Character(username="ShadowNinja", character_class="Rogue")
player2 = Character(username="MerlinTheGreat", character_class="Wizard")

# Let's interact with our instances to see how everything works together:

# Calling methods on player1
player1.show_profile()

# Accessing a specific attribute on player2 directly using dot notation
print(f"Checking data: player2's class is {player2.character_class}.\n")

# Calling a method that modifies an attribute on player1
player1.take_damage(25)
print(f"Direct check: player1 health is now {player1.health} HP.")

"""


#.5.2.4 The__str__method

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def __str__(self):
        return f"{self.make} {self.model}"
my_car = Car('Toyota', 'Corolla')
print(my_car) # Output: Toyota Corolla


#5.2.5 Inheritance
# What is inheritance: Inheritance is a feature of object-oriented programming where a class can inherit attributes and methods from another class=
class Animal:
    def speak(self):
        return "Sound"
    def alive(self):
        return True
class Cow(Animal):
    def speak(self):
        return "Moooo"
my_cow = Cow()
print(my_cow.alive()) # Output: True
print(my_cow.speak()) # Output: Moooo


"""
5.3 Instant functions: an introduction to lambdas
In python, lamda functions provide a concise way to create a function. Unlike standard functions using def syntax, lambdas are anonmyous functions, essentially not needing def syntax
they are short functions 

5.3.1 
the basic syntax of a lambda function is lambda argument:expression
e.g 3 * x

tripler = lambda x: 3 * x
print(tripler(5))
"""

#5.3.4 Examples and activities
numbers = [1,2,3,4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)