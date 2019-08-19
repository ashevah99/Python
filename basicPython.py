
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


def loops():
    stuff = "hello my name is sam nice to meet you".split()
    newstuff = []
    print(stuff)
    # added in reverse
    while stuff:
        newstuff.append(stuff.pop())

    newstuff.reverse()
    print(newstuff)
    while 'sam' in newstuff:
        newstuff.remove('sam')

    print(newstuff)

loops()


def sampleInput():
    dic = {}
    while dic.__len__() < 10:
        name = input("\nwhat is your name?")
        response = input("\nhow did you find your service?")
        dic[name] = response
        print("will keep repeating until 10 recipients have been tended to")
        print("current number: " + str(dic.__len__()))
    print(dic)


sampleInput()
