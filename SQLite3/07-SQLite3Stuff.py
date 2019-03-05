import sqlite3

# Initialize the database in memory
# Follow https://docs.python.org/2/library/sqlite3.html

con = sqlite3.connect(':memory:') # This does not make a file
cur = con.cursor() # current cursor position


# We initiate the query to create the table in the memory of an unnamed
# database.
query = """
CREATE TABLE shodantable (
    id   INTEGER PRIMARY KEY ASC AUTOINCREMENT
                 NOT NULL
                 UNIQUE,
    ip   VARCHAR NOT NULL,
    port VARCHAR NOT NULL,
    data TEXT
);
"""

# Execute once, the query. Uponsuccess, the table is now created.
if cur.execute(query):
    con.commit()
    print("Success")


# We craft a script to insert this data into the database!
# Just make sure you end them with a semi column. (;)
script = """
INSERT INTO shodantable
(ip, port, data)
VALUES
('{ip}','{port}','{data}');
INSERT INTO shodantable
(ip,port,data)
VALUES
('{ip}','{port}','{data}');""".format(ip='8.8.8.8',
                                port='443',
                                data='some data'
                        )

# We apply the script. Note that we are using executescript(). This function is
# VERY reliable because you can execute more than one query!
if cur.executescript(script):
    con.commit()
    print('Success')

# Execute this once, with a given value of integer 1. Note the ? at the end of
# the query. Note that this is more secure than using {}. We are using the {}
# because we are not giving the user INPUT. Do NOT do this. If you're literally
# taking input from the user from your bot, use this method.
# But for a discord bot, you won't really need to ask a user for an input,
# unless your application does something like that.

# This demonstrates the fetchone() command. Note that you NEED to store this in
# a variable, otherwise you will lose the data. Because it's at the current
# cursor. Note the >> cur. <<
if cur.execute("SELECT * FROM shodantable WHERE id is ?", (1,)):
    items = cur.fetchone()
    print(items)

# Demonstrate fetchall()
if cur.execute("SELECT * FROM shodantable"):
    items = cur.fetchall()
    print(items)

# You can also visualize it like this, easier!
for _ in items:
    print(_)


# Make sure you close your data base after every call! This can be done in
# functions etc.
con.close()
