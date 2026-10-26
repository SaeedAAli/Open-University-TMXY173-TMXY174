username = 'Alice'
usertext = username
username = 'Bertie'

print(usertext)


name = "Saeed"
age = 19
flag = "British"

print(name)
print(age)
print(flag)


x = 42

print((type(x)))



## Activity 3.5 Self Assesment
x = '123'
y = int(x)
print(y + 1)
z = str(y)
print(z + '1')

## The reason why there is a 1231 and not 1241 is becuase the last print command line is doing addition
    ##-> ## Since the y variable is 123 and that its a string and not quotation
        ## the z variable uses that variable string that is stored in the z var which is '123' essentially in this whole jargon, using outdated numbers pretty much
## ------


## Activity 3.6 Practical

number = 10
word = "Dante"
decimal = 1.5
bools = True


print(type(number))
print(type(word))
print(type(decimal))
print(type(bools))


i = [number, word, decimal, bools]

print(i)

holt = {"name": "Kendall", "age": 21, "grades": [85,90,78]}


combination = holt

print(combination)

## Activity 3.8

width = 7.5
height = 3

area = width * height
print(area)

number1 = 29

q2 = number1 / 5
print(q2)

exponenation = 2 ** 5
print(exponenation)


result = 10 // 3
print (result)
    ##It differs since you're looking for a remainder not a whole number



#Activtiy 3.9

legal_name = "SAEED ALI"
legal_name[0]

jackpot = print(legal_name[0:5])

##winner = jackpot.replace(str("__________"))

##print(winner)





## Final Activity for Unit 3


Unit3_name = input(str("What is your fall name\n"))
print(Unit3_name)

Unit3_age = str(input("What is your age\n"))
print(Unit3_age)

Unit3_height = float(input("How Tall are you"))
print(Unit3_height)

unit3_mini_exercise = (f"Your name is {Unit3_name} You are {Unit3_age} and your height is {Unit3_height} m ")


print(unit3_mini_exercise)


from datetime import date



age_arithmetic = int(input("How old are you\n"))

user_age = age_arithmetic



learning_score = int(input("What is your learning score\n"))

squared_time = Unit3_age ** learning_score

print(squared_time)







new_name = print(Unit3_name.upper())

extraction = Unit3_name[0: 5]



