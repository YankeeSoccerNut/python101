print "Loops file"

# for loops test at beginning...second number is terminal value
# did we hit terminal value, Yes, then commands don't execute

for i in range (1,11):
    print "%r" %i

# Especially powerful when combined with Lists
# A list is a single variable with a bunch of numbered (indexed) parts
# An index is always an integer and starts at 0

students = ["Mikalya", "Jennifer", "Nikolas", "Zach"]
print students  # all students
print students[-1]  # last element
print students[-2] # penultimate

atlantaTeams = ["Falcons", "Braves", "Hawks", "Thrashers"]
print atlantaTeams

# Remove the last element with .pop(), can also remove ith element with .pop(i)
# atlantaTeams.pop()
# print atlantaTeams

# Add element to the end with .append
atlantaTeams.append("ATL United")
print atlantaTeams

# to get part of the list, use [x:y].  Starts at x and goes through y-1
# all but the 1st would be [1:] skips 0 gotes to end
