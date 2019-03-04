# There are several ways to add items into a list.

a = [1,2,3,4,5,6,7,8,9,0]
tmp = []

for _ in a:
    tmp.append(_)

print(tmp)


# To make this more advanced:

a = [1,1,1,3,4,5,6,7,8,9,2,2,4,5,6,87,0]
tmp = []

for _ in a:
    if _ not in tmp:
        tmp.append(_)

print(tmp)


# Another faster way to dedupe is to change the list to a set()
# Note, this will take off the order.

print(set(a))

# There are myriad of other techniques to do things. Most of them can be found
# by simply searching them online. Search what you wish to do and you will find
# your answer easily.
