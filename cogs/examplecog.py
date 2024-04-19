import discord
from discord import app_commands
from discord.ext import commands
import random
import json
import os
from collections import Counter


from utils import data, save_data, insert_data, get_data, rcolor, delete_data, list_all_keys, list_keys_with_prefix, developer_check
save_data(data)

class MarketCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name='ping', description = 'gives the bots latency (ping)')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! {round(self.client.latency * 1000)}ms')
        

async def setup(client):
    await client.add_cog(MarketCog(client))