# What is this
This is for a talk on using Python + SQLite3 + Discord + Shodan

# Context
1. Using pip to install requirements.
2. Hello World
3. Lists and Loops
4. Python tricks to be used
5. Shodan API
6. Default example from Shodan
7. SQLite3 example
8. Advanced database manipulation
9. Discord API
10. Integration

# 1. Using pip to install the requirements.
```bash
pip3 install -r ./requirements.txt
```

Note, use `pip3` because we need to be in python3. Use `pip` if your default python is version 3.
Also, use `sudo`... Run as root if you are under linux.

In addition, note that you can put this whole thing in a different env if you have another version of discord.py, since discord.py rewrite is WAY different than discord.py.

# Conclusion
By the end of getting the basics from this lab, you will be able to create and maintain your own Discord bot that utilizes a database to retain information and uses an API to interface with another application.
