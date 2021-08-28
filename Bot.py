# discord.py-new-bot
Is a bot for everyone. it's for free.

import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import time
import re
import random
from discord import Game
from asyncio import sleep
import asyncio
from configur import settings

client = discord.Client()

bot = discord.Client()

bot = commands.Bot(command_prefix = settings['prefix'])

# embeds

@bot.command()
async def embed(ctx):
    e = discord.Embed(
    title= input("Title: "),
    description= input("Description: "),
    color=0xFF0000
    )
    await ctx.send(embed=e)

# commands

@bot.command()
async def ping(ctx):
    author = ctx.message.author
    await ctx.send("Hello \nEveryone")

# Status

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='TikTok'))

print('Bot Games is online')
print(client.user.name)
print('-----------')
name = input("Your nickname: ")
print(f" Приветик папочка~ мурр)")
print('-----------')
print ("""\

  ____        _   
 |  _ \      | |  
 | |_) | ___ | |_ 
 |  _ < / _ \| __|
 | |_) | (_) | |_ 
 |____/ \___/ \__|

""")

# Token

bot.run(settings['token'])
