# What is this
This is for a talk on using Python + SQLite3 + Discord + Shodan

# Context
1. Using pip to install requirements.
2. SQLiteStudio
3. Shodan API
4. Discord API
5. Integration

# 1. Using pip to install the requirements.
```bash
pip3 install -r ./requirements.txt
```

Note, use `pip3` because we need to be in python3. Use `pip` if your default python is version 3.
Also, use `sudo`... Run as root if you are under linux.

In addition, note that you can put this whole thing in a different env if you have another version of discord.py, since discord.py rewrite is WAY different than discord.py.

# 2. SQLiteStudio
Please download this to visualize and make databases easily, please download SQLiteStudio from [here](https://sqlitestudio.pl/index.rvt?act=download)

# 3. Shodan API
For this, please register a free account with your student email or whatever. If you have problems registering, just login via google. That works just fine. Then go to your profile and you will see the API area

[shodan]: https://raw.githubusercontent.com/loust/layer8-python/master/images/shodanapi.png
[shodan]


# Conclusion
By the end of getting the basics from this lab, you will be able to create and maintain your own Discord bot that utilizes a database to retain information and uses an API to interface with another application.
