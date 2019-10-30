from .skynote import skynote


def setup(bot):
    cog = skynote(bot)
    bot.add_cog(cog)
