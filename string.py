myString = "My string"

print myString.upper()

print myString

print "this string".upper()

# Reverse

print "string"[::-1]

# Leetspeak

def leetSpeak(aParagraph):

# Strings are immuatable (not changeable in Python!) so make a copy, convert it to a list and work with that
# also, we have to convert the return to a string otherwise it's a list!

    workingCopy = list(aParagraph)

    for i in range (0,(len(aParagraph))):
        if (workingCopy[i] == 'A' or workingCopy[i] == 'a'):
            workingCopy[i] = '4'
        elif (workingCopy[i] == 'E' or workingCopy[i] == 'e'):
            workingCopy[i] = '3'
        elif (workingCopy[i] == 'G' or workingCopy[i] == 'g'):
            workingCopy[i] = '6'
        elif (workingCopy[i] == 'I' or workingCopy[i] == 'i'):
            workingCopy[i] = '1'
        elif (workingCopy[i] == 'O' or workingCopy[i] == 'o'):
            workingCopy[i] = '0'
        elif (workingCopy[i] == 'S' or workingCopy[i] == 's'):
            workingCopy[i] = '5'
        elif (workingCopy[i] == 'T' or workingCopy[i] == 't'):
            workingCopy[i] = '7'

    return ''.join(workingCopy)

testParagraph = "Laboris irure qui laborum elit commodo quis culpa aliquip anim Lorem nostrud voluptate. Commodo dolore qui irure Lorem irure proident ad aliqua sunt est veniam est excepteur. Sunt sunt deserunt ex tempor enim pariatur commodo nostrud mollit voluptate nostrud. Aute commodo do commodo adipisicing aliquip anim sit Lorem. Adipisicing enim aliquip nisi voluptate ipsum dolore sunt reprehenderit aliquip laborum."

newParagraph = leetSpeak(testParagraph)

print "\nTest Paragraph:\n"
print testParagraph
print "\nNew, Leetified Paragraph:\n"
print newParagraph

def leetSpeak(aParagraph):

# Strings are immuatable (not changeable in Python!) so make a copy, convert it to a list and work with that
# also, we have to convert the return to a string otherwise it's a list!

    workingCopy = list(aParagraph)

    for i in range (0,(len(aParagraph))):
        if (workingCopy[i] == 'A' or workingCopy[i] == 'a'):
            workingCopy[i] = '4'
        elif (workingCopy[i] == 'E' or workingCopy[i] == 'e'):
            workingCopy[i] = '3'
        elif (workingCopy[i] == 'G' or workingCopy[i] == 'g'):
            workingCopy[i] = '6'
        elif (workingCopy[i] == 'I' or workingCopy[i] == 'i'):
            workingCopy[i] = '1'
        elif (workingCopy[i] == 'O' or workingCopy[i] == 'o'):
            workingCopy[i] = '0'
        elif (workingCopy[i] == 'S' or workingCopy[i] == 's'):
            workingCopy[i] = '5'
        elif (workingCopy[i] == 'T' or workingCopy[i] == 't'):
            workingCopy[i] = '7'

    return ''.join(workingCopy)
