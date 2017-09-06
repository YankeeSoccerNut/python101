classSize = 19
question = "How big is your class?"
print question
response = raw_input(">")
response_as_int = int(response)

if (response_as_int != classSize):
    print "You must not be in the September class"
else:
    print "Let's start coding!"


import random
secret_number = random.randint(1,10)
print secret_number

keepGoing = True
print "I'm thinking"
while (keepGoing):
