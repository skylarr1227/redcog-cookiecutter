from discord.ext import commands
import discord
import random
import re
from redbot.core import Config, commands, checks


colors = {
  'DEFAULT': 0x000000,
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'GREY': 0x95A5A6,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_GREY': 0x979C9F,
  'DARKER_GREY': 0x7F8C8D,
  'LIGHT_GREY': 0xBCC0C0,
  'DARK_NAVY': 0x2C3E50,
  'BLURPLE': 0x7289DA,
  'GREYPLE': 0x99AAB5,
  'DARK_BUT_NOT_BLACK': 0x2C2F33,
  'NOT_QUITE_BLACK': 0x23272A
}

bot = commands.Bot
BaseCog = getattr(commands, "Cog", object)
listener = getattr(commands.Cog, "listener", None) 
if listener is None:
  
    def listener(name=None):
        return lambda x: x
    
class Skyembed(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(name='rhelp', description='Help menu for users +Rank Display')
    async def rank_help(self, ctx):
        embed = discord.Embed(title="Skybot's Leveling System", colour=discord.Colour(0x12bdca), description="For help with other display options within the leveler system see: `\n+lvlhelp`")

        embed.set_image(url="https://pokepla.net/rhelp.png")
        embed.set_thumbnail(url="https://pokepla.net/epic.gif")
        embed.set_author(name="+rank Display Help", url="https://pokepla.net/epic.gif", icon_url="https://pokepla.net/epic2.gif")
        embed.set_footer(text="Suggestions on how to make this better? DM Skylarr#6666!!", icon_url="https://pokepla.net/epic2.gif")

        embed.add_field(name="Rank Background Viewer", value="```+backgrounds rank```")
        embed.add_field(name="Set Rank Display Background", value="```+setrbg [bg name]```")
        embed.add_field(name="Set Rank Color Overlay [not recommended]", value="```+setrcolor [0x52345]```")

        await bot.say(embed=embed)

    @commands.command(
        name='sembed',
        description='The embed command',
    )
    async def embed_command(self, ctx):

        # Defined check function  
        def check(ms):        
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author

         #title
        await ctx.send(content='What would you like the title to be?')

        # Wait for a response and get the title
        msg = await self.bot.wait_for('message', check=check)
        title = msg.content # Set the title

        # content
        await ctx.send(content='What would you like the Description to be?')
        msg = await self.bot.wait_for('message', check=check)
        desc = msg.content

        # make and send it
        msg = await ctx.send(content='Now generating the embed...')

        color_list = [c for c in colors.values()]
        # Convert
        # random

        embed = discord.Embed(
            title=title,
            description=desc,
            color=random.choice(color_list)
        )
        # thumbnail to be the bot's pfp
        embed.set_thumbnail(url=self.bot.user.avatar_url)

        # user
        embed.set_author(
            name=ctx.message.author.name,
            icon_url=ctx.message.author.avatar_url
        )

        await msg.edit(
            embed=embed,
            content=None
        )
        
        
        

        return
        
        
       

def setup(bot):
    bot.add_cog(Skyembed(Bot))
