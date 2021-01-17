import os
import discord
import random
import json

# Load own modules
import sc2_version

# To instantiate a Bot, the commands extension is needed
from discord.ext import commands

from dotenv import load_dotenv

# Intents are necessary for handling member actions, like sending DMs
intents = discord.Intents.default()
intents.members = True

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
WA_GROUP = os.getenv('WHATSAPP_GROUP')

# Instantiate bot with command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user.name} connected to following server:\n'
        f'Name: {guild.name} --- ID: {guild.id}'
    )

# Send DM to new members
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Olá, {member.name},\n'
        f'Bem Vindo ao servidor {GUILD}. Este é o nosso ponto de'
        'encontro virtual quando jogamos. Fique à vontade para'
        f'também se juntar ao nosso grupo de WhatsApp:\n{WA_GROUP} .'
        '\n\nDivirta-se!!!'
    )

# Check if the Starcraft 2 Version was updated
@bot.command(name='sc2_version', help='Checks if there is an updated version of Starcraft II')
async def check_version(ctx):
    data = sc2_version.get_version()
    if data['new_version_info']['version'] != data['old_version_info']['version']:
        await ctx.send(
            'A versão do Starcraft foi atualizada da versão '
            f'{data["old_version_info"]["version"]}, checada no dia '
            f'{data["old_version_info"]["date"]}, para a versão '
            f'{data["new_version_info"]["version"]}.'
        )
    else:
        await ctx.send(
            f'Não houve alteração de versão desde a última checagen no dia '
            f'{data["new_version_info"]["date"]}. A versão atual é a '
            f'{data["new_version_info"]["version"]}'
        )

"""
ToDo 
- Inform about updates
    - Detect version with webscraping
- Inform about latest game using StarCraft's API
"""

""" Check Version automatically """

bot.run(TOKEN)