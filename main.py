import os
import sys

import discord
from discord.ext import tasks, commands

import config
sys.path.insert(0, 'cogs/')
from cogs import *

class AImchopBot(commands.Bot):

    def __init__(self, command_prefix):

        intents = discord.Intents.default()
        intents.message_content = True # enables bot to access message content
        super().__init__(command_prefix=command_prefix, intents=intents)

    async def setup_hook(self):
        # load extensions
        errored_ext = []
        for ext in config.extensions:
            try:
                await bot.load_extension(ext)
                print(f"Loaded extension \'{ext}\'")
            except:
                print(f"Faileed to load extensions \'{ext}\' \n{type(e).__name__}: {e}")
                errored_ext.append(ext)
            
            print(f"Loaded extensions: {[x for x in bot.cogs]}")
            for ext in errored_ext: config.extensions.remove(ext)

            return


# initialize bot instance
bot = AImchopBot(command_prefix='!')

@bot.command() # load extension <ext>
async def load(ctx, ext):
    if ext in config.extensions:
        print(f"Extension \'{ext}\' is already loaded.")
        return
    
    try:
        await bot.load_extension(ext)
        print(f"Loading extension \'{ext}\'")
        config.extensions.append(ext)
    except Exception as e:
        print(f"Failed to load extension \'{ext}\'\n{type(e).__name__}: {e}")
        
    return

@bot.command() # unloads extension <ext>
async def unload(ctx, ext):
    if ext not in config.extensions:
        print(f"Extension \'{ext}\' not found, or not currently loaded.")
        return
    
    try:
        await bot.unload_extension(ext)
        print(f"Unloading extension \'{ext}\'")
        config.extensions.remove(ext)
    except Exception as e:
        print(f"Failed to unload extension \'{ext}\'\n{type(e).__name__}: {e}")

    return

@bot.command() # reloads extension <ext>
async def reload(ctx, ext):
    
    if ext not in config.extensions:
        print(f"Extension \'{ext}\' not found, or not currently loaded.")
        return
    
    try:
        await bot.reload_extension(ext)
        print(f"Extension \'{ext}\' reloaded")
    except Exception as e:
        print(f"Failed to reload extension \'{ext}\'\n{type(e).__name__}: {e}")

    return

@bot.command()
async def extensions(ctx):
    message = "Currently Loaded Extensions:\n"
    for i, extension in enumerate(config.extensions):
        message += f"{i+1}. {extension}\n"
    await ctx.channel.send(f"```{message}```")
    return

bot.run(config.token)