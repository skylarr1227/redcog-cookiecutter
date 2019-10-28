from discord.ext import commands
import discord
import random
import re
from redbot.core import Config, commands, checks


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
            server = discord.utils.get(self.bot.guilds, id=idnum)
            if server:
                await self._confirm_invite(server, owner, ctx)
            else:
                await self.bot.say("I'm not in that server")
        else:
            msg = ""
            servers = sorted(self.bot.guilds, key=lambda s: s.name)
            for i, server in enumerate(servers, 1):
                msg += "{}: {}\n".format(i, guild.name)
            msg += "\nTo post an invite for a server just type its number."
            for page in pagify(msg, delims=["\n"]):
                await self.bot.say(box(page))
                await asyncio.sleep(1.5)  # Just in case for rate limits
            msg = await self.bot.wait_for_message(author=owner, timeout=15)
            if msg is not None:
                try:
                    msg = int(msg.content.strip())
                    server = servers[msg - 1]
                except ValueError:
                    await self.bot.say("You must enter a number.")
                except IndexError:
                    await self.bot.say("Index out of range.")
                else:
                    try:
                        await self._confirm_invite(server, owner, ctx)
                    except discord.Forbidden:
                        await self.bot.say("I'm not allowed to make an invite"
                                           " for {}".format(guild.name))
            else:
                await self.bot.say("Response timed out.")
 


    @commands.command(name='joinsrv', description='send invite for discord server')
    async def create_invite(self, ctx, channel: int = None):
        """Create instant invite"""
        link = await ctx.channel.create_invite(max_age = 300)
        await ctx.send(link)
        
        
def setup(bot):
    bot.add_cog(invitegen(Bot))
