import discord
import asyncio
import random
from discord.ext import commands
import sys, traceback

initial_extensions = ['cogs.giveaway',
                      'cogs.owner']

bot = commands.Bot(command_prefix='$')

bot.loop.set_debug(True)
# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    heart = discord.utils.get(guild.roles, name = 'HEART')
    brole = discord.utils.get(guild.roles, name = 'BLUE')
    yrole = discord.utils.get(guild.roles, name = 'YELLOW')
    grole = discord.utils.get(guild.roles, name = 'GREEN')
    mem = guild.get_member(payload.user_id) 
    if payload.user_id == bot.user.id:
        return
    if payload.message_id == bot.rmsg.id:
        if payload.emoji.name == '\U00002764':
            await mem.add_roles(heart)
        elif payload.emoji.name == '\U0001f49b':
            await mem.add_roles(yrole)
        elif payload.emoji.name == '\U0001f499':
            await mem.add_roles(brole)
        elif payload.emoji.name == '\U0001f49a':
            await mem.add_roles(grole)
        

@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    heart = discord.utils.get(guild.roles, name = 'HEART')
    brole = discord.utils.get(guild.roles, name = 'BLUE')
    yrole = discord.utils.get(guild.roles, name = 'YELLOW')
    grole = discord.utils.get(guild.roles, name = 'GREEN')
    mem = guild.get_member(payload.user_id)
    if payload.user_id == bot.user.id:
        return
    if payload.message_id == bot.rmsg.id:
        if payload.emoji.name == '\U00002764':
            await mem.remove_roles(heart)
        elif payload.emoji.name == '\U0001f49b':
            await mem.remove_roles(yrole)
        elif payload.emoji.name == '\U0001f499':
            await mem.remove_roles(brole)
        elif payload.emoji.name == '\U0001f49a':
            await mem.remove_roles(grole)


@bot.command()
async def ping(ctx):
    """pong"""
    embed = discord.Embed(title = 'ping',colour=discord.Colour(0xaf1329),description="pong")
    await ctx.send(content=None,embed=embed)

@bot.command()
async def invite(ctx):
    """Creates Invite link"""
    await ctx.send('https://discordapp.com/oauth2/authorize?client_id=451647260707651596&scope=bot')


@bot.command()    
async def rolepress(ctx):
    bot.rmsg = await ctx.send('Click on an emoji to get that role!')
    for emoji in ['💙','❤','💚','💛']:
        await bot.rmsg.add_reaction(emoji)


bot.run('TOKEN')  