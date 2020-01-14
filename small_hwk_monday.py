#1 
name = input("What is your name? ")
print(name)
#1b
if (len(name) > 0):
    print("HELLO " + name.upper() + "YOUR NAME HAS " + str(len(name)))
#len(name) is an integer, had to parse it so it can be a string.

