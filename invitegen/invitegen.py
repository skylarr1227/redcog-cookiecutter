from discord.ext import commands
import discord
import random
import re
import asyncio
from redbot.core import Config, commands, checks
from redbot.core import bank
from redbot.core import checks
from redbot.core import commands
from redbot.core.data_manager import bundled_data_path
from redbot.core.utils.chat_formatting import pagify, box
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS
from redbot.core.utils.predicates import MessagePredicate


bot = commands.Bot
BaseCog = getattr(commands, "Cog", object)
listener = getattr(commands.Cog, "listener", None) 
if listener is None:
  
    def listener(name=None):
        return lambda x: x
    
class invitegen(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def partycrash(self, ctx, idnum=None):
        """Lists servers and generates invites for them"""
        owner = ctx.message.author
        if idnum:
            guild = discord.utils.get(self.bot.guilds, id=idnum)
            if guild:
                await ctx.bot.accept_invite(guild, owner, ctx)
            else:
                await ctx.send("I'm not in that server")
        else:
            msg = ""
            guilds = sorted(self.bot.guilds, key=lambda s: s.name)
            for i, guild in enumerate(guilds, 1):
                msg += "{}: {}\n".format(i, guild.name)
            msg += "\nTo post an invite for a server just type its number."
            for page in pagify(msg, delims=["\n"]):
                await ctx.send(box(page))
                await asyncio.sleep(1.5)  # Just in case for rate limits
            msg = await ctx.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            if msg is not None:
                try:
                    msg = int(msg.content.strip())
                    guild = guilds[msg - 1]
                except ValueError:
                    await ctx.send("You must enter a number.")
                except IndexError:
                    await ctx.send("Index out of range.")
                else:
                    try:
                        await ctx.bot.accept_invite(guild, owner, ctx)
                    except discord.Forbidden:
                        await ctx.send("I'm not allowed to make an invite"
                                           " for {}".format(guild.name))
            else:
                await ctx.send("Response timed out.")
 


    @commands.command(name='joinsrv', description='send invite for discord server')
    async def create_invite(self, ctx, channel: int = None):
        """Create instant invite"""
        link = await ctx.channel.create_invite(max_age = 300)
        await ctx.send(link)
        
        
def setup(bot):
    bot.add_cog(invitegen(Bot))
