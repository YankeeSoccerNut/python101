# sum all the numbers in a list
numbers = [-1, 0, 1, 3, 2, 5, 7, 4, 9, 11, 13, 22, -2, -4]
sum = 0

for x in numbers:
    sum += x

print "the sum of this list %r is %d" % (numbers, sum)

# Smallest number....use min function
print "The smallest number is %d" % min(numbers)

# Largest number....use max function
print "The largest number is %d" % max(numbers)

# Even numbers....use mod 2
evenNumbers = []
for x in numbers:
    if x % 2 == 0:
        # print x
        evenNumbers.append(x)

print "Even numbers found %r" % evenNumbers

# positive numbers....simple compare
positiveNumbers = []
for x in numbers:
    if x > 0:
        # print x
        positiveNumbers.append(x)

print "Positive numbers found %r" % positiveNumbers

# lets define a function that returns the resulting list from multiplying a given list of numbers by a given factor

def multiplyListByFactor(aListOfNumbers, aFactor):
    resultList = []
    for x in aListOfNumbers:
        resultList.append(x * aFactor)

    return resultList

print "Multiplying this list %r \nby a factor of %d yields \n%r" % (numbers, 2, multiplyListByFactor(numbers, 2))

def multiplyVectors (x, y):
    resultVector = []

#multiply equal vectors only
    if len(x) != len(y):
        print "Unequal vectors...can't proceed"
        return resultVector

    #at this point the vectors are equal in length...do the math

    for i in range(0, (len(x))):
            resultVector.append(x[i] * y[i])

    return resultVector

vector1 = [2,4,5]
vector2 = [2,3,6]

print "vector1 is %r vector2 is %r their product is %r" % (vector1, vector2, multiplyVectors(vector1, vector2))

# add any 2 equal length Matrices....
def addTwoEqualMatrices(matrix1, matrix2):
    resultMatrix = []

    #add together equally sized matrices only (same rows and same columns)
    #row count is an easy test....columns could be tougher

    if (len(matrix1)) != (len(matrix2)):  #unequal so return empty resultMatrix
        print "Row counts are different...can't be added"
        return resultMatrix

    #at this point we have same number of rows...
    #we'll have to test columns for each row as we go and break out if we find inequality

    for i in range (0, len(matrix1)):
        rowForResultMatrix = []

        for j in range (0, len(matrix1[i])):
            if (len(matrix1[i]) != (len(matrix2[i]))): #unequal so return empty
                print "Column counts on row %d are different...can't be added" % i
                resultMatrix = [] #wipe out anything we may have calculated
                return resultMatrix

            # at this point we know columns are equal too...let's add and build the row for the result matrix...

            rowForResultMatrix.append(matrix1[i][j] + matrix2[i][j])

        #print "rowForResultMatrix %r" % rowForResultMatrix
        resultMatrix.append(rowForResultMatrix)
    return resultMatrix

matrix1 = [[1,1,1,16],[1,2,1,10],[1,3,1,90]]
print "matrix1 %r" % matrix1
matrix2 = [[2,1,2,14],[2,2,2,30],[2,3,2,40]]
print "matrix2 %r" % matrix2

print "the sum of these matrices is %r" % addTwoEqualMatrices(matrix1, matrix2)

def deDupe(aList):
    deDupedList = []

    for item in aList:
        #check to see if item is already in our deDupedList
        #if not, add it
        if deDupedList.count(item) == 0:
            deDupedList.append(item)

    return deDupedList

listToDedupe = [1,2,3,'a',3,3,'a','b',3,1,1,4,'b','b','c','c','d',4,4,5,6]

print listToDedupe
print deDupe(listToDedupe)
