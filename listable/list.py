from os import getenv
import discord
from discord.ext import commands
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from tabulate import tabulate
from redbot.core import Config, checks, commands
from redbot.core.utils import chat_formatting as cf
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS

From models import Base, List, Member, Yes


BaseCog = getattr(commands, "Cog", object)
engine = create_engine('sqlite:///listable.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()



class Listable(BaseCog)
    
    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def pong(ctx):
        '''Returns pong when called'''
        author = ctx.message.author.name
        server = ctx.message.server.name
        await bot.say('Pong for {} from {}!'.format(author, server))


    @bot.command(pass_context=True)
    async def create(ctx, name: str, date: str, time: str='0:00am'):
        '''Creates an list with specified name and date
            example: ?create party 12/22/2017 1:40pm
        '''
        server = ctx.message.server.name
        date_time = '{} {}'.format(date, time)
        try:
            list_date = datetime.strptime(date_time, '%m/%d/%Y %I:%M%p')
            list = List(name=name, server=server, date=list_date)
            session.add(list)
            session.commit()
            await bot.say('List {} created successfully for {}'.format(name, list.date))
        except Exception as e:
            await bot.say('Could not complete your command')
            print(e)



    @bot.command(pass_context=True)
    async def checkin(ctx, name: str):
       '''Allows a user to checkin on a list
             example: +checkin skysparty
       '''
        author = ctx.message.author.name
        avatar = ctx.message.author.avatar_url
        id = ctx.message.author.id

        try:
            count = session.query(Member).filter(Member.id == id).count()
            list = session.query(List).filter(List.name == name).first()

            # Verify This list exists
            if not list:
                await bot.say('This list does not exist')
                return

            # Create member if they do not exist in our database
            if count < 1:
                member = Member(id=id, name=author, avatar=avatar)
                session.add(member)

            checkedin = Yes(member_id=id, list_id=list.id)
            session.add(checkedin)
            session.commit()
            await bot.say('Member {} has checked in on list {}'.format(author, name))
        except Exception as e:
            await bot.say('Could not complete your command')
            print(e)

    @bot.command()
    async def showlists():
        '''Displays the list of all the lists
            example: +showlist
        '''
        try:
            lists = session.query(List).order_by(List.date).all()
            headers = ['Name', 'Date', 'Server']
            rows = [[e.name, e.date, e.server] for e in lists]
            table = tabulate(rows, headers)
            await bot.say('```\n' + table + '```')
            except Exception as e:
            await bot.say('Could not complete your command')
            print(e)

    @bot.command()
    async def view(name: str):
        '''Displays information about a specific list
            example: +view list
        '''
        try:
        list = session.query(List).filter(List.name == name).first()
        # Verify This list exists
        if not list:
            await bot.say('This list does not exist')
            return

            checkedin = session.query(Yes).filter(Yes.list_id == list.id).count()
            info = [['Name', list.name], ['Date', list.date], ['Server', list.server], ['Number checkedin', Yes]]
            await bot.say('```\n' + tabulate(info) + '```')
        except Exception as e:
            await bot.say('Could not complete your command')
            print(e)

