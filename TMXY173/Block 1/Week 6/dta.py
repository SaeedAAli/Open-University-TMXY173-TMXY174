"""def function(num1, num2):
    return num1 +  num2

yes = function(10, 21)
print(yes)


class Dog:
    def __init__(self, make, number):
        self.make = make
        self.number = number
    def description(self):
        print(f'{self.make}'', Collectible iteam and the year that was invovled in is {}' ,f'{self.make}')
domino = Dog('Corolla', '2007')

print(domino.description())

"""

# Data Structures and Algorithms

# What is Data Structure: A particular way of organising and storing data in a computer so that it can be accessed and modified efficiently.
# it conveys from simple concepts from lists and array to more complex queues, maps, and trees. What were going to do is to go more in depth on the built-in structures and python array


# ----------------------------------------------------------------------------------------------------------------------

#6.1 List

# Alist is an ordered mutable(which means that the lists can change) collection that can hold items of any type(int,float,bool,string) List are defined using square brackets

my_list = [1,3,4,5,6]
character = my_list
print(my_list[0]) # The square brackets in between the circular brackets can print out the index of the list so in this case it would print out 1 since this is the 0 index in the list, 0,1,2,3,4

my_list2 = [4,9,1,6,8,8,3]
print(my_list2[1:3]) # What this does is that it slices
print(my_list2[-3:]) # The colon feature in this line is a slicing mechanism where it starts at the first index and stops at the last index
# In this example above, not the negative what it does that it starts at 9 and stops before 6 so if it's essentially 9,1
# The second example is that it's a negative number, but it counts backwords so that it becomes 883 - in short terms, it starts at the very end rather than the very beginning



# 6.1.2 Sets
# A set is an unordered collection of unique elements. Sets are defined using curly braces. They are useful for membership testing and removing duplicates

my_set ={1,2,3,3,2} ## If you want to remove
print(my_set)

definition ={11, 11, 11, 22, 22,22, 33, 33, 44, 44, 44, 55, 55, 55, 66, 66,}   # Essentially what this does is that it removes duplicates from the list so it will only contain one unique number so this will print out 11,22,33,44,55,66 just once
no = sorted(definition)
print(no)


# 6.1.3 Tuples
# What is a tuple, a ordered, immutable collection of elements in python - A immutable object is something that can't be changed where as mutable can be changed
coord = (4,1)
print(f"You hit {coord}", "you've sank my battleship" )

#6.1.4 Dictionaries

# A dictionary is a mutable, unordered, collection of key value in python
# They use curly braces for this

my_dict = {'name': 'Alice', 'age': 30}
print(my_dict['name']) ## Outputs Alice as the name

# 6.1.5 Array
# An array is a data structure that stores elements in a block - for memory’s sake, used efficiently for data handling

import array

my_array = array.array('i', [1,2,3,4])
for i in range(len(my_array)):
    print(my_array)


# 6.1.6 List comprehensions
# A concise way to create lists using a single line of code with a for loop and an optional condition
print([x * x for x in range (5)])

"""
6.1.7 Comparison of data structure
tuples - limited, ordered, mutable, duplicates
lists - ordered, mutable, duplicates
sets - unordered, mutable, no duplicates
dictionaries - key-value pairs, unordered, mutable
array - used for storing num data, uniform type

"""

