from .skylog import Skylog


def setup(bot):
    cog = skylog(bot)
    bot.add_cog(cog)
