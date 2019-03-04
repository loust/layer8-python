# This is a single comment.

"""
This is a long comment
"""

print("Hello World\n")

# Another way to say hello is the following:

hello = "World"

print("Hello {}".format(hello))

# Another nice way to repeat similar things

print("Hello {0} {0} {0}".format(hello))

# Now, you can see that, with a loop, you can make it so it will output something different when
# it reaches the last item in the loop. An example will be shown in the Lists and Loops section.

world = "Hello"

print("{0} {1}".format(world,hello))

# This is the same as the following

print("{} {}".format(world,hello))

# But does not follow the numbering.

# {0} is the first paramter and {1} is the second.
