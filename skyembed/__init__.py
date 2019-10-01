from .skyembed import skyembed


def setup(bot):
    cog = skyembed(bot)
    bot.add_cog(cog)
