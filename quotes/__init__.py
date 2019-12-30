from .quoteit import QuoteIT


def setup(bot):
    cog = Quoteit(bot)
    bot.add_cog(cog)
