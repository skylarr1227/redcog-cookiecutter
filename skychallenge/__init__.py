from .Skychallenge import challenge


def setup(bot):
    cog = Skychallenge(bot)
    bot.add_cog(cog)
