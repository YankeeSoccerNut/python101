# Passing variables into functions are called ARGUMENTS on the way in...PARAMETERS inside the functions
# Functions ALWAYS return a value

def sayHelloWithName(name):
    print "Hello, %s" % name
    return (name, "Yes", "Crazy")

# sayHelloWithName("Scott")
# sayHelloWithName("Allyson")
# sayHelloWithName("Michael")

students = ["Scott", "Allyson", "Michael"]

for i in range (0, len(students)):
    x,y,z = sayHelloWithName(students[i])
    print x
    print y
    print z
