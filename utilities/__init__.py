from .utilities import Utilities


def setup(bot):
    cog = Utilities(bot)
    bot.add_cog(cog)
