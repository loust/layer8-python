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
![alt text][shodan]

Either press the show API or go to your account and copy it from there.

# 4. Discord API
[discord_developer01]: https://raw.githubusercontent.com/loust/layer8-python/master/images/discord-developer01.png
[discord_developer02]: https://raw.githubusercontent.com/loust/layer8-python/master/images/discord-developer02.png
We will need to enable the developer mode in Discord because we need this to see channel IDs and user IDs to test our bots further.

Go to your user settings and on the left aside, you will see the App settings. Click on "Appearance".
![alt text][discord_developer01]

Now, scroll down to find the Advanced section, only to toggle the developer mode on.
![alt text][discord_developer02]

# Conclusion
By the end of getting the basics from this lab, you will be able to create and maintain your own Discord bot that utilizes a database to retain information and uses an API to interface with another application.
