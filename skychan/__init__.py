from .Skychannel import CustomChannels


def setup(bot):
    bot.add_cog(Skychannel(bot))
