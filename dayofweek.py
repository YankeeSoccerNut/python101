daysOfTheWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

userDay = int(raw_input("What day of the week do you want (0-6)?"))

print "You picked %s." % daysOfTheWeek[userDay]

if userDay == 0 or userDay == 6:
    print "It's the weekend...you should sleep!"
else:
    print "It's a weekday...you should go to work"
