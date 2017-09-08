# 1) Declare two variables, a string and an integer
# named "fullName" and "age". Set them equal to your name and age.

fullName = "Scott Anderson"
age = 51

# 2) Declare an empty array called "myArray".
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.

myArray = []

myArray.append(fullName)
myArray.append(age)

print myArray

print fullName.split()

import datetime
now = datetime.datetime.now()
currentYear = now.year

def myAge(yearBorn):
    print (currentYear - yearBorn)

def sayName():
    print "Hello, %s" % fullName.split()[0]

sayName()
myAge(1966)

In the beginning...alpha Omega
