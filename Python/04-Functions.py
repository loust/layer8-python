# Functions' purpose is to reuse

def testing():
    print("Do stuff here")

testing()

def paramslol(a,b,c):
    print("Printing: {} {} {}".format(a,b,c))

paramslol(1,2,3)

def longer(a,*b):
    print("Printing: {0} {1}".format(a,b))

longer(1,2,3,45)


# Oh look, it returns this as Printing: 1 (2, 3, 45)!
# We can do some stuff with the longer(int,*int) function

def longer2(a,*b):
    for _ in b:
        print("{0} belongs to {1}".format(a,_))

longer2(1,2,3,4,5,6)
