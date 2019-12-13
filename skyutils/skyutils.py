import asyncio
import random
import re
import string
import urllib.parse
import discord
import requests
#import config
import datetime
import json
import os
import urllib
import pytz
import io
import aiohttp
import async_timeout

from typing import Union
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
from redbot.core.config import Config
from redbot.core import commands, checks
#from discord.ext import commands
from .tools import remove_html, resolve_emoji

bot = commands.Bot
BaseCog = getattr(commands, "Cog", object)
Embed = discord.Embed


class Skyutils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   

    @commands.command()
    async def fuckchoices(self, ctx):
        multiple_choice = BotMultipleChoice(ctx, ['one', 'two', 'three', 'four', 'five', 'six'], "How many babys would you eat")
        await multiple_choice.run()

        await multiple_choice.quit(multiple_choice.choice)



    @commands.command()
    async def testconfirm(self, ctx):
        confirmation = BotConfirmation(ctx, 0x012345)
        await confirmation.confirm("So... yes, you want to pledge your eternal soul to Sky to help raise her undead army??")

        if confirmation.confirmed:
            await confirmation.update("Confirmed", color=0x55ff55)
        else:
            await confirmation.update("Not confirmed", hide_author=True, color=0xff5555)


    @commands.command()        
    async def helpadv(self, ctx):
        """Quick reference for Adventure...bitches """
        embeds = [
            Embed(title="Quick Reference for Skybot", description="__**+adventure**__\nStart an adventure in your current channel\n__**+stats**__\nTo view your character sheet as well as\nyour currently equipped items.\n", color=0x115599),
            Embed(title="Quick Reference cont. Loot", description="__**+loot**__\nUse to open your lootboxes\nJust specify the type\nExample:\n```+loot normal```\nor\n```+loot epic 10```\nfor multiple at once\n\n__**+combine**__\nCombiine your loot boxes by specifying type you wish to convert", color=0x5599ff),
            Embed(title="Quick Reference cont. Hero-classes", description="```+heroclass\n   -Bard\n   -Wizard\n   -Ramger\n   -Beserker\n   -Cleric```", color=0x191638)
        ]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()
    
    
    
            
            

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        """Dem math probs with the + in em"""
        await ctx.send(left + right)

    @commands.command()
    async def subtract(self, ctx, left: int, right: int):
        """For all those times you can't be bothered with
        how many apples Jake has after little Timmy used 6
        to throw at the kids doing their math homework"""
        await ctx.send(left - right)

    @commands.command()
    async def multiply(self, ctx, left: int, right: int):
        """fuck a calculator, skybot is here baby"""
        await ctx.send(left * right)

    @commands.command()
    async def divide(self, ctx, left: int, right: int):
        """Division is for nerds"""
        await ctx.send(left / right)

        
  
    @commands.command()
    async def pfp(self, ctx, *, member: discord.Member = None):
        """Displays a user's avatar."""
        if member is None:
            member = ctx.author
        embed = discord.Embed(color=discord.Color.blue(),
                              description=f"[Link to Avatar]({member.avatar_url_as(static_format='png')})")
        embed.set_author(name=f"{member.name}\'s Avatar")
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
        

     @commands.command()
     def nick(self, ctx, *, nick: str):
        """Set your nickname.
        Usage: nick [new nickname]"""
        if ctx.author.guild_permissions.change_nickname:
            await ctx.author.edit(nick=nick, reason='User requested using command')
            await ctx.send(':thumbsup: Done.')
        else:
            await ctx.send(':x: You don\'t have permission to change your nickname.')      
            
def setup(bot):
    bot.add_cog(Skyutils(bot))
