# Disclaimer, I will not go over dictionaries due to time. A list should be good enough for this.

# To make a simple list to test things out:

# A list of integers.
a = [1,2,3,4,5,6,7,8,9,0]

# A list of strings
b = ['one','two','three','four','five','six','seven','eight','nine','zero']


# Now, we can do some nice things. The most commonly used loop are the following:
for item in a:
    print(item)

for item in b:
    print(item)

# Now, if you wish to do something faster instead of typing "item"
for _ in a:
    print(_)

# Regardless, we can also loop through numbers
for _ in range(0,10):
    print(_)

# Now, if you want a more traditional indexed loop, we can do the following, but not necessary.
for index,item in enumerate(b):
    print("{} @ {}".format(item,index))


# To put things next to eachother, we can do this
for _ in b:
    print(_),
# NOTE THE COMMAN. THIS IS ONLY FOR PYTHON 2!


# Another (older) way of putting strings together is this:
print("This is "+str(a[0])+" a test")
print("This is ",str(a[0])," a test")

# Note how the fact that you have to cast str() to an integer in order for this to work.
# Using the .format() would automatically convert the paramter to a string.

# Also, see how the commas inser an extra space. This is useful when making CSVs.

# Now, like earlier, we can make it so the last item in the loop gets a special modifier.
last = ''
for _ in b:
    if _ is b[-1]:
        last = '.'
    else:
        last = ','
    print("{0}{1}".format(_,last)),
# NOTE THIS WILL BREAK. IT IS ONLY FOR PYTHON 2 TO ADD THE COMMA


# To do this in Python3, we do the following:
last = ''
for _ in b:
    if _ is b[-1]:
        last = '.\n'
    else:
        last = ', '
    print("{0}{1}".format(_,last),sep='',end='',flush=True)

# end='' changes end='\n' to nothing so you can have something right after. Alternatively, you could
# remove the space from last = ', ' and change end = '' to end = ' '
# I don't know what flush is for. Google it.
