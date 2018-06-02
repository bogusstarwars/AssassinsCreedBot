import discord
import asyncio
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ping(ctx):
    """pong"""
    await ctx.send('pong')

@bot.command()
async def invite(ctx):
    """Creates Invite link"""
    await ctx.send('https://discordapp.com/oauth2/authorize?client_id=451647260707651596&scope=bot')

@bot.command()
async def giveaway(ctx, time: str):
    """Starts a giveaway. Only Staff Role can use this. Requires time input (in h/m/s). (Ex: $giveaway 10h)"""
    #Is the Author a Staff member
    if discord.utils.get(ctx.guild.roles, name='Staff') in ctx.message.author.roles:
        #Are we dealing with seconds, minutes, or hours 
        if 's' in time:
            t = int(time[:-1])
            timey = time[:-1] + ' seconds'
        elif 'm' in time:
            t = int(time[:-1])*60
            timey = time[:-1] + ' minutes' 
        elif 'h' in time:
            t = int(time[:-1])*3600
            timey = time[:-1] + ' hours'
        nessage = await ctx.send('🎉 React to this message to enter the giveaway! This giveaway will end in {}! '.format(timey))
        await nessage.add_reaction('🎉')
        while t > 0:
            if (t <= 60):
                await asyncio.sleep(t)
                t = (t - 60)
            elif t > 60 and t < 3600:
                await asyncio.sleep(60)
                t = (t - 60)
                timey = str(int(t/60)) + ' minute(s)'
                await nessage.edit(content='🎉 React to this message to enter the giveaway! This giveaway will end in {} ! '.format(timey))
            elif t >= 3600:
                await asyncio.sleep(900)
                t = (t - 900)
                timey = str(t/3600) + ' hour(s)'
                await nessage.edit(content='🎉 React to this message to enter the giveaway! This giveaway will end in {} ! '.format(timey))
        await nessage.remove_reaction('🎉',bot.user)
        await nessage.edit(content='🎉 React to this message to enter the giveaway! Time is UP! Winner is below!')
        reacts = discord.utils.get(bot._connection._messages, id=nessage.id).reactions
        print (reacts)
        users = await reacts[0].users().flatten()
        print (users)
        winner = random.choice(users) 
        await ctx.send('{0.name} has won!'.format(winner))
    
    else:
        await ctx.send('Only Staff can start giveaways.')
    





bot.run('T O K E N')  