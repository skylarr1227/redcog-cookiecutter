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

From models import Base, Event, Member, Attendance


BaseCog = getattr(commands, "Cog", object)
engine = create_engine('sqlite:///listable.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()



class Listable(BaseCog)
    
    def __init__(self, bot):
        self.bot = bot


    @bot.command(pass_context=True)
    async def ping(ctx):
        '''Returns pong when called'''
        author = ctx.message.author.name
        server = ctx.message.server.name
        await bot.say('Pong for {} from {}!'.format(author, server))


    @bot.command(pass_context=True)
    async def create(ctx, name: str, date: str, time: str='0:00am'):
        '''Creates an event with specified name and date
            example: ?create party 12/22/2017 1:40pm
        '''
        server = ctx.message.server.name
        date_time = '{} {}'.format(date, time)
        try:
            event_date = datetime.strptime(date_time, '%m/%d/%Y %I:%M%p')
            event = Event(name=name, server=server, date=event_date)
            session.add(event)
            session.commit()
            await bot.say('Event {} created successfully for {}'.format(name, event.date))
        except Exception as e:
            await bot.say('Could not complete your command')
            print(e)



    @bot.command(pass_context=True)
    async def attend(ctx, name: str):
       '''Allows a user to attend an upcoming event
             example: ?attend party
       '''
        author = ctx.message.author.name
        avatar = ctx.message.author.avatar_url
        id = ctx.message.author.id

        try:
            count = session.query(Member).filter(Member.id == id).count()
            event = session.query(Event).filter(Event.name == name).first()

            # Verify This event exists
            if not event:
                await bot.say('This event does not exist')
                return

            # Create member if they do not exist in our database
            if count < 1:
                member = Member(id=id, name=author, avatar=avatar)
                session.add(member)

            attending = Attendance(member_id=id, event_id=event.id)
            session.add(attending)
            session.commit()
            await bot.say('Member {} is now attending event {}'.format(author, name))
        except Exception as e:
            await bot.say('Could not complete your command')
            print(e)

    @bot.command()
    async def list():
        '''Displays the list of current events
            example: ?list
        '''
        try:
            events = session.query(Event).order_by(Event.date).all()
            headers = ['Name', 'Date', 'Server']
            rows = [[e.name, e.date, e.server] for e in events]
            table = tabulate(rows, headers)
            await bot.say('```\n' + table + '```')
            except Exception as e:
            await bot.say('Could not complete your command')
            print(e)

    @bot.command()
    async def view(name: str):
        '''Displays information about a specific event
            example: ?view party
        '''
        try:
        event = session.query(Event).filter(Event.name == name).first()
        # Verify This event exists
        if not event:
            await bot.say('This event does not exist')
            return

            attending = session.query(Attendance).filter(Attendance.event_id == event.id).count()
            info = [['Name', event.name], ['Date', event.date], ['Server', event.server], ['Number Attending', attending]]
            await bot.say('```\n' + tabulate(info) + '```')
        except Exception as e:
            await bot.say('Could not complete your command')
            print(e)

