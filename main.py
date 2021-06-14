#Class for variables
class boob_bot_cmd_executer():
    dev = "EinWortspiel 3#9998" 
    github = "https://github.com/EinWortspiel"
    inspiration = "Too horny Kappa"

#All used Modules
import discord
import asyncio
import json
import colorama
import os

#Extra things from the Modules
from discord.ext import commands
from colorama import Style, Fore, init
init()

boob_bot_bot = commands.Bot(command_prefix = json.load(open("config.json", "r"))["Prefix"], self_bot = True, case_sensitive = True, intents = discord.Intents.all())
#Standard help command removed
boob_bot_bot.remove_command("help")

#Style and Color variable
style_and_color = f"{Fore.BLUE}{Style.BRIGHT}"

#on connect event
@boob_bot_bot.event
async def on_connect():
    print("Connected...")

#on ready event
@boob_bot_bot.event
async def on_ready():
    os.system("mode 135, 25")
    print(f"""{style_and_color}
                            ██████╗  ██████╗  ██████╗ ██████╗ ██████╗  ██████╗ ████████╗    ██████╗  ██████╗ ████████╗
                            ██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝
                            ██████╔╝██║   ██║██║   ██║██████╔╝██████╔╝██║   ██║   ██║       ██████╔╝██║   ██║   ██║   
                            ██╔══██╗██║   ██║██║   ██║██╔══██╗██╔══██╗██║   ██║   ██║       ██╔══██╗██║   ██║   ██║   
                            ██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝╚██████╔╝   ██║       ██████╔╝╚██████╔╝   ██║   
                            ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝       ╚═════╝  ╚═════╝    ╚═╝\n""")
    print(f"                            {style_and_color}Boobbot Bot made by = {boob_bot_cmd_executer.dev}")
    print(f"                            {style_and_color}Github Link = {boob_bot_cmd_executer.github}")   
    print(f"                            {style_and_color}Inspiration = {boob_bot_cmd_executer.inspiration}")                                                                                                                           

#start cmd
@boob_bot_bot.command()
async def start(ctx,*, command : str, channel : discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    while True:
        try:
            await channel.send(command)
            await asyncio.sleep(2)
        except Exception as e:
            print(f"{style_and_color}Error while trying to use the {command} command = {e}")

#start
boob_bot_bot.run(json.load(open("config.json", "r"))["Token"], bot=False)