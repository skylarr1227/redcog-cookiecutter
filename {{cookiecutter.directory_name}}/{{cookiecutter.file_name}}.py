import discord
from redbot.core import commands, checks
from redbot.core.config import Config


class {{cookiecutter.cog_name}}:
    """
    {{cookiecutter.description}}
    """

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier={{cookiecutter.config_id}},
            force_registration=True,
        )