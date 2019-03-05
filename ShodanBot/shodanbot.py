import discord
import shodan
import sqlite3
#import getpass
#import sys
#import datetime
from discord.ext import commands
from pathlib import Path

###################################################################################################

# TOKEN

TOKEN = ''
SHODAN_API_KEY = ""

# You can also use the import getpass and use it like this:
#TOKEN = getpass.getpass("Enter your bot token here: ")


###################################################################################################

# INITS AND GLOBAL VARS

description = '''Shodan bot''' # Description of your bot
prefix = '!' # The prefix to identify command calls
shodanbot = commands.Bot(command_prefix=prefix, description=description) # Initiate bot
shodanbot.remove_command('help') # remove the default help command to make your own
client = discord.Client() # Initiate the client aside from the commands
my_server = ['552069550519222273'] # server ID
dbname = 'shodandb.db'
#if not Path(dbname).is_file():
#    print("[x] DB file not found. Creating...")
#    # Create tables with the database filename here.
#    # I don't have the code at the moment.
#    quit()
#else:
#    print("[+] DB SET")

###################################################################################################

# FUNCTIONS

# Get the data by service search
#   @param
#       serv        Service name        str
#   @return
#       List of ip and data
def byservice(serv):
    api = shodan.Shodan(SHODAN_API_KEY)
    # Wrap the request in a try/ except block to catch errors
    try:
        # Search Shodan
        results = api.search(serv)

        # Show the results
        #print('Results found: {}'.format(results['total']))
        ip = ''
        data = ''
        for result in results['matches']:
            # Store to return
            ip = result['ip_str']
            data = result['data']

        return [ip,data]
    except shodan.APIError as e:
        print('Error: {}'.format(e))


# Get the data by IP address
#   @param
#       hostip      Ip address      str
#   @return
#       List of ip, port and data
def byhost(hostip):
    api = shodan.Shodan(SHODAN_API_KEY)
    # Lookup the host
    host = api.host(hostip)

    # Store the IP
    ip = host['ip_str']

    port = ''
    data = ''

    # Print all banners
    for item in host['data']:
        port = item['port']
        data = item['data']

    return [ip,port,data]

###################################################################################################

# BOT INITS

@shodanbot.event
async def on_ready():
    print(shodanbot.guilds)
    for guild in shodanbot.guilds:
        print(guild)
        print(guild.id)
        if str(guild.id) not in my_server:
            print("left server "+str(guild.id))
            await Guild.leave()
        else:
            print("Logged in as")
            print(shodanbot.user.name)
            print(shodanbot.user.id)
            game = discord.Game("Scanning the world!")
            await shodanbot.change_presence(status=discord.Status.online,
                    activity=game)

    return

@shodanbot.event
async def on_server_join(server):
    if server.id not in my_server:
        print("{}".format(server.id))
        prin('left server {}'.format(server.id))
        await Guild.leave()
    return

###################################################################################################

# BOT FUNCTIONS

# HELP FUNCTION
#   @param
#       ctx         Context
@commands.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
            color = discord.Color.green()
    )

    embed.set_author(name="Welcome to Shodanbot")
    embed.add_field(name=prefix+'help', value="Shows this page", inline=False)
    embed.add_field(name=prefix+'sscan', value=prefix+"sscan ip/service <address/name>", inline=False)

    # DMs the author
    await author.send(embed=embed)
    # If you want to show it in the channel, pass the channel ID
    # get the channel ID by doing ctx.message.channel? Check the docs!

# Shodan Scan
#   @param
#       ctx         Context
#       *passes     Passes
@commands.command()
async def sscan(ctx, *passes):
    author = ctx.message.author
    channel = ctx.message.channel
    server = ctx.message.guild # server ID

    if len(passes) < 2:
        await ctx.send("{}sscan ipaddress/service target".format(prefix))
        return

    if passes[0] in 'service':
        await ctx.send('service: {}'.format(passes[1]))
        info = byservice(passes[1])
        await ctx.send(info)
        return

    if passes[0] in 'ipaddress':
        await ctx.send('IP: {}'.format(passes[1]))
        info = byhost(passes[1])
        await ctx.send(info)
        return
    return

###################################################################################################

# ALL THE COMMANDS

shodanbot.add_command(help)
shodanbot.add_command(sscan)

###################################################################################################

# TODO

# 1. Take notes here

###################################################################################################

# RUN THE BOT

shodanbot.run(TOKEN)

###################################################################################################
