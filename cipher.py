def caesarCipher(aMessage):
    key = ['a','b', 'c', 'd','e', 'f','g','h', 'i','j','k', 'l','m','n','o','p','q', 'r','s','t','u','v','w', 'x','y','z']

    returnMsg = []

    for i in range (0,(len(aMessage))):
        # Don't forget about non-alphabetic chars!!!
        # just copy these to the returnMsg and move on

        if aMessage[i].isalpha() == False:
            returnMsg.append(aMessage[i])
            continue

        # At this point we have an alphabetic char that needs to be (de)ciphered

        # find the index value of the letter in the message
        #print "i is %d searching for %s" % (i, aMessage[i].lower())
        msgIndex = key.index(aMessage[i].lower())
        #print "found match at index %d" % msgIndex

        #translate the index to it's ROT13 counterpart to find the encrypt/ decrypt index value
        if msgIndex <= 12:
            cipherIndex = msgIndex + 13
        else:
            cipherIndex = msgIndex - 13

        #build the return message with the letter at the translated index value
        #print "cipherIndex %d" % cipherIndex
        returnMsg.append(key[cipherIndex])
        #print "returnMsg %r" % returnMsg

    return ''.join(returnMsg)

testParagraph = "lbh zhfg hayrnea jung lbh unir yrnearq"

newParagraph = caesarCipher(testParagraph)

print "\nTest Paragraph:"
print testParagraph
print "\nNew Paragraph:"
print newParagraph

#now let's reverse the process
print "\nBack to the original:"
print caesarCipher(newParagraph)
