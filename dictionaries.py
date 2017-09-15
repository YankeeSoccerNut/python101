zombie = {}
zombie["weapon"] = "axe"
zombie["health"] = 100
zombie["speed"] = 10
zombie["name"] = "Scott"

print zombie
for key,value in zombie.items():
    print "Zombie has a key of %s with a value of %s" % (key, value)
    print "Zombie has a key of %s with a value of %s" % (key, zombie[key])

#put lists and dictionaries together
zombies = []

zombies.append(zombie)
zombies.append({"weapon":"fist", "health":150, "speed":15, "name":"Rob"})

print zombies
