def longVowel(aWord):

    longVowel = list(aWord)
    returnWord = longVowel

    for i in range (0,(len(aWord))):
        if (longVowel[i] == 'A' or longVowel[i] == 'a'):
            if (longVowel[i].upper() == longVowel[i+1].upper()):
                # Magic happens here....insert 3 vowels
                returnWord.insert(i+1, 'aaa')

        elif (longVowel[i] == 'E' or longVowel[i] == 'e'):
            if (longVowel[i].upper() == longVowel[i+1].upper()):
                # Magic happens here....insert 3 vowels
                returnWord.insert(i+1, 'eee')

        elif (longVowel[i] == 'I' or longVowel[i] == 'i'):
            if (longVowel[i].upper() == longVowel[i+1].upper()):
                # Magic happens here....insert 3 vowels
                returnWord.insert(i+1, 'iii')

        elif (longVowel[i] == 'O' or longVowel[i] == 'o'):
            if (longVowel[i].upper() == longVowel[i+1].upper()):
                # Magic happens here....insert 3 vowels
                returnWord.insert(i+1, 'ooo')

        elif (longVowel[i] == 'U' or longVowel[i] == 'u'):
            if (longVowel[i].upper() == longVowel[i+1].upper()):
                # Magic happens here....insert 3 vowels
                returnWord.insert(i+1, 'uuu')



    return ''.join(returnWord)


testParagraph = "bookkeeper"

newParagraph = longVowel(testParagraph)

print "\nTest Paragraph:\n"
print testParagraph
print "\nNew Paragraph:\n"
print newParagraph
