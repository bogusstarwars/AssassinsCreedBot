import discord
from discord.ext import commands
import random
import asyncio


class GiveawayCog:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def giveaway(self, ctx, time: str):
        """Starts a giveaway. Only Staff Role can use this. Requires time input (in h/m/s). (Ex: $giveaway 10h)"""
        #Is the Author a Staff member
        if discord.utils.get(ctx.guild.roles, name='Staff') in ctx.message.author.roles:
            #Are we dealing with seconds, minutes, hours, or days 
            if 's' in time:
                t = int(time[:-1])
                timey = time[:-1] + ' seconds'
            elif 'm' in time:
                t = int(time[:-1])*60
                timey = time[:-1] + ' minutes' 
            elif 'h' in time:
                t = int(time[:-1])*3600
                timey = time[:-1] + ' hours'
            elif 'd' in time:
                t = int(time[:-1])*86400
                timey = time[:-1] + ' days'
            embed = discord.Embed(title=":tada:GIVEAWAY:tada:", colour=discord.Colour(0xaf1329), description="React to this messge to enter the giveaway! This giveaway ends in {}!".format(timey))
            nessage = await ctx.send(content=None,embed=embed)
            await nessage.add_reaction('🎉')
            while t > 0:
                if (t <= 60):
                    await asyncio.sleep(t)
                    t = (t - 60)    
                elif t > 60 and t < 3600:
                    await asyncio.sleep(60)
                    t = (t - 60)
                    timey = str(int(t/60)) + ' minute(s)'
                    embed = discord.Embed(title=":tada:GIVEAWAY:tada:", colour=discord.Colour(0xaf1329), description="React to this messge to enter the giveaway! This giveaway ends in {}!".format(timey))
                    await nessage.edit(content='🎉 React to this message to enter the giveaway! This giveaway will end in {} ! '.format(timey))
                elif t >= 3600 and t < 86400:
                    await asyncio.sleep(60)
                    t = (t - 60)
                    h = int(t/3600)
                    m = (t%3600)/60
                    #timey = str(t/3600) + ' hour(s)'
                    embed = discord.Embed(title=":tada:GIVEAWAY:tada:", colour=discord.Colour(0xaf1329), description="🎉 React to this message to enter the giveaway! This giveaway will end in {} hours and {} minutes! ".format(h,m))
                    await nessage.edit(embed=embed)
                elif t >= 86400:
                    await asyncio.sleep(60)
                    t = (t - 60)
                    d = int(t/86400)
                    h = int((t%86400)/3600)
                    m = int(((t%86400)%3600)/60)
                    #timey = str(t/86400) + ' day(s)'
                    embed = discord.Embed(title=":tada:GIVEAWAY:tada:", color=discord.Color(0xaf1329), description='🎉 React to this message to enter the giveaway! This giveaway will end in {} days, {} hours, and {} minutes! '.format(d,h,m))
                    await nessage.edit(embed=embed)
            await nessage.remove_reaction('🎉',self.bot.user)
            await nessage.edit(content='🎉 React to this message to enter the giveaway! Time is UP! Winner is below!')
            reacts = discord.utils.get(self.bot._connection._messages, id=nessage.id).reactions
            print (reacts)
            users = await reacts[0].users().flatten()
            print (users)
            winner = random.choice(users) 
            await ctx.send('{0.name} has won!'.format(winner))
        
        else:
            await ctx.send('Only Staff can start giveaways.')

def setup(bot):
    bot.add_cog(GiveawayCog(bot))
