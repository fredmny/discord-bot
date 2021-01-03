import os
import discord
import random

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


bot.run(TOKEN)