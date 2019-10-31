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
            Embed(title="Quick Reference cont. Loot", description="__**+loot**__\nUse to open your lootboxes\nJust specify the type\nExample:\n```+loot normal\nor\n+loot epic 10\nfor multiple at once```\n\n__**+combine**__\nCombiine your loot boxes by specifying type you wish to convert", color=0x5599ff),
            Embed(title="Quick Reference cont. Hero-classes", description="```+heroclass\n   -Bard\n   -Wizard\n   -Ramger\n   -Beserker\n   -Cleric```", color=0x191638)
        ]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()
    
    
    @commands.command()
    async def sayit(self, ctx, *, args: str):
        """
        Edit/Say a message and you can use the silentsay variable as well.
        **FLAGS**:``
            If you use `--s` as a flag, your arguments are simply what you want the bot to say and have it remove your message afterwards.
            If you use `--e` as a flag, the arguments are the message id you want to edit and the new content.
            If no flag is passed, the bot will simply send the message like normal excluding the actual command."""
        args = args.replace("@everyone", "<insert {} trying to mention everyone here>".format(str(ctx.message.author)))
        args = args.replace("@here", "<insert {} trying to mention everyone here>".format(str(ctx.message.author)))
        if args.startswith("--s"):
            if args == "--s":  # --s == silentsay
                await ctx.send("You can't silently send an empty message!")
            else:
                args = args[4:]
                await ctx.send(str(args))
                try:
                    await ctx.message.delete()
                except:
                    pass
        elif args.startswith("--e"):
            if args == "--e":  # --e == edit
                return await ctx.send("You can't edit nothingness.")
            try:
                args = args[4:]
                mid = args.split(' ')
                to_edit = await ctx.message.channel.get_message(int(mid[0]))
                content = args.replace(mid[0] + " ", "")
                try:
                    await to_edit.edit(content=content)
                except discord.Forbidden:
                    await ctx.send("Can't edit that message.")
                await ctx.message.delete()
            except discord.NotFound:
                not_found = await ctx.send("Couldn't find the message.")
                await asyncio.sleep(5)
                await not_found.delete()
                await ctx.message.delete()
            except (IndexError, ValueError):
                indx_err = await ctx.send("Usage: `g_say --e <id> <content>`")
                await asyncio.sleep(5)
                await indx_err.delete()
                await ctx.message.delete()
            except discord.Forbidden:
                err = await ctx.send("I don't have permission to delete your message.")
                await asyncio.sleep(5)
                await err.delete()
        else:
            await ctx.send(str(args))
            
            
    @commands.command()
    async def math(self, ctx, *, expression: str):
        """Evaluate complex mathematical equations (or simple ones, whatever you prefer).
        The available operations are as follows:
        `simplify, factor, derive, integrate, zeroes, tangent, area, cos, tan, arccos, arcsin, arctan, abs, log`"""
        available_endpoints = ["simplify", "factor", "derive", "integrate", "zeroes", "tangent", "area", "cos", "tan",
                               "arccos", "arcsin", "arctan", "abs", "log"]
        oper = expression.split(' -operation ')
        op = "simplify"
        if len(oper) > 1:
            try:
                if oper[1].lower() in available_endpoints:
                    op = oper[1].lower()
                else:
                    return await ctx.send(resolve_emoji('ERROR', ctx) + " S-Sorry! That operation seems invalid")
            except:
                return await ctx.send(
                    resolve_emoji('ERROR',
                                  ctx) + " Y-you need to give me a valid operation! I made a list for you in the command help.")
        expr = oper[0].replace('/', '%2F')
        r = requests.get("https://newton.now.sh/" + op + "/" + expr)
        try:
            js = r.json()
        except json.decoder.JSONDecodeError:
            return await ctx.send(resolve_emoji('ERROR', ctx) + " I-I'm sorry! Something happened with the api.")
        em = discord.Embed(title="Expression Evaluation", color=ctx.message.author.color)
        em.add_field(name="Operation", value=js['operation'], inline=False)
        em.add_field(name="Expression", value=js['expression'], inline=False)
        em.add_field(name="Result", value=js['result'], inline=False)
        em.set_footer(text="Requested by " + str(ctx.message.author))
        em.timestamp = datetime.datetime.now()
        await ctx.send(embed=em)
        
    @commands.command()
    async def define(self, ctx, word: str):
        """Define a word."""
        r = requests.get('http://api.pearson.com/v2/dictionaries/laes/entries?headword=' + word)
        js = r.json()
        if len(js['results']) > 0:
            try:
                define = js['results'][0]['senses'][0]['definition'][0]
                pos = js['results'][0]['part_of_speech']
                ex = js['results'][0]['senses'][0]['translations'][0]['example'][0]['text']
                word = js['results'][0]['headword']
                em = discord.Embed(description="**Part Of Speech:** `{1}`\n**Headword:** `{0}`".format(word, pos),
                                   color=0x8181ff)
                em.set_thumbnail(url="https://www.shareicon.net/download/2016/05/30/575440_dictionary_512x512.png")
                em.set_footer(
                    text="Requested by {} | Powered by http://api.pearson.com/".format(str(ctx.message.author)))
                em.add_field(name="Definition", value="**{}**".format(define))
                em.add_field(name="Example", value="**{}**".format(ex))
                em.set_author(name="Definition for {}".format(word),
                              icon_url=ctx.message.author.avatar_url.replace('?size=1024', ''))
                await ctx.send(embed=em)
            except KeyError:
                await ctx.send(resolve_emoji('ERROR', ctx) + " No results found.")
        else:
            await ctx.send(resolve_emoji('ERROR', ctx) + " No results found.")
            
 
            
            
def setup(bot):
    bot.add_cog(Skyutils(bot))
