
# beginning stuff
message = "                     \n" + " djkldsj"
message.isspace()
foo = " hello "
print(foo + "\n" + foo.rstrip() + foo.strip())
print(message + " hello\nfucking kill me")
print("hello\n\n\n\n")

# lists
stuff = ['hello', 'what', 'is', 'up', 3]

del(stuff[-1])  # or stuff.pop()
stuff.append(float(2))
stuff.insert(0, "22222")
stuff.insert(stuff.__len__(), "e")

# prints last elem
# list can be multiple types
print((stuff))
