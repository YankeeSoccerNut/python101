# Step 1...hard code the secretNumber, unlimited guesses

secretNumber = 3
keepGoing = True

print "I'm thinking of a number between 1 and 10."

while ( keepGoing == True ):
    guess = raw_input ("What's the number? ")
    if ( int(guess) == secretNumber ):
        print "Yes!  You win!"
        keepGoing = False
    else:
        print "Nope, try again."
