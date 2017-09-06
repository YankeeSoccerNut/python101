# Step 2...add a hint to version 1

secretNumber = 3
keepGoing = True

print "I'm thinking of a number between 1 and 10."

while ( keepGoing == True ):
    guess = int(raw_input ("What's the number? "))
    if ( guess == secretNumber ):
        print "Yes!  You win!"
        keepGoing = False
    else:
        if (guess > secretNumber):
            print "%d is too high" % guess
        else:
            print "%d is too low" % guess
