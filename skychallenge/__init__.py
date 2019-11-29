from .Skychallenge import challenge


def setup(bot):
    cog = challenge(bot)
    bot.add_cog(cog)
