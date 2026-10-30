## Week 4

"""
4.1 Comments, Code blocks and conditionals
This is Week four for TMXY173 Control Structures in Python
This below me is a mutli string comment while
"""

# The text below which is the one I'm currently writing on is a single line comment with only one hastag

# 4.1.2 If statements, conditional logic and blocks
"""
x = 12
if x < 10:
    print("X is less then 10")
elif x > 10:
    print("X is bigger than 10")
else:
    print("Ignore the rest above")
"""
"""
4.2.1 Conditional Values
Logical Operator: An operator such as and, or, or not, used to combine or modify boolean expression


Alter the X variable of your choice and it will indicate which conditionals sentence it will print out in the console.

Equality == This is used if two variables match it will convert to a true meaning its truthful, correct

Inequality, != Resolves to False if two values are equal

Greater than > = 

"""


#4.2.3 Match Syntax

# A control structure that is pushed to v3.10 of PY for pattern recognition, similar to switch case like C# and JavaScript

#Alternative to If-Elif-Else -> More cleaner, functional method compared to just
"""
month = 'January'
match month:
    case 'January':
        print("Xmas is done, time to go back to work.")
    case 'March':
        print('Time to pay attention to the garden again!')
    case _:
        print("Bit of a monthly month")

"""
## Activity 4.2 Practical
"""

day = "Monday"
match day:
    case 'Saturday':
        print("This is the weekend; Try Again")
    case 'Tuesday':
        print("This is the second day of the week try again")
    case 'Monday':
        print("This is the correct one, well done")
    case '_':
        print("End")

"""

#4.3.1 The for Loop
"""
array = [3, 6, 9, 12]
for i in array:
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1
    ## If you do =+ 1 it will end in an loop constantly | removing the count line 78 loops to 0

"""

"""
Loop Control Statements

What is a break - it's a control statement that is used to exit a loop prematurely, in more detail, if the conditions are met, it closes the loop and exists code
What is continue - A control statement that skips the current iteration of a loop and proceeds with the next iteration

"""

## Activity 4.4

#Question 1
for i in range(11):
    print( i * 2)

#Question 2
number = 100
while number > 0:
    print(number)
    number -=1

#Question 3

hello = [i for i in range(100)]
print(hello)


for i in range(100):
    if i > 50:
        break
    print(i)


my_list = []

f = 5
my_list.append(f)