import discord
from discord import app_commands
from discord.ext import commands
import random
import json
import os
from collections import Counter


from utils import data, save_data, insert_data, get_data, rcolor, delete_data, list_all_keys, list_keys_with_prefix, developer_check
save_data(data)

class ExampleCog(commands.Cog):
    def __init__(self, client):
        self.client = client


    @app_commands.command(name='ping', description = 'gives the bots latency (ping)')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Pong! {round(self.client.latency * 1000)}ms')
        
    @app_commands.command(name='example_command', description = 'This is an example description')
    @app_commands.choices(choices=[
        app_commands.Choice(name='tiem2', value='item1'),
        app_commands.Choice(name='item1', value='item2'),
    ])  
    @app_commands.describe(arg1 = 'description for first argument')
    @app_commands.describe(arg2 = 'description for second argument')
    @app_commands.describe(choices = 'description for third argument')
    async def examplecommand(self, interaction: discord.Interaction, arg1: str, arg2: str | None, choices: app_commands.Choice[str]):
        #to acess choices you need to do choices.value()
        #you can put ephemeral=True to make the message only visible to the user
        
        embed = discord.Embed(color = random.choice(rcolor), title='Title', description='Desc')
        embed.add_field(name=f'Title', value=f'Value', inline=False)
        await interaction.channel.send(embed=embed)
        
        await interaction.response.send_message(f'Pong! {round(self.client.latency * 1000)}ms')
        

async def setup(client):
    await client.add_cog(ExampleCog(client))