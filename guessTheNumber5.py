# Step 5...Bonus...play gain...is using a function cheating?

import random

def playTheGame():
    secretNumber = random.randint(1,10)
    maxGuesses = 5
    numGuesses = 0

    print "I'm thinking of a number between 1 and 10."

    while ( numGuesses < maxGuesses ):
        print "You have %d guesses left." % (maxGuesses - numGuesses)
        guess = int(raw_input ("What's the number? "))
        numGuesses += 1
        if ( guess == secretNumber ):
            print "Yes!  You win!"
            break
        else:
            if (guess > secretNumber):
                print "%d is too high" % guess
            else:
                print "%d is too low" % guess

    if ( numGuesses == maxGuesses ):
        print "You ran out of guesses!"
    else:
        print "Nice win!  It only took you %d guesses!" % numGuesses

    return()

# main loop...
keepGoing = True

while (keepGoing == True):
    playTheGame()
    playAgain = raw_input("Would you like to play again (y/n)")
    if ( playAgain == "n" ):
        keepGoing = False

print "Thanks for playing!"
