# What is this
This is for a talk on using Python + SQLite3 + Discord + Shodan

# Context
1. [Using pip to install requirements.](https://github.com/loust/layer8-python#1-using-pip-to-install-the-requirements)
2. [SQLiteStudio](https://github.com/loust/layer8-python#2-sqlitestudio)
3. [Shodan API](https://github.com/loust/layer8-python#3-shodan-api)
4. [Discord API](https://github.com/loust/layer8-python#4-discord-api)
5. [Integration](https://github.com/loust/layer8-python#4-integration)

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

[shodan_docs]:
Now, to view the basic usage of this API, follow this [link](https://shodan.readthedocs.io/en/latest/)

Here are two snippets directly from [here](https://shodan.readthedocs.io/en/latest/tutorial.html#looking-up-a-host)

We begin by importing shodan and using our API key
```python
import shodan

SHODAN_API_KEY = "insert your API key here"

api = shodan.Shodan(SHODAN_API_KEY)
```

```python
# Wrap the request in a try/ except block to catch errors
try:
# Search Shodan
    results = api.search('apache')

# Show the results
    print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
except shodan.APIError as e:
    print('Error: {}'.format(e))
```

Also, this snippet:

```python
# Lookup the host
host = api.host('217.140.75.46')

# Print general info
print("""
        IP: {}
        Organization: {}
        Operating System: {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

# Print all banners
for item in host['data']:
        print("""
                Port: {}
                Banner: {}

        """.format(item['port'], item['data']))
```
Note, for this lab, we only need the basics. We don't need to output a lot of detail. We just need a showcase. You can later on go ahead and look around the rest of the Shodan documentation to utilize and expand your bot.

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
