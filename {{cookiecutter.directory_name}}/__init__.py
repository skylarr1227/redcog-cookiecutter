from .{{cookiecutter.file_name}} import {{cookiecutter.cog_name}}


def setup(bot):
    cog = {{cookiecutter.cog_name}}(bot)
    bot.add_cog(cog)