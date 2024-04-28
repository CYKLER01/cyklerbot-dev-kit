import discord
from discord import app_commands
from discord.ext import commands
import random
import json
import os
from collections import Counter


from utils import data, save_data, insert_data, get_data, rcolor, delete_data, list_all_keys, list_keys_with_prefix, developer_check, loadinv
save_data(data)

class PremadeCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    #money    
        
    @app_commands.command(name='money', description = 'Returns money of a given user')
    async def money(self, interaction: discord.Interaction, user: str | None):
        await interaction.defer()
        if '<@' not in user:
            return await interaction.followup.send(f'please use correct user formatting by tagging user')
        guild_id = interaction.guild_id
        if user is None:
            user = f'<@{interaction.user.id}>'
        try:
            money = data[f'm{guild_id}{user}']
        except:
            data[f'm{guild_id}{user}'] = 0
            money = data[f'm{guild_id}{user}']
        await interaction.followup.send(money)

    @app_commands.command(name='setmoney', description = 'Sets a users money.')
    async def setmoney(self, interaction: discord.Interaction, user: str | None, amt: int):
        await interaction.defer()
        if '<@' not in user:
            return await interaction.followup.send(f'please use correct user formatting by tagging user')
        guild_id = interaction.guild_id
        if user is None:
            user = f'<@{interaction.user.id}>'
        try:
            money = data[f'm{guild_id}{user}']
        except:
            data[f'm{guild_id}{user}'] = 0
            money = data[f'm{guild_id}{user}']
        data[f'm{guild_id}{user}'] = amt
        await interaction.followup.send(amt)

async def setup(client):
    await client.add_cog(PremadeCog(client))