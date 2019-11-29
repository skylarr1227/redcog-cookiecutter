from .skychallenge import Skychallenge


def setup(bot):
    cog = Skychallenge(bot)
    bot.add_cog(cog)