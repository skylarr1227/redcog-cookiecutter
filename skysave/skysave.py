from typing import Optional

import discord
from redbot.core.config import Config
from redbot.core import commands, checks
from redbot.core.i18n import Translator, cog_i18n
from redbot.core.utils.antispam import AntiSpam

from .checks import has_active_box

_ = Translator("??", __file__)


@cog_i18n(_)
class Skysave(commands.Cog):
    """
    For saving all that important shit you were otherwise going to forget
    """

    __version__ = "1.0.6"

    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        self.config = Config.get_conf(
            self, identifier=78631113035100160, force_registration=True
        )
        self.config.register_guild(
            boxes=[],
            add_reactions=False,
            reactions=["\N{THUMBS UP SIGN}", "\N{THUMBS DOWN SIGN}"],
            forms={},  
            approval_queues={},
            log_channel=None,
        )
        self.config.register_global(
            boxes=[],
            add_reactions=False,
            reactions=["\N{THUMBS UP SIGN}", "\N{THUMBS DOWN SIGN}"],
            forms={}, 
            approval_queues={},
        )
        
        self.config.init_custom("SUGGESTION", 1)
        self.config.register_custom("SUGGESTION", data={})

       
        self.config.register_member(blocked=False)
        self.config.register_user(blocked=False)
        self.antispam = {}

    @checks.admin_or_permissions(manage_guild=True)
    @commands.guild_only()
    @commands.group(name="saveset", aliases=["sset"])
    async def sset(self, ctx: commands.Context):
        """
        Setup for skysave to save important shit
        """
        pass

    @sset.command(name="make")
    async def sset_make(self, ctx, *, channel: discord.TextChannel):
        """
        sets a channel to be a save box... a place for saved shit
        """
        async with self.config.guild(ctx.guild).boxes() as boxes:
            if channel.id in boxes:
                return await ctx.send(_("Channel is already box for saving shit... get outta here with that shit"))
            boxes.append(channel.id)

        await ctx.tick()

    @sset.command(name="remove")
    async def sset_rm(self, ctx, *, channel: discord.TextChannel):
        """
        Unset a savebox
        """
        async with self.config.guild(ctx.guild).boxes() as boxes:
            if channel.id not in boxes:
                return await ctx.send(_("THIS CHANNEL IS NOT SET WHAT ARE YOU DOING??"))
            boxes.remove(channel.id)

        await ctx.tick()

    @sset.command(name="addreactions")
    async def sset_adds_reactions(self, ctx, option: bool = None):
        """
        sets whether to add reactions to saves
        displays current setting without a provided option.
        off = Don't use reactions
        on = Use reactions
        """
        if option is None:
            current = await self.config.guild(ctx.guild).add_reactions()
            if current:
                base = _(
                    "Adding Reactions to saves"
                    "\nUse {command} for more information"
                )
            else:
                base = _(
                    "Not adding Reactions to saves"
                    "\nUse {command} for more information"
                )

            await ctx.send(
                base.format(
                    command=f"`{ctx.clean_prefix}help saveset addreactions`"
                )
            )
            return

        await self.config.guild(ctx.guild).add_reactions.set(option)
        await ctx.tick()

#    @has_active_box()
    @commands.command(name="skysave")
    async def skysave(
        self,
        ctx,
        channel: Optional[discord.TextChannel] = None,
        *,
        savecontent: str = "",
    ):
        """
        Save something, anything, ill even save dick pics (forever.....)
        Options
        channel : Mention channel to specify the save destination
        """

        if ctx.guild not in self.antispam:
            self.antispam[ctx.guild] = {}

        if ctx.author not in self.antispam[ctx.guild]:
            self.antispam[ctx.guild][ctx.author] = AntiSpam([])

        if self.antispam[ctx.guild][ctx.author].spammy:
            return await ctx.send(_("Ok... Cool your fucking jets, you've been cut off from saving anything for a bit."))

        ids = await self.config.guild(ctx.guild).boxes()
        channels = [c for c in ctx.guild.text_channels if c.id in ids]
        if channel is None:

            if not channels:
                return await ctx.send(
                    _("Cannot find channels to send to, even though configured.")
                )

            if len(channels) == 1:
                channel, = channels
            else:
                base_error = _(
                    "Multiple save boxes available, "
                    "Specify one of the proper destinations next time, k?"
                )
                output = f'{base_error}\n{", ".join(c.mention for c in channels)}'
                return await ctx.send(output)

        elif channel not in channels:
            return await ctx.send(_("Does that look like a proper save destination? Come on... try again."))

        if not savecontent:
            return await ctx.send(_("Please try again while including something to save"))

        perms = channel.permissions_for(ctx.guild.me)
        if not (perms.send_messages and perms.embed_links):
            return await ctx.send(_("I don't have the required permissions... I am useless, self-destruct initiated."))

        embed = discord.Embed(color=(await ctx.embed_color()), description=savecontent)
 # embed = discord.Embed(color=(await ctx.embed_color()), description=suggestion)
        embed.set_author(
            name=_("Saved by {author_info}").format(
                author_info=f"{ctx.author.display_name} ({ctx.author.id})"
            ),
            icon_url=ctx.author.avatar_url,
        )

        try:
            msg = await channel.send(embed=embed)
        except discord.HTTPException:
            return await ctx.send(_("An unexpected error occured."))
        else:
            grp = self.config.custom("SUGGESTION", msg.id)
            async with grp.data() as data:
                data.update(
                    channel=channel.id, savecontent=savecontent, author=ctx.author.id
                )
            self.antispam[ctx.guild][ctx.author].stamp()
            await ctx.send(
                f'{ctx.author.mention}: {_("Your... whatever that is... was successfully saved")}'
            )

        if ctx.channel.permissions_for(ctx.guild.me).manage_messages:
            try:
                await ctx.message.delete()
            except discord.HTTPException:
                pass

        if await self.config.guild(ctx.guild).add_reactions():

            for reaction in await self.config.guild(ctx.guild).reactions():
                await msg.add_reaction(reaction)
