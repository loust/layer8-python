# This is pretty straight forward.
# if exists then else.

a = 'test1'

if a is "test":
    print("yay")
else:
    print("boohoo")

# Note, if we reverse this order:

if 'test' in a:
    print("yay")
else:
    print("boohoo")


# Note, in is different than is.
# is : exactly this string or integer
# in : item exists in this list or string

# For example, we can check if a user is Admin or Mod
roles1 = "AdminMod"
roles2 = ["Admin","Mod"]

user_role = "Mod"

if user_role in roles1:
    print("Success")

if user_role in roles2:
    print("Success")

# Note how both of these two do the same thing. roles1 is more efficient since it's a string


# Now, let's think of negative space.

user_role = "Member"

if user_role not in roles1:
    print("no access")

if user_role not in roles2:
    print("no access")

# Note how the user gets no access due to the role being a "Member" and not a part of "Admin" or "Mod"

# Now, for boolean values

access = True
if access:
    print("proceed")

if not access:
    print("don't proceed")

access = False
if access:
    print("proceed")

if not access:
    print("don't proceed")
