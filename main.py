#imports#######################################################################################################################imports#

import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.ext.commands import BucketType
from discord.utils import get
import random
from itertools import cycle
import os
import re
import time
import math
import asyncio
import datetime
from datetime import datetime, timedelta
import nacl
import matplotlib.pyplot as plt
import json
from typing import List
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
from io import BytesIO
import topgg

database_file = 'database.txt'

#starting#####################################################################################################################starting#

activities = [
    discord.Game(name="/help"),
    discord.Game(name="//help")
]
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
client.remove_command('help')

rcolor = [
    discord.Colour.purple(),
    discord.Colour.orange(),
    discord.Colour.green(),
    discord.Colour.blue(),
    discord.Colour.red(),
    discord.Colour.teal(),
    discord.Colour.dark_teal(),
    discord.Colour.dark_green(),
    discord.Colour.dark_blue(),
    discord.Colour.dark_purple(),
    discord.Colour.magenta(),
    discord.Colour.dark_magenta(),
    discord.Colour.gold(),
    discord.Colour.dark_gold(),
    discord.Colour.dark_orange(),
    discord.Colour.dark_red(),
    discord.Colour.lighter_gray(),
    discord.Colour.dark_gray(),
    discord.Colour.light_gray(),
    discord.Colour.darker_gray(),
    discord.Colour.blurple(),
    discord.Colour.greyple()
]

@client.event
async def on_ready():
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            await client.load_extension(f"cogs.{file[:-3]}")
            print(f"cogs.{file[:-3]}")
    print("CYKLERBOT is ready, you can now leave the tab")
    embed = discord.Embed(colour=discord.Colour.blue())
    channel = client.get_channel("starting channel id here")
    try:
        synced = await client.tree.sync()
        embed.add_field(name=f'back online',
                    value=f'cyklerbot has been updated, {len(synced)} commands synced',
                     inline=False)
        await channel.send(embed=embed)
    except:
        embed.add_field(name=f'back online',
                    value='cyklerbot has been updated.',
                    inline=False)
        await channel.send(embed=embed)
    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print(e)
    while True:
        for activity in activities:
            await client.change_presence(activity=activity)
            await asyncio.sleep(5)
    
                
from utils import data, save_data, load_data, insert_data, get_data, rcolor, delete_data, list_all_keys, list_keys_with_prefix
save_data(data)


#commands####################################################################################################################commands#


#end###################################################################################################################################end#
data = load_data()


client.run("TOKEN HERE")
