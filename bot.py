import asyncio
import os
from os.path import join, dirname

import discord
from discord.ext import commands
from dotenv import load_dotenv

from movietime import tiktok_blur
from imgur import upload

from settings import *

# discord gateway intents
intents = discord.Intents.default()
allowed_mentions = discord.AllowedMentions(everyone=False,
                                           users=True,
                                           roles=False)

# bot instance
bot = discord.ext.commands.Bot(command_prefix=prefix,
                               intents=intents,
                               description=description,
                               case_insensitive=True,
                               allowed_mentions=allowed_mentions)

# load .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


@bot.command()
async def tiktok(ctx):
    await ctx.send(f'Send a file to be rendered. It must be a `.mp4`.')

    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name='for a video upload'))

    # check for file
    def check(message):
        return message.author == ctx.author and \
               len(message.attachments) == 1 and \
               '.mp4' in message.attachments[0].filename

    # placeholder
    msg = None
    try:
        msg = await bot.wait_for('message', check=check, timeout=300)
    except asyncio.TimeoutError:
        await ctx.send('Timed out. Please try again')

    # save file
    await msg.attachments[0].save('temp/input.mp4')
    await ctx.send('File saved, now rendering...')
    # render file
    await bot.change_presence(activity=discord.Game(
        name='| Rendering a video...'))
    await tiktok_blur('temp/input.mp4')
    # upload file to imgur
    await ctx.send(f'{ctx.author.menion}, here\'s your video: {await upload()}')

    await bot.change_presence(activity=discord.Game(name='nothing :)'))


bot.run(os.getenv('BOT_TOKEN'))
