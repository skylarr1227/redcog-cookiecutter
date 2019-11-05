from redbot.core.utils.chat_formatting import pagify 
import re
from redbot.core import commands
import webbrowser
import random as rand
import discord
import sqlite3
import threading
from sqlite3 import Error
import math
import asyncio
import math
import os
import time
import datetime
from redbot.core import bank, commands,checks
from redbot.core.utils.menus import menu, DEFAULT_CONTROLS

def charge(amount: int):
    async def pred(ctx):
        try:
            await bank.withdraw_credits(ctx.author, amount)
        except ValueError:
            return False
        else:
            return True

    return commands.check(pred)
def givec(amount: int):
    async def pred(ctx):
        try:
            await bank.deposit_credits(ctx.author, amount)
        except ValueError:
            return False
        else:
            return True
    return commands.check(pred)
class Pokemon():
        hp:int
        atk:int
        defense:int
        spatk:int
        spdef:int
        speed:int
        lv:int
        evs:[int,int,int,int,int,int]
        nature:str
        ability:str
class blaze(commands.Cog):
    """Blazibot -- A Pokemon Bot"""
    def __init__(self, bot):
        self.bot = bot
        self.count=0
    @commands.command(name='moves' , aliases=["m"])
    async def moves (self, ctx):
        await ctx.send("this will show your selected moves") 
        conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')

        c = conn.cursor()
        c.execute(f"select selected from Players where ID='{ctx.author.id}'")
        selected=c.fetchone()
        selected=str(selected)
        selected=selected[1:-2]
        c.execute(f"select move1,move2,move3,move4 from Owned_Pokes where ID_Owned={selected} and Owner='{ctx.author.id}'")
        moves=c.fetchall()
        moves=str(moves)
        moves=moves[2:-2]
        move=moves.split(',')
        m1=move[0]
        m1=m1[1:-1]
        m2=move[1]
        m2=m2[1:-1]
        m3=move[2]
        m3=m3[1:-1]
        m4=move[3]
        m4=m4[1:-1]
        movesselected=f"""
                        ``` 
                            {m1}  |  {m2}  |
                             --------------
                            {m3}  |  {m4}  |```"""
        await ctx.send(movesselected)
        c.close()    
    @commands.command(name='doubleteam' , aliases=["agility"])
    async def doubleteam(self, ctx):
       conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
       c = conn.cursor()
       c.execute(f"select selected from Players where ID={ctx.author.id}")
       selected=c.fetchone()
       selected=str(selected)
       selected=selected[1:-2]
       c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
       selectedpoke=c.fetchone()
       selectedpoke=str(selectedpoke)
       selectedpoke=selectedpoke[1:-2]
       c.execute(f"select Name from Pokes where Number={selectedpoke}")
       selectedname=c.fetchone()
       selectedname=str(selectedname)
       selectedname=selectedname[2:-3]
       c.close()   
       await ctx.send(f"{ctx.author.mention}'s {selectedname}'s evasiveness rose-- Nothing can touch it now!")   
    @commands.command(name='defensecurl' , aliases=["df"])
    async def defensecurl(self, ctx):
       conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
       c = conn.cursor()
       c.execute(f"select selected from Players where ID={ctx.author.id}")
       selected=c.fetchone()
       selected=str(selected)
       selected=selected[1:-2]
       c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
       selectedpoke=c.fetchone()
       selectedpoke=str(selectedpoke)
       selectedpoke=selectedpoke[1:-2]
       c.execute(f"select Name from Pokes where Number={selectedpoke}")
       selectedname=c.fetchone()
       selectedname=str(selectedname)
       selectedname=selectedname[2:-3]
       c.close()   
       await ctx.send(f"{ctx.author.mention}'s {selectedname}'s defense Rose dramatically!")    
    @commands.command(name='helpinghand' , aliases=["hh"])
    async def helpinghand(self, ctx):
       conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
       c = conn.cursor()
       c.execute(f"select selected from Players where ID={ctx.author.id}")
       selected=c.fetchone()
       selected=str(selected)
       selected=selected[1:-2]
       c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
       selectedpoke=c.fetchone()
       selectedpoke=str(selectedpoke)
       selectedpoke=selectedpoke[1:-2]
       c.execute(f"select Name from Pokes where Number={selectedpoke}")
       selectedname=c.fetchone()
       selectedname=str(selectedname)
       selectedname=selectedname[2:-3]
       c.close()   
       await ctx.send(f"{ctx.author.mention}'s {selectedname} is ready to assist!") 
    @commands.command(name='givedeems' , aliases=["gd"])
    async def givedeems(self, ctx,player:discord.Member,amt:int):
        conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select redeems from Players where ID={ctx.author.id}")
        adeem=c.fetchone()
        adeem=str(adeem)
        adeem=adeem[1:-2]
        c.execute(f"select redeems from Players where ID={player.id}")
        bdeem=c.fetchone()
        bdeem=str(bdeem)
        bdeem=bdeem[1:-2]
        newbdeem=int(bdeem)+amt
        if int(adeem)>amt and player.id != ctx.author.id:
            newadeem=int(adeem)-amt
            c.execute(f"update Players set redeems={newadeem} where ID={ctx.author.id}")
            conn.commit()
            c.execute(f"update Players set redeems={newbdeem} where ID={player.id}")
            conn.commit()
            await ctx.send(f"{ctx.author.mention} has given {player.mention} {amt} redeems!")
            c.close()
        else:
            await ctx.send("You dont have that many redeems!")
            c.close()
    @commands.command(name='focusenergy' , aliases=["adrenaline"])
    async def focusenergy(self, ctx):
       conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
       c = conn.cursor()
       c.execute(f"select selected from Players where ID={ctx.author.id}")
       selected=c.fetchone()
       selected=str(selected)
       selected=selected[1:-2]
       c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
       selectedpoke=c.fetchone()
       selectedpoke=str(selectedpoke)
       selectedpoke=selectedpoke[1:-2]
       c.execute(f"select Name from Pokes where Number={selectedpoke}")
       selectedname=c.fetchone()
       selectedname=str(selectedname)
       selectedname=selectedname[2:-3]
       c.close()
       await ctx.send(f"{ctx.author.mention}'s {selectedname} is getting pumped!")
    @commands.command(name='raid' , aliases=["rp"])
    @commands.cooldown(1, 3600,commands.BucketType.user)
    async def raid(self, ctx):
        conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')

        c = conn.cursor()
        c.execute(f"select name from raidtable")
        namelist=c.fetchall()
        namelist=str(namelist)
        namelist=namelist.replace("(","")
        namelist=namelist.replace(")","")
        namelist=namelist.replace("[","")
        namelist=namelist.replace("]","")
        namelist=namelist.replace("'","")
        namelist=namelist.replace(",,",",")
        namelist=namelist.replace(" ","")
        numpokeraid=namelist.split(',')
        numberofnames=len(numpokeraid)
        selectedboss=rand.randint(0,numberofnames)
        
        selectedbosspoke=numpokeraid[selectedboss]
        embed = discord.Embed(title=selectedbosspoke, description="Group Pokemon Raid", color=0x00ff00)
        embed.set_image(url=f"http://157.245.8.88/html/dex/media/pokemon/sugimori/{selectedbosspoke}.png")
        embed.add_field(name="How to play!", value="React to Fight the Boss!", inline=False)
        raidstuff=await ctx.send(embed=embed)
        raidtime=20
        
        
        await raidstuff.add_reaction("⚔")
        
        await raidstuff.add_reaction("🛡")
         
        await raidstuff.add_reaction("🍙")
             
        reactioncount=20
        raids = discord.Embed(title='raidstimer', description="Raid Timer", color=0x00ff00)
        raids.add_field(name="Countdown", value=str(raidtime), inline=False)       
        ti=await ctx.send("start timer")
        players1=[]
        players2=[]
        players3=[]
        reactioncount=2
        while raidtime>0:
        
            raidtime -=1
            await asyncio.sleep(1)
            await ti.edit(content=str(raidtime))
          
            reactionstuff=['⚔','🛡','🍙']
            
        if raidtime<=0:
                await ti.edit(content="Calculating..")
                raidstuff = await raidstuff.channel.fetch_message(raidstuff.id)
                output = ""
                user_ids= ""
                output = '\n'.join(f"{r.emoji}: {r.count}" for r in raidstuff.reactions)
                
                currentlist=0
                plist=[]
                for reaction in raidstuff.reactions:
                    if reaction.emoji not in reactionstuff:
                        continue
                    emoji = reaction.emoji
                    user_ids = [u.id async for u in reaction.users()]
                    plist.append(user_ids)
                    currentlist = 1 +currentlist
        fightingpokes=[]
        defendingpokes=[]
        supportingpokes=[]
        fightinglevel=[]
        defendivs=[]
        atkivs=[]
        p=0
        p0len=len(plist[0])
        a0len=len(plist[1])
        b0len=len(plist[2])
        while p< p0len:
            c.execute(f"select selected from Players where ID={plist[0][p]}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            if 'o'not in selected: 
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner=={plist[0][p]}")
                pokenum=c.fetchone()
                pokenum=str(pokenum)
                pokenum=pokenum[1:-2]
                c.execute(f"select level from Owned_Pokes where Number_Caught={selected} and Owner=={plist[0][p]}")
                level=c.fetchone()
                level=str(level)
                level=level[1:-2]
                fightinglevel.append(level)
                c.execute(f"select atk from Owned_Pokes where Number_Caught={selected} and Owner=={plist[0][p]}")
                atk=c.fetchone()
                atk=str(atk)
                atk=atk[1:-2]
                atkivs.append(atk)
                c.execute(f"select def from Owned_Pokes where Number_Caught={selected} and Owner=={plist[0][p]}")
                df=c.fetchone()
                df=str(df)
                df=df[1:-2]
                defendivs.append(df)
                c.execute(f"select Name from Pokes where Number={pokenum}")
                name=c.fetchone()
                name=str(name)
                name=name[2:-3]
                fightingpokes.append(name)
            p=p+1
        a=0
        while a< a0len:
            c.execute(f"select selected from Players where ID={plist[1][a]}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            if 'o'not in selected: 
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner=={plist[1][a]}")
                pokenum=c.fetchone()
                pokenum=str(pokenum)
                pokenum=pokenum[1:-2]
                c.execute(f"select Name from Pokes where Number={pokenum}")
                name=c.fetchone()
                name=str(name)
                name=name[2:-3]
                defendingpokes.append(name)
            a=a+1
        b=0
        while b< b0len:
            c.execute(f"select selected from Players where ID={plist[2][b]}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            if 'o'not in selected: 
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner=={plist[2][b]}")
                pokenum=c.fetchone()
                pokenum=str(pokenum)
                pokenum=pokenum[1:-2]
                c.execute(f"select Name from Pokes where Number={pokenum}")
                name=c.fetchone()
                name=str(name)
                name=name[2:-3]
                supportingpokes.append(name)
            b=b+1        
        attackpower=0
        defendpower=0
        hppower=0
        speedpower=0
        supportpower=0
        
        for pk in fightingpokes:
            c.execute(f"select attack from Pokes where Name='{pk}'")
            atk=c.fetchone()
            atk=str(atk)
            atk=atk[1:-2]
            level=fightinglevel[fightingpokes.index(pk)]
            atkiv=fightinglevel[fightingpokes.index(pk)]
            atk=int(atk)*int(atkiv)
            atk=atk/1000
            atk=atk*int(level)
            atk=atk*1.5
            attackpower=attackpower+int(atk)
            
        for pk in defendingpokes:
            c.execute(f"select defense from Pokes where Name='{pk}'")
            df=c.fetchone()
            df=str(df)
            df=df[1:-2]
            level=fightinglevel[defendingpokes.index(pk)]
            defenseiv=fightinglevel[defendingpokes.index(pk)]
            df=int(df)*int(defenseiv)
            df=df/1000
            df=df*int(level)
            df=df*2
            defense=+defendpower+int(atk)
        for pk in supportingpokes:
            c.execute(f"select attack from Pokes where Name='{pk}'")
            atk=c.fetchone()
            atk=str(atk)
            atk=atk[1:-2]
            c.execute(f"select level from Owned_Pokes")
            level=c.fetchone()
            level=str(level)
            level=level[1:-2]
            atk=int(atk)*int(level)
            atk=atk/2
            atk=int(atk)
            
            suportpower=supportpower+int(atk)
            supportpower=supportpower+20
        attackpower=attackpower+supportpower
        defparty=len(fightingpokes)+len(defendingpokes)+len(supportingpokes)
        c.execute(f"select attack,defense from raidtable where name='{selectedbosspoke}'")
        bosstat=c.fetchall()
        bosstat=str(bosstat)
        bosstat=bosstat.replace("[","")
        bosstat=bosstat.replace("]","")
        bosstat=bosstat.replace(")","")
        bosstat=bosstat.replace("(","")
        bosstat=bosstat.replace(",,",",")
        stats=bosstat.split(',')
        bossatk=int(stats[0])
        raideratk=int(attackpower)
        
        while bossatk>1 and raideratk>1: 
            if raideratk<1:
                await ctx.send("Raiders win!")
                c.execute(f"select cash from raidtable where name='{selectedbosspoke}'")
                cash=c.fetchone()
                cash=str(cash)
                cash=cash[1:-2]
                cash=int(cash)                
                c.execute(f"select items from raidtable where name='{selectedbosspoke}'")
                items=c.fetchone()
                items=str(items)
                items=items[2:-3]
                items=items.replace("'","")
                i=0
                plen=len(plist[0])
                for l in plist[0]:
                    g=str(l)
                    user= ctx.get_user(g)
                    await ctx.send(f"{user.mention}")
                    await bank.deposit_credits(user, cash/10)
                    
                    
            
            raideratk=raideratk-int(stats[1])            
            bossatk=bossatk-defense      
            if raideratk<1:
                await ctx.send("The raid boss won.better luck next time.")
                
            elif (bossatk<1):
                await ctx.send("Raiders win!")
                c.execute(f"select cash from raidtable where name='{selectedbosspoke}'")
                cash=c.fetchone()
                cash=str(cash)
                cash=cash[1:-2]
                cash=int(cash)
                c.execute(f"select items from raidtable where name='{selectedbosspoke}'")
                items=c.fetchone()
                items=str(items)
                items=items[2:-3]
                items=items.replace("'","")
                items=items.replace("\,",",")
                itemslist=items.split(',')
                itemlen=len(itemslist)
                randitem=rand.randint(0,itemlen-1)
                item=itemslist[randitem]
                item=item.replace("\\","")
                
                
                
                
                i=0
                plen=len(plist[0])
                for l in plist[0]:
                    g=str(l)
                    user=  self.bot.get_user(int(g))
                    await bank.deposit_credits(user, cash)
                    c.execute(f"select number from items where name='{item}' and Owner={user.id}")
                    num=c.fetchone()
                    num=str(num)
        
                    if "None" in num:
                        c.execute(f"insert into items(Owner,name,number) Values({user.id},'{item}',1);")
                        conn.commit()
                    else:
                        num=num[1:-2]
                        num=int(num)
                        c.execute(f"update items set number={num+1} where name='{item}' and Owner={user.id}")
                        conn.commit()
                await ctx.send(f"Raiders won {str(cash)} credits and 1 {item}")
                
                
            else:
                " "
                
            
       
            
            
      
            
    @commands.command(name='howto' , aliases=["how"])
    async def howto(self, ctx):
        info="""Tutorial For Blazibot!
        
[1] To start just type -start
[2] You probably want to view it now, don't you? Well just type -i 1
[3] Maybe you want some credits to start your journey, just type -payday
[4] Okay dueling, at this point in time, you are allowed to duel yourself for some easy credits, however, this will get removed later on, dueling others works too, just type -battle @(player's name)
[5] Say you want a specific pokemon to spawn and it wont, just type -spawn (pokemon type) and a pokemon of that typing will spawn
[6] The market works, just items do not
[7] If you want to become a gym leader There are perks There are 5 open spots left, Normal, Steel, Ice, Electric, and Rock. If you dont want to be any of those, but you still wanna be one, you can be the co-leader, you would do the gym if the leader is sleeping or school
[8] Trading is not added yet too
[9] Kensei (the owner if the bot and amazing person) creates little easter eggs ever-now-and-then. He is the only one who knows that the answer is so everyone is racing to solve them. there are nice prizes wink
[10] To learn moves for your battling experiences, type -moveset and -learn (1-4) (move name) and if there is two words in the move name, put a - where the space is. Right now, pokemon moves are based on their type, so say I had a pikachu, that pikachu would be able to learn every electric move."""
        await ctx.send_interactive(pagify("```"+info+"```"))
    @commands.command(name='npc' , aliases=["duel"])
    @commands.cooldown(1, 10800,commands.BucketType.user)
    async def npc(self, ctx):
        await ctx.send("This will be NPC duels")
        npcrand=rand.randint(-17,809)
        conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select Type from Pokes where Number={npcrand}")
        npctype=c.fetchone()
        npctype=str(npctype)
        npctype=npctype[2:-3]
        await ctx.send(npctype)
        c.execute(f"select Name from Pokes where Number={npcrand}")
        npcname=c.fetchone()
        npcname=str(npcname)
        npcname=npcname[2:-3]
        names = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan", "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul", "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed", "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel", "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam", "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil", "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed", "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian", "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay", "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert", "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs", "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf", "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider", "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen", "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan", "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer", "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs", "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet", "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio", "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep", "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez", "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis", "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran", "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved", "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley", "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal", "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun", "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan", "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub", "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise", "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley", "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz", "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz", "Benedict", "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay", "Bernard", "Bertie", "Bevin", "Bezalel", "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod", "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", "Blessing", "Blue", "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony", "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly", "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden", "Brandon", "Brandonlee", "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme", "Brendan", "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody", "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan", "Bryce", "Bryden", "Brydon", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak", "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan", "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Caiden", "Caiden-Paul", "Caidyn", "Caie", "Cailaen", "Cailean", "Caileb-John", "Cailin", "Cain", "Caine", "Cairn", "Cal", "Calan", "Calder", "Cale", "Calean", "Caleb", "Calen", "Caley", "Calib", "Calin", "Callahan", "Callan", "Callan-Adam", "Calley", "Callie", "Callin", "Callum", "Callun", "Callyn", "Calum", "Calum-James", "Calvin", "Cambell", "Camerin", "Cameron", "Campbel", "Campbell", "Camron", "Caolain", "Caolan", "Carl", "Carlo", "Carlos", "Carrich", "Carrick", "Carson", "Carter", "Carwyn", "Casey", "Casper", "Cassy", "Cathal", "Cator", "Cavan", "Cayden", "Cayden-Robert", "Cayden-Tiamo", "Ceejay", "Ceilan", "Ceiran", "Ceirin", "Ceiron", "Cejay", "Celik", "Cephas", "Cesar", "Cesare", "Chad", "Chaitanya", "Chang-Ha", "Charles", "Charley", "Charlie", "Charly", "Chase", "Che", "Chester", "Chevy", "Chi", "Chibudom", "Chidera", "Chimsom", "Chin", "Chintu", "Chiqal", "Chiron", "Chris", "Chris-Daniel", "Chrismedi", "Christian", "Christie", "Christoph", "Christopher", "Christopher-Lee", "Christy", "Chu", "Chukwuemeka", "Cian", "Ciann", "Ciar", "Ciaran", "Ciarian", "Cieran", "Cillian", "Cillin", "Cinar", "CJ", "C-Jay", "Clark", "Clarke", "Clayton", "Clement", "Clifford", "Clyde", "Cobain", "Coban", "Coben", "Cobi", "Cobie", "Coby", "Codey", "Codi", "Codie", "Cody", "Cody-Lee", "Coel", "Cohan", "Cohen", "Colby", "Cole", "Colin", "Coll", "Colm", "Colt", "Colton", "Colum", "Colvin", "Comghan", "Conal", "Conall", "Conan", "Conar", "Conghaile", "Conlan", "Conley", "Conli", "Conlin", "Conlly", "Conlon", "Conlyn", "Connal", "Connall", "Connan", "Connar", "Connel", "Connell", "Conner", "Connolly", "Connor", "Connor-David", "Conor", "Conrad", "Cooper", "Copeland", "Coray", "Corben", "Corbin", "Corey", "Corey-James", "Corey-Jay", "Cori", "Corie", "Corin", "Cormac", "Cormack", "Cormak", "Corran", "Corrie", "Cory", "Cosmo", "Coupar", "Craig", "Craig-James", "Crawford", "Creag", "Crispin", "Cristian", "Crombie", "Cruiz", "Cruz", "Cuillin", "Cullen", "Cullin", "Curtis", "Cyrus", "Daanyaal", "Daegan", "Daegyu", "Dafydd", "Dagon", "Dailey", "Daimhin", "Daithi", "Dakota", "Daksh", "Dale", "Dalong", "Dalton", "Damian", "Damien", "Damon", "Dan", "Danar", "Dane", "Danial", "Daniel", "Daniele", "Daniel-James", "Daniels", "Daniil", "Danish", "Daniyal", "Danniel", "Danny", "Dante", "Danyal", "Danyil", "Danys", "Daood", "Dara", "Darach", "Daragh", "Darcy", "D'arcy", "Dareh", "Daren", "Darien", "Darius", "Darl", "Darn", "Darrach", "Darragh", "Darrel", "Darrell", "Darren", "Darrie", "Darrius", "Darroch", "Darryl", "Darryn", "Darwyn", "Daryl", "Daryn", "Daud", "Daumantas", "Davi", "David", "David-Jay", "David-Lee", "Davie", "Davis", "Davy", "Dawid", "Dawson", "Dawud", "Dayem", "Daymian", "Deacon", "Deagan", "Dean", "Deano", "Decklan", "Declain", "Declan", "Declyan", "Declyn", "Dedeniseoluwa", "Deecan", "Deegan", "Deelan", "Deklain-Jaimes", "Del", "Demetrius", "Denis", "Deniss", "Dennan", "Dennin", "Dennis", "Denny", "Dennys", "Denon", "Denton", "Denver", "Denzel", "Deon", "Derek", "Derick", "Derin", "Dermot", "Derren", "Derrie", "Derrin", "Derron", "Derry", "Derryn", "Deryn", "Deshawn", "Desmond", "Dev", "Devan", "Devin", "Devlin", "Devlyn", "Devon", "Devrin", "Devyn", "Dex", "Dexter", "Dhani", "Dharam", "Dhavid", "Dhyia", "Diarmaid", "Diarmid", "Diarmuid", "Didier", "Diego", "Diesel", "Diesil", "Digby", "Dilan", "Dilano", "Dillan", "Dillon", "Dilraj", "Dimitri", "Dinaras", "Dion", "Dissanayake", "Dmitri", "Doire", "Dolan", "Domanic", "Domenico", "Domhnall", "Dominic", "Dominick", "Dominik", "Donald", "Donnacha", "Donnie", "Dorian", "Dougal", "Douglas", "Dougray", "Drakeo", "Dre", "Dregan", "Drew", "Dugald", "Duncan", "Duriel", "Dustin", "Dylan", "Dylan-Jack", "Dylan-James", "Dylan-John", "Dylan-Patrick", "Dylin", "Dyllan", "Dyllan-James", "Dyllon", "Eadie", "Eagann", "Eamon", "Eamonn", "Eason", "Eassan", "Easton", "Ebow", "Ed", "Eddie", "Eden", "Ediomi", "Edison", "Eduardo", "Eduards", "Edward", "Edwin", "Edwyn", "Eesa", "Efan", "Efe", "Ege", "Ehsan", "Ehsen", "Eiddon", "Eidhan", "Eihli", "Eimantas", "Eisa", "Eli", "Elias", "Elijah", "Eliot", "Elisau", "Eljay", "Eljon", "Elliot", "Elliott", "Ellis", "Ellisandro", "Elshan", "Elvin", "Elyan", "Emanuel", "Emerson", "Emil", "Emile", "Emir", "Emlyn", "Emmanuel", "Emmet", "Eng", "Eniola", "Enis", "Ennis", "Enrico", "Enrique", "Enzo", "Eoghain", "Eoghan", "Eoin", "Eonan", "Erdehan", "Eren", "Erencem", "Eric", "Ericlee", "Erik", "Eriz", "Ernie-Jacks", "Eroni", "Eryk", "Eshan", "Essa", "Esteban", "Ethan", "Etienne", "Etinosa", "Euan", "Eugene", "Evan", "Evann", "Ewan", "Ewen", "Ewing", "Exodi", "Ezekiel", "Ezra", "Fabian", "Fahad", "Faheem", "Faisal", "Faizaan", "Famara", "Fares", "Farhaan", "Farhan", "Farren", "Farzad", "Fauzaan", "Favour", "Fawaz", "Fawkes", "Faysal", "Fearghus", "Feden", "Felix", "Fergal", "Fergie", "Fergus", "Ferre", "Fezaan", "Fiachra", "Fikret", "Filip", "Filippo", "Finan", "Findlay", "Findlay-James", "Findlie", "Finlay", "Finley", "Finn", "Finnan", "Finnean", "Finnen", "Finnlay", "Finnley", "Fintan", "Fionn", "Firaaz", "Fletcher", "Flint", "Florin", "Flyn", "Flynn", "Fodeba", "Folarinwa", "Forbes", "Forgan", "Forrest", "Fox", "Francesco", "Francis", "Francisco", "Franciszek", "Franco", "Frank", "Frankie", "Franklin", "Franko", "Fraser", "Frazer", "Fred", "Freddie", "Frederick", "Fruin", "Fyfe", "Fyn", "Fynlay", "Fynn", "Gabriel", "Gallagher", "Gareth", "Garren", "Garrett", "Garry", "Gary", "Gavin", "Gavin-Lee", "Gene", "Geoff", "Geoffrey", "Geomer", "Geordan", "Geordie", "George", "Georgia", "Georgy", "Gerard", "Ghyll", "Giacomo", "Gian", "Giancarlo", "Gianluca", "Gianmarco", "Gideon", "Gil", "Gio", "Girijan", "Girius", "Gjan", "Glascott", "Glen", "Glenn", "Gordon", "Grady", "Graeme", "Graham", "Grahame", "Grant", "Grayson", "Greg", "Gregor", "Gregory", "Greig", "Griffin", "Griffyn", "Grzegorz", "Guang", "Guerin", "Guillaume", "Gurardass", "Gurdeep", "Gursees", "Gurthar", "Gurveer", "Gurwinder", "Gus", "Gustav", "Guthrie", "Guy", "Gytis", "Habeeb", "Hadji", "Hadyn", "Hagun", "Haiden", "Haider", "Hamad", "Hamid", "Hamish", "Hamza", "Hamzah", "Han", "Hansen", "Hao", "Hareem", "Hari", "Harikrishna", "Haris", "Harish", "Harjeevan", "Harjyot", "Harlee", "Harleigh", "Harley", "Harman", "Harnek", "Harold", "Haroon", "Harper", "Harri", "Harrington", "Harris", "Harrison", "Harry", "Harvey", "Harvie", "Harvinder", "Hasan", "Haseeb", "Hashem", "Hashim", "Hassan", "Hassanali", "Hately", "Havila", "Hayden", "Haydn", "Haydon", "Haydyn", "Hcen", "Hector", "Heddle", "Heidar", "Heini", "Hendri", "Henri", "Henry", "Herbert", "Heyden", "Hiro", "Hirvaansh", "Hishaam", "Hogan", "Honey", "Hong", "Hope", "Hopkin", "Hosea", "Howard", "Howie", "Hristomir", "Hubert", "Hugh", "Hugo", "Humza", "Hunter", "Husnain", "Hussain", "Hussan", "Hussnain", "Hussnan", "Hyden", "I", "Iagan", "Iain", "Ian", "Ibraheem", "Ibrahim", "Idahosa", "Idrees", "Idris", "Iestyn", "Ieuan", "Igor", "Ihtisham", "Ijay", "Ikechukwu", "Ikemsinachukwu", "Ilyaas", "Ilyas", "Iman", "Immanuel", "Inan", "Indy", "Ines", "Innes", "Ioannis", "Ireayomide", "Ireoluwa", "Irvin", "Irvine", "Isa", "Isaa", "Isaac", "Isaiah", "Isak", "Isher", "Ishwar", "Isimeli", "Isira", "Ismaeel", "Ismail", "Israel", "Issiaka", "Ivan", "Ivar", "Izaak", "J", "Jaay", "Jac", "Jace", "Jack", "Jacki", "Jackie", "Jack-James", "Jackson", "Jacky", "Jacob", "Jacques", "Jad", "Jaden", "Jadon", "Jadyn", "Jae", "Jagat", "Jago", "Jaheim", "Jahid", "Jahy", "Jai", "Jaida", "Jaiden", "Jaidyn", "Jaii", "Jaime", "Jai-Rajaram", "Jaise", "Jak", "Jake", "Jakey", "Jakob", "Jaksyn", "Jakub", "Jamaal", "Jamal", "Jameel", "Jameil", "James", "James-Paul", "Jamey", "Jamie", "Jan", "Jaosha", "Jardine", "Jared", "Jarell", "Jarl", "Jarno", "Jarred", "Jarvi", "Jasey-Jay", "Jasim", "Jaskaran", "Jason", "Jasper", "Jaxon", "Jaxson", "Jay", "Jaydan", "Jayden", "Jayden-James", "Jayden-Lee", "Jayden-Paul", "Jayden-Thomas", "Jaydn", "Jaydon", "Jaydyn", "Jayhan", "Jay-Jay", "Jayke", "Jaymie", "Jayse", "Jayson", "Jaz", "Jazeb", "Jazib", "Jazz", "Jean", "Jean-Lewis", "Jean-Pierre", "Jebadiah", "Jed", "Jedd", "Jedidiah", "Jeemie", "Jeevan", "Jeffrey", "Jensen", "Jenson", "Jensyn", "Jeremy", "Jerome", "Jeronimo", "Jerrick", "Jerry", "Jesse", "Jesuseun", "Jeswin", "Jevan", "Jeyun", "Jez", "Jia", "Jian", "Jiao", "Jimmy", "Jincheng", "JJ", "Joaquin", "Joash", "Jock", "Jody", "Joe", "Joeddy", "Joel", "Joey", "Joey-Jack", "Johann", "Johannes", "Johansson", "John", "Johnathan", "Johndean", "Johnjay", "John-Michael", "Johnnie", "Johnny", "Johnpaul", "John-Paul", "John-Scott", "Johnson", "Jole", "Jomuel", "Jon", "Jonah", "Jonatan", "Jonathan", "Jonathon", "Jonny", "Jonothan", "Jon-Paul", "Jonson", "Joojo", "Jordan", "Jordi", "Jordon", "Jordy", "Jordyn", "Jorge", "Joris", "Jorryn", "Josan", "Josef", "Joseph", "Josese", "Josh", "Joshiah", "Joshua", "Josiah", "Joss", "Jostelle", "Joynul", "Juan", "Jubin", "Judah", "Jude", "Jules", "Julian", "Julien", "Jun", "Junior", "Jura", "Justan", "Justin", "Justinas", "Kaan", "Kabeer", "Kabir", "Kacey", "Kacper", "Kade", "Kaden", "Kadin", "Kadyn", "Kaeden", "Kael", "Kaelan", "Kaelin", "Kaelum", "Kai", "Kaid", "Kaidan", "Kaiden", "Kaidinn", "Kaidyn", "Kaileb", "Kailin", "Kain", "Kaine", "Kainin", "Kainui", "Kairn", "Kaison", "Kaiwen", "Kajally", "Kajetan", "Kalani", "Kale", "Kaleb", "Kaleem", "Kal-el", "Kalen", "Kalin", "Kallan", "Kallin", "Kalum", "Kalvin", "Kalvyn", "Kameron", "Kames", "Kamil", "Kamran", "Kamron", "Kane", "Karam", "Karamvir", "Karandeep", "Kareem", "Karim", "Karimas", "Karl", "Karol", "Karson", "Karsyn", "Karthikeya", "Kasey", "Kash", "Kashif", "Kasim", "Kasper", "Kasra", "Kavin", "Kayam", "Kaydan", "Kayden", "Kaydin", "Kaydn", "Kaydyn", "Kaydyne", "Kayleb", "Kaylem", "Kaylum", "Kayne", "Kaywan", "Kealan", "Kealon", "Kean", "Keane", "Kearney", "Keatin", "Keaton", "Keavan", "Keayn", "Kedrick", "Keegan", "Keelan", "Keelin", "Keeman", "Keenan", "Keenan-Lee", "Keeton", "Kehinde", "Keigan", "Keilan", "Keir", "Keiran", "Keiren", "Keiron", "Keiryn", "Keison", "Keith", "Keivlin", "Kelam", "Kelan", "Kellan", "Kellen", "Kelso", "Kelum", "Kelvan", "Kelvin", "Ken", "Kenan", "Kendall", "Kendyn", "Kenlin", "Kenneth", "Kensey", "Kenton", "Kenyon", "Kenzeigh", "Kenzi", "Kenzie", "Kenzo", "Kenzy", "Keo", "Ker", "Kern", "Kerr", "Kevan", "Kevin", "Kevyn", "Kez", "Khai", "Khalan", "Khaleel", "Khaya", "Khevien", "Khizar", "Khizer", "Kia", "Kian", "Kian-James", "Kiaran", "Kiarash", "Kie", "Kiefer", "Kiegan", "Kienan", "Kier", "Kieran", "Kieran-Scott", "Kieren", "Kierin", "Kiern", "Kieron", "Kieryn", "Kile", "Killian", "Kimi", "Kingston", "Kinneil", "Kinnon", "Kinsey", "Kiran", "Kirk", "Kirwin", "Kit", "Kiya", "Kiyonari", "Kjae", "Klein", "Klevis", "Kobe", "Kobi", "Koby", "Koddi", "Koden", "Kodi", "Kodie", "Kody", "Kofi", "Kogan", "Kohen", "Kole", "Konan", "Konar", "Konnor", "Konrad", "Koray", "Korben", "Korbyn", "Korey", "Kori", "Korrin", "Kory", "Koushik", "Kris", "Krish", "Krishan", "Kriss", "Kristian", "Kristin", "Kristofer", "Kristoffer", "Kristopher", "Kruz", "Krzysiek", "Krzysztof", "Ksawery", "Ksawier", "Kuba", "Kurt", "Kurtis", "Kurtis-Jae", "Kyaan", "Kyan", "Kyde", "Kyden", "Kye", "Kyel", "Kyhran", "Kyie", "Kylan", "Kylar", "Kyle", "Kyle-Derek", "Kylian", "Kym", "Kynan", "Kyral", "Kyran", "Kyren", "Kyrillos", "Kyro", "Kyron", "Kyrran", "Lachlainn", "Lachlan", "Lachlann", "Lael", "Lagan", "Laird", "Laison", "Lakshya", "Lance", "Lancelot", "Landon", "Lang", "Lasse", "Latif", "Lauchlan", "Lauchlin", "Laughlan", "Lauren", "Laurence", "Laurie", "Lawlyn", "Lawrence", "Lawrie", "Lawson", "Layne", "Layton", "Lee", "Leigh", "Leigham", "Leighton", "Leilan", "Leiten", "Leithen", "Leland", "Lenin", "Lennan", "Lennen", "Lennex", "Lennon", "Lennox", "Lenny", "Leno", "Lenon", "Lenyn", "Leo", "Leon", "Leonard", "Leonardas", "Leonardo", "Lepeng", "Leroy", "Leven", "Levi", "Levon", "Levy", "Lewie", "Lewin", "Lewis", "Lex", "Leydon", "Leyland", "Leylann", "Leyton", "Liall", "Liam", "Liam-Stephen", "Limo", "Lincoln", "Lincoln-John", "Lincon", "Linden", "Linton", "Lionel", "Lisandro", "Litrell", "Liyonela-Elam", "LLeyton", "Lliam", "Lloyd", "Lloyde", "Loche", "Lochlan", "Lochlann", "Lochlan-Oliver", "Lock", "Lockey", "Logan", "Logann", "Logan-Rhys", "Loghan", "Lokesh", "Loki", "Lomond", "Lorcan", "Lorenz", "Lorenzo", "Lorne", "Loudon", "Loui", "Louie", "Louis", "Loukas", "Lovell", "Luc", "Luca", "Lucais", "Lucas", "Lucca", "Lucian", "Luciano", "Lucien", "Lucus", "Luic", "Luis", "Luk", "Luka", "Lukas", "Lukasz", "Luke", "Lukmaan", "Luqman", "Lyall", "Lyle", "Lyndsay", "Lysander", "Maanav", "Maaz", "Mac", "Macallum", "Macaulay", "Macauley", "Macaully", "Machlan", "Maciej", "Mack", "Mackenzie", "Mackenzy", "Mackie", "Macsen", "Macy", "Madaki", "Maddison", "Maddox", "Madison", "Madison-Jake", "Madox", "Mael", "Magnus", "Mahan", "Mahdi", "Mahmoud", "Maias", "Maison", "Maisum", "Maitlind", "Majid", "Makensie", "Makenzie", "Makin", "Maksim", "Maksymilian", "Malachai", "Malachi", "Malachy", "Malakai", "Malakhy", "Malcolm", "Malik", "Malikye", "Malo", "Ma'moon", "Manas", "Maneet", "Manmohan", "Manolo", "Manson", "Mantej", "Manuel", "Manus", "Marc", "Marc-Anthony", "Marcel", "Marcello", "Marcin", "Marco", "Marcos", "Marcous", "Marcquis", "Marcus", "Mario", "Marios", "Marius", "Mark", "Marko", "Markus", "Marley", "Marlin", "Marlon", "Maros", "Marshall", "Martin", "Marty", "Martyn", "Marvellous", "Marvin", "Marwan", "Maryk", "Marzuq", "Mashhood", "Mason", "Mason-Jay", "Masood", "Masson", "Matas", "Matej", "Mateusz", "Mathew", "Mathias", "Mathu", "Mathuyan", "Mati", "Matt", "Matteo", "Matthew", "Matthew-William", "Matthias", "Max", "Maxim", "Maximilian", "Maximillian", "Maximus", "Maxwell", "Maxx", "Mayeul", "Mayson", "Mazin", "Mcbride", "McCaulley", "McKade", "McKauley", "McKay", "McKenzie", "McLay", "Meftah", "Mehmet", "Mehraz", "Meko", "Melville", "Meshach", "Meyzhward", "Micah", "Michael", "Michael-Alexander", "Michael-James", "Michal", "Michat", "Micheal", "Michee", "Mickey", "Miguel", "Mika", "Mikael", "Mikee", "Mikey", "Mikhail", "Mikolaj", "Miles", "Millar", "Miller", "Milo", "Milos", "Milosz", "Mir", "Mirza", "Mitch", "Mitchel", "Mitchell", "Moad", "Moayd", "Mobeen", "Modoulamin", "Modu", "Mohamad", "Mohamed", "Mohammad", "Mohammad-Bilal", "Mohammed", "Mohanad", "Mohd", "Momin", "Momooreoluwa", "Montague", "Montgomery", "Monty", "Moore", "Moosa", "Moray", "Morgan", "Morgyn", "Morris", "Morton", "Moshy", "Motade", "Moyes", "Msughter", "Mueez", "Muhamadjavad", "Muhammad", "Muhammed", "Muhsin", "Muir", "Munachi", "Muneeb", "Mungo", "Munir", "Munmair", "Munro", "Murdo", "Murray", "Murrough", "Murry", "Musa", "Musse", "Mustafa", "Mustapha", "Muzammil", "Muzzammil", "Mykie", "Myles", "Mylo", "Nabeel", "Nadeem", "Nader", "Nagib", "Naif", "Nairn", "Narvic", "Nash", "Nasser", "Nassir", "Natan", "Nate", "Nathan", "Nathanael", "Nathanial", "Nathaniel", "Nathan-Rae", "Nawfal", "Nayan", "Neco", "Neil", "Nelson", "Neo", "Neshawn", "Nevan", "Nevin", "Ngonidzashe", "Nial", "Niall", "Nicholas", "Nick", "Nickhill", "Nicki", "Nickson", "Nicky", "Nico", "Nicodemus", "Nicol", "Nicolae", "Nicolas", "Nidhish", "Nihaal", "Nihal", "Nikash", "Nikhil", "Niki", "Nikita", "Nikodem", "Nikolai", "Nikos", "Nilav", "Niraj", "Niro", "Niven", "Noah", "Noel", "Nolan", "Noor", "Norman", "Norrie", "Nuada", "Nyah", "Oakley", "Oban", "Obieluem", "Obosa", "Odhran", "Odin", "Odynn", "Ogheneochuko", "Ogheneruno", "Ohran", "Oilibhear", "Oisin", "Ojima-Ojo", "Okeoghene", "Olaf", "Ola-Oluwa", "Olaoluwapolorimi", "Ole", "Olie", "Oliver", "Olivier", "Oliwier", "Ollie", "Olurotimi", "Oluwadamilare", "Oluwadamiloju", "Oluwafemi", "Oluwafikunayomi", "Oluwalayomi", "Oluwatobiloba", "Oluwatoni", "Omar", "Omri", "Oran", "Orin", "Orlando", "Orley", "Orran", "Orrick", "Orrin", "Orson", "Oryn", "Oscar", "Osesenagha", "Oskar", "Ossian", "Oswald", "Otto", "Owain", "Owais", "Owen", "Owyn", "Oz", "Ozzy", "Pablo", "Pacey", "Padraig", "Paolo", "Pardeepraj", "Parkash", "Parker", "Pascoe", "Pasquale", "Patrick", "Patrick-John", "Patrikas", "Patryk", "Paul", "Pavit", "Pawel", "Pawlo", "Pearce", "Pearse", "Pearsen", "Pedram", "Pedro", "Peirce", "Peiyan", "Pele", "Peni", "Peregrine", "Peter", "Phani", "Philip", "Philippos", "Phinehas", "Phoenix", "Phoevos", "Pierce", "Pierre-Antoine", "Pieter", "Pietro", "Piotr", "Porter", "Prabhjoit", "Prabodhan", "Praise", "Pranav", "Pravin", "Precious", "Prentice", "Presley", "Preston", "Preston-Jay", "Prinay", "Prince", "Prithvi", "Promise", "Puneetpaul", "Pushkar", "Qasim", "Qirui", "Quinlan", "Quinn", "Radmiras", "Raees", "Raegan", "Rafael", "Rafal", "Rafferty", "Rafi", "Raheem", "Rahil", "Rahim", "Rahman", "Raith", "Raithin", "Raja", "Rajab-Ali", "Rajan", "Ralfs", "Ralph", "Ramanas", "Ramit", "Ramone", "Ramsay", "Ramsey", "Rana", "Ranolph", "Raphael", "Rasmus", "Rasul", "Raul", "Raunaq", "Ravin", "Ray", "Rayaan", "Rayan", "Rayane", "Rayden", "Rayhan", "Raymond", "Rayne", "Rayyan", "Raza", "Reace", "Reagan", "Reean", "Reece", "Reed", "Reegan", "Rees", "Reese", "Reeve", "Regan", "Regean", "Reggie", "Rehaan", "Rehan", "Reice", "Reid", "Reigan", "Reilly", "Reily", "Reis", "Reiss", "Remigiusz", "Remo", "Remy", "Ren", "Renars", "Reng", "Rennie", "Reno", "Reo", "Reuben", "Rexford", "Reynold", "Rhein", "Rheo", "Rhett", "Rheyden", "Rhian", "Rhoan", "Rholmark", "Rhoridh", "Rhuairidh", "Rhuan", "Rhuaridh", "Rhudi", "Rhy", "Rhyan", "Rhyley", "Rhyon", "Rhys", "Rhys-Bernard", "Rhyse", "Riach", "Rian", "Ricards", "Riccardo", "Ricco", "Rice", "Richard", "Richey", "Richie", "Ricky", "Rico", "Ridley", "Ridwan", "Rihab", "Rihan", "Rihards", "Rihonn", "Rikki", "Riley", "Rio", "Rioden", "Rishi", "Ritchie", "Rivan", "Riyadh", "Riyaj", "Roan", "Roark", "Roary", "Rob", "Robbi", "Robbie", "Robbie-lee", "Robby", "Robert", "Robert-Gordon", "Robertjohn", "Robi", "Robin", "Rocco", "Roddy", "Roderick", "Rodrigo", "Roen", "Rogan", "Roger", "Rohaan", "Rohan", "Rohin", "Rohit", "Rokas", "Roman", "Ronald", "Ronan", "Ronan-Benedict", "Ronin", "Ronnie", "Rooke", "Roray", "Rori", "Rorie", "Rory", "Roshan", "Ross", "Ross-Andrew", "Rossi", "Rowan", "Rowen", "Roy", "Ruadhan", "Ruaidhri", "Ruairi", "Ruairidh", "Ruan", "Ruaraidh", "Ruari", "Ruaridh", "Ruben", "Rubhan", "Rubin", "Rubyn", "Rudi", "Rudy", "Rufus", "Rui", "Ruo", "Rupert", "Ruslan", "Russel", "Russell", "Ryaan", "Ryan", "Ryan-Lee", "Ryden", "Ryder", "Ryese", "Ryhs", "Rylan", "Rylay", "Rylee", "Ryleigh", "Ryley", "Rylie", "Ryo", "Ryszard", "Saad", "Sabeen", "Sachkirat", "Saffi", "Saghun", "Sahaib", "Sahbian", "Sahil", "Saif", "Saifaddine", "Saim", "Sajid", "Sajjad", "Salahudin", "Salman", "Salter", "Salvador", "Sam", "Saman", "Samar", "Samarjit", "Samatar", "Sambrid", "Sameer", "Sami", "Samir", "Sami-Ullah", "Samual", "Samuel", "Samuela", "Samy", "Sanaullah", "Sandro", "Sandy", "Sanfur", "Sanjay", "Santiago", "Santino", "Satveer", "Saul", "Saunders", "Savin", "Sayad", "Sayeed", "Sayf", "Scot", "Scott", "Scott-Alexander", "Seaan", "Seamas", "Seamus", "Sean", "Seane", "Sean-James", "Sean-Paul", "Sean-Ray", "Seb", "Sebastian", "Sebastien", "Selasi", "Seonaidh", "Sephiroth", "Sergei", "Sergio", "Seth", "Sethu", "Seumas", "Shaarvin", "Shadow", "Shae", "Shahmir", "Shai", "Shane", "Shannon", "Sharland", "Sharoz", "Shaughn", "Shaun", "Shaunpaul", "Shaun-Paul", "Shaun-Thomas", "Shaurya", "Shaw", "Shawn", "Shawnpaul", "Shay", "Shayaan", "Shayan", "Shaye", "Shayne", "Shazil", "Shea", "Sheafan", "Sheigh", "Shenuk", "Sher", "Shergo", "Sheriff", "Sherwyn", "Shiloh", "Shiraz", "Shreeram", "Shreyas", "Shyam", "Siddhant", "Siddharth", "Sidharth", "Sidney", "Siergiej", "Silas", "Simon", "Sinai", "Skye", "Sofian", "Sohaib", "Sohail", "Soham", "Sohan", "Sol", "Solomon", "Sonneey", "Sonni", "Sonny", "Sorley", "Soul", "Spencer", "Spondon", "Stanislaw", "Stanley", "Stefan", "Stefano", "Stefin", "Stephen", "Stephenjunior", "Steve", "Steven", "Steven-lee", "Stevie", "Stewart", "Stewarty", "Strachan", "Struan", "Stuart", "Su", "Subhaan", "Sudais", "Suheyb", "Suilven", "Sukhi", "Sukhpal", "Sukhvir", "Sulayman", "Sullivan", "Sultan", "Sung", "Sunny", "Suraj", "Surien", "Sweyn", "Syed", "Sylvain", "Symon", "Szymon", "Tadd", "Taddy", "Tadhg", "Taegan", "Taegen", "Tai", "Tait", "Taiwo", "Talha", "Taliesin", "Talon", "Talorcan", "Tamar", "Tamiem", "Tammam", "Tanay", "Tane", "Tanner", "Tanvir", "Tanzeel", "Taonga", "Tarik", "Tariq-Jay", "Tate", "Taylan", "Taylar", "Tayler", "Taylor", "Taylor-Jay", "Taylor-Lee", "Tayo", "Tayyab", "Tayye", "Tayyib", "Teagan", "Tee", "Teejay", "Tee-jay", "Tegan", "Teighen", "Teiyib", "Te-Jay", "Temba", "Teo", "Teodor", "Teos", "Terry", "Teydren", "Theo", "Theodore", "Thiago", "Thierry", "Thom", "Thomas", "Thomas-Jay", "Thomson", "Thorben", "Thorfinn", "Thrinei", "Thumbiko", "Tiago", "Tian", "Tiarnan", "Tibet", "Tieran", "Tiernan", "Timothy", "Timucin", "Tiree", "Tisloh", "Titi", "Titus", "Tiylar", "TJ", "Tjay", "T-Jay", "Tobey", "Tobi", "Tobias", "Tobie", "Toby", "Todd", "Tokinaga", "Toluwalase", "Tom", "Tomas", "Tomasz", "Tommi-Lee", "Tommy", "Tomson", "Tony", "Torin", "Torquil", "Torran", "Torrin", "Torsten", "Trafford", "Trai", "Travis", "Tre", "Trent", "Trey", "Tristain", "Tristan", "Troy", "Tubagus", "Turki", "Turner", "Ty", "Ty-Alexander", "Tye", "Tyelor", "Tylar", "Tyler", "Tyler-James", "Tyler-Jay", "Tyllor", "Tylor", "Tymom", "Tymon", "Tymoteusz", "Tyra", "Tyree", "Tyrnan", "Tyronebreed", "Tyson", "Ubaid", "Ubayd", "Uchenna", "Uilleam", "Umair", "Umar", "Umer", "Umut", "Urban", "Uri", "Usman", "Uzair", "Uzayr", "Valen", "Valentin", "Valentino", "Valery", "Valo", "Vasyl", "Vedantsinh", "Veeran", "Victor", "Victory", "Vinay", "Vince", "Vincent", "Vincenzo", "Vinh", "Vinnie", "Vithujan", "Vladimir", "Vladislav", "Vrishin", "Vuyolwethu", "Wabuya", "Wai", "Walid", "Wallace", "Walter", "Waqaas", "Warkhas", "Warren", "Warrick", "Wasif", "Wayde", "Wayne", "Wei", "Wen", "Wesley", "Wesley-Scott", "Wiktor", "Wilkie", "Will", "William", "William-John", "Willum", "Wilson", "Windsor", "Wojciech", "Woyenbrakemi", "Wyatt", "Wylie", "Wynn", "Xabier", "Xander", "Xavier", "Xiao", "Xida", "Xin", "Xue", "Yadgor", "Yago", "Yahya", "Yakup", "Yang", "Yanick", "Yann", "Yannick", "Yaseen", "Ydef sellasin", "Yasir", "Yassin", "Yoji", "Yong", "Yoolgeun", "Yorgos", "Youcef", "Yousif", "Youssef", "Yu", "Yuanyu", "Yuri", "Yusef", "Yusuf", "Yves", "Zaaine", "Zaak", "Zac", "Zach", "Zachariah", "Zacharias", "Zacharie", "Zacharius", "Zachariya", "Zachary", "Zachary-Marc", "Zachery", "Zack", "Zackary", "Zaid", "Zain", "Zaine", "Zaineddine", "Zainedin", "Zak", "Zakaria", "Zakariya", "Zakary", "Zaki", "Zakir", "Zakk", "Zamaar", "Zander", "Zane", "Zarran", "Zayd", "Zayn", "Zayne", "Ze", "Zechariah", "Zeek", "Zeeshan", "Zeid", "Zein", "Zen", "Zendel", "Zenith", "Zennon", "Zeph", "Zerah", "Zhen", "Zhi", "Zhong", "Zhuo", "Zi", "Zidane", "Zijie", "Zinedine", "Zion", "Zishan", "Ziya", "Ziyaan", "Zohaib", "Zohair", "Zoubaeir", "Zubair", "Zubayr", "Zuriel"]
        namel=len(names)
        namepick=rand.randint(0,namel)
        npctrainer=names[namepick]
        await ctx.send(npcname)
        embed = discord.Embed(title="NPC Battle", description="Trainer "+npctrainer+" wants to battle!", color=0x00ff00)
        embed.set_image(url="http://157.245.8.88/html/dex/media/pokemon/sugimori/trainer.png")
        hpnpcstat=rand.randint(0,31)
        atknpcstat=rand.randint(0,31)
        defnpcstat=rand.randint(0,31)
        sp_atknpcstat=rand.randint(0,31)
        sp_defnpcstat=rand.randint(0,31)
        speednpcstat=rand.randint(0,31)
        p1=[]
        p1.append(hpnpcstat)
        p1.append(atknpcstat)
        p1.append(defnpcstat)
        p1.append(sp_atknpcstat)
        p1.append(sp_defnpcstat)
        p1.append(speednpcstat)
        await ctx.send(embed=embed)
        
        hpnpc=500
        hpplayer=500
        atkplayerstat=31
        while hpnpc>1 and hpplayer>1: 
            c.execute("Select identifier from Moves where power != 'null'")
            possiblemoves=c.fetchall()
            possiblemoves=str(possiblemoves)
            possiblemoves=possiblemoves.replace(")","")
            possiblemoves=possiblemoves.replace("(","")
            possiblemoves=possiblemoves.replace("]","")
            possiblemoves=possiblemoves.replace("[","")
            possiblemoves=possiblemoves.replace(",,",",")
            possiblemoves=possiblemoves.replace("'","")
            selectmove=possiblemoves.split(',')
            randmove=rand.randint(0,len(selectmove))
            level1=50
            advant1=1
            moveselected=selectmove[randmove]
            await ctx.send(f'Select a move {ctx.author.mention}!') 
            move = await self.bot.wait_for("message",timeout=300)
            while move.author.id != ctx.author.id and 'use' not in move.content:
                await ctx.send(f'Select a move {ctx.author.mention}!') 
                move = await self.bot.wait_for("message",timeout=300)
            movec=move.content
            playermove="move"+movec[-1:]
            c.execute(f"select selected from Players where ID={ctx.author.id}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            c.execute(f"select level from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
            playerlevel=c.fetchone()
            playerlevel=str(playerlevel)
            playerlevel=playerlevel[1:-2]
            c.execute(f"select {playermove} from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
            selectedmove=c.fetchone()
            selectedmove=str(selectedmove)
            selectedmove=selectedmove[2:-3]
            await ctx.send(f"{ctx.author.mention} used {selectedmove}")
            await ctx.send("NPC used "+moveselected)
            c.execute(f"select power from moves where identifier='{moveselected[1:]}'")
            npcpower=c.fetchone()
            npcpower=str(npcpower)
            
            npcpower=npcpower[2:-3]
            await ctx.send(npcpower)
            damagenpc=int(npcpower)*int(atknpcstat)
            damagenpc=int(damagenpc)/(rand.randint(2,50))
            hpnpc=hpnpc-int(damagenpc)
            c.execute(f"select power from moves where identifier='{selectedmove}'")
            playerpower=c.fetchone()
            playerpower=str(playerpower)
            playerpower=playerpower[2:-3]
            damageplayer=int(playerpower)*int(atkplayerstat)
            damageplayer=int(damageplayer)/int(playerlevel)
            hpplayer=hpplayer-int(damagenpc)
            hpnpc=hpnpc-int(damageplayer)
        if hpnpc<1:
            await ctx.send(f"{ctx.author.mention} wins and got 100 Blazibucks!")
            await bank.deposit_credits(ctx.author, 100)
        elif hpplayer<1:
            await ctx.send(f"NPC wins!")
       
    @commands.command(name='typeadv' , aliases=["ty"])
    async def typeadv(self, ctx,typeadv:str):
       conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')

       c = conn.cursor()
       c.execute(f"select attacking from typeadv")
       num=c.fetchone()
       num=str(num)
       number=num.split(',')
       tnum=len(number)
       current=1
       while current<17:
           c.execute(f"select * from typeadv where attacking='{typeadv.casefold().capitalize()}'")
           tadv=c.fetchall()
           tadv=str(tadv)
           t=tadv.split(',')
           c.execute(f"select attacking from typeadv")
           att=c.fetchall()
           att=str(att)
          
           
           
           att=att.replace("(","")
           att=att.replace(")","")
           att=att.replace(",","")
           at=att.split("' '")
           for o in t:
                await ctx.send(f"{str(current)}  |  {at[current]}  |  {str(t[current])}")
                current=current+1
           c.close() 
    @commands.command(name='dis' , aliases=["disable"])
    @checks.admin()
    async def dis(self, ctx,oldchannel:discord.TextChannel):
        conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        await ctx.send(f"Attempting to disable {str(oldchannel)}")
        old = oldchannel.id
        
        c.execute(f"select disabled from disables where disabled='{old}'")
        exists=c.fetchone()
        exists=str(exists)
        if 'None' in exists:
            c.execute(f"insert into disables(disabled) Values('{old}')")
            conn.commit()
            await ctx.send("You have successfully disabled this channel")
        else:
            await ctx.send("You have already disabled this channel!")
        c.close()  
    @commands.command(name='redirect' , aliases=["change spawn"])
    @checks.admin()
    async def redirect(self, ctx,oldchannel:discord.TextChannel, newchannel:discord.TextChannel):
        conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        await ctx.send(f"Attempting to redirect from {str(oldchannel)} to {str(newchannel)}")
        old = oldchannel.id
        new=newchannel.id
        
        c.execute(f"select redirect_channel from redirects where channel_id='{old}'")
        exists=c.fetchone()
        exists=str(exists)
        if 'None' in exists:
            c.execute(f"insert into redirects(server_id,channel_id,redirect_channel) Values(1,'{old}','{new}')")
            conn.commit()
            await ctx.send("You have successfully redirected")
        else:
            await ctx.send("You have already redirected from this channel!")
        c.close()  
    @commands.command(name='inv' , aliases=["invitebot"])
    async def inv(self, ctx):        
        await ctx.send("https://discordapp.com/oauth2/authorize?client_id=548295233138327583&scope=bot")
    @commands.command(name='movesets' , aliases=["ms"])
    async def movesets(self, ctx):
        author=ctx.author.id
        authorpic=ctx.author.avatar_url
        conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')

        c = conn.cursor()
        c.execute(f"select selected from Players where ID='{author}'")
        num=c.fetchone()
        num=str(num).strip(",").strip(")").strip("(")
        

        num=num[:-1]
        c.execute(f"select poke_id from Owned_Pokes where {num}=ID_Owned and Owner={author}")
        owned=c.fetchone()
        owned=str(owned)[1:-2]
        c.execute(f"select move_id from pokemoves where pokemon_id={int(owned)}")
        moves=c.fetchall()
        moves=str(moves).replace("(","").replace(")","").replace("[]","").replace("]","").replace("'","").replace(",,",",")
        move=[]
        count=0
        mo=moves.split(',')
        for m in mo:
            
            try:
                c.execute(f"select identifier from Moves where id={int(m)}")
                a=c.fetchone()
                a=str(a)
                a=a[2:-3]
                b=a
                if count==25:
                    count=0
                    v=str(b)+'.'
                    v=v+'#'
                    move.append(v)
                else:
                    count=count+1
                    b=b+'#'
                    move.append(str(b))
            except:
                print("error")
        ls=[]
        [ls.append(x) for x in move if x not in ls] 
        await menu(ctx, str(ls).replace(",","").replace("'","").replace("#",'\n').replace("','","").split('.'), DEFAULT_CONTROLS)
        
        c.close()
    
    @commands.command(name='learn' , aliases=["l"])
    async def learn(self, ctx,spot:str,movename:str):
        author=ctx.author.id
        authorpic=ctx.author.avatar_url
        conn=sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')

        c = conn.cursor()
        c.execute(f"select selected from Players where ID='{author}'")
        num=c.fetchone()
        num=str(num).strip(",").strip(")").strip("(")
        moveslot=""
        if spot=='1':
            moveslot='move1'
        elif spot=='2':
            moveslot='move2'
        elif spot=='3':
            moveslot='move3'
        elif spot=='4':
            moveslot='move4'
        num=num[:-1]
        c.execute(f"select poke_id from Owned_Pokes where {num}=ID_Owned and Owner={author}")
        owned=c.fetchone()
        owned=str(owned)[1:-2]
        c.execute(f"select move_id from pokemoves where pokemon_id={int(owned)}")
        moves=c.fetchall()
        moves=str(moves).replace("(","").replace(")","").replace("[]","").replace("]","").replace("'","").replace(",,",",")
        move=[]
        count=0
        mo=moves.split(',')
        for m in mo:
            
            try:
                c.execute(f"select identifier from Moves where id={int(m)}")
                a=c.fetchone()
                a=str(a)
                a=a[2:-3]
                b=a
                
                move.append(str(b))
            except:
                print("error")
        ls=[]
        [ls.append(x) for x in move if x not in ls] 
        if movename.casefold() in ls:
            await ctx.send(movename+" is being learnt!")
            c.execute(f"update Owned_Pokes set {moveslot.capitalize()}='{movename}' where Owner={author} and {num}=ID_Owned")
            conn.commit()
        else:
            await ctx.send("Your pokemon cannot learn "+movename)
        c.close()
    @commands.command(name='start' , aliases=["begin"])
    async def start (self, ctx):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
                
        author=ctx.author.id          
        c = conn.cursor()
        c.execute(f"SELECT ID from Players where ID='{author}';")
        exists=c.fetchone()
        exists=str(exists)
        if("None" not in exists):
            await ctx.send("You already have a starter!")
        else:
            await ctx.send('http://24.media.tumblr.com/76a62fc06cba1d98361add310f69a5de/tumblr_mxg5t6FckL1t2frpuo1_500.gif')
            await ctx.send('Hello there! \nWelcome to the world of Pokémon! My name is Oak! People call me the Pokémon Prof! \nThis world is inhabited by creatures called Pokémon! For some people, Pokémon are pets. Other use them for fights. \nMyself… I study Pokémon as a profession. \nFirst, what is your name?')
            name = await self.bot.wait_for("message",timeout=300)
            while name.author.id != author:   
                 name = await self.bot.wait_for("message",timeout=1000)   
            await ctx.send('Oak: Ah, I remember! Your name is '+name.content)
            await ctx.send(f'Oak: Which region are you travelling from {name.content}?') 
            region = await self.bot.wait_for("message",timeout=300)
            await ctx.send(f'Oak: Which region are you travelling from {name.content}?') 
            while region.author.id != author:
                 region = await self.bot.wait_for("message",timeout=1000)
            starters=[""]
            if region.content.casefold().capitalize()=="Kanto":
                starters=["Charmander","Squirtle","Bulbasaur"]
            elif region.content.casefold().capitalize()=="Johto":
                starters=["Cyndaquil","Totodile","chikorita"]
            elif region.content.casefold().capitalize()=="Hoenn":
                starters=["Torchic","Mudkip","Treecko"]
            elif region.content.casefold().capitalize()=="Sinnoh":
                starters=["Chimchar","Piplup","Turtwig"]
            elif region.content.casefold().capitalize()=="Unova":
                starters=["Tepig","Oshawott","Snivy"]
            elif region.content.casefold().capitalize()=="Kalos":
                starters=["Fennekin","Froakie","Chespin"]
            elif region.content.casefold().capitalize()=="Alola":
                starters=["Litten","Popplio","Rowlet"]
            else:
                await ctx.send("```Please pick a valid region!```")
            await ctx.send(f'Would you like {starters[0]}, {starters[1]}, or {starters[2]}')            
            starter = await self.bot.wait_for("message",timeout=1000)
            while starter.author.id != author:   
                starter = await self.bot.wait_for("message",timeout=1000)
            starter=starter.content.casefold().capitalize()
            await ctx.send(f'So, you want the {starter} (y/n)')        
            yesnostart= await self.bot.wait_for("message",timeout=10000)
            while yesnostart.author.id != author: 
                yesnostart= await self.bot.wait_for("message",timeout=10000)  
            if yesnostart.content.casefold().capitalize()=='Y' and starter in starters:
                await ctx.send(f'{starter} is a great Pokemon!')
            
                c.execute(f"INSERT INTO Players(ID , nick , poke1 , poke2 , poke3 , poke4 ,poke5 , poke6 , role, selected ) VALUES('{str(author)}','{name.content}',1,0,0,0, 0,0,'Initiate',1);")
                conn.commit()
                
            
                c.execute(f"Select Number from Pokes where Name='{starter}'")
                snum=c.fetchone()
                snum=str(snum)
                await ctx.send(str(snum))
                snum=snum[1:-2]

                await ctx.send(snum)
                await ctx.send(snum+"pokemon")
               
                hp=rand.randint(0,31)
                atk=rand.randint(0,31)
                df=rand.randint(0,31)
                sp_atk=rand.randint(0,31)
                sp_def=rand.randint(0,31)
                speed=rand.randint(0,31)
                
                c.execute(f"select nature from Natures")
                natures=c.fetchall()
                natures=str(natures)
                natures=natures.replace("(","")
                natures=natures.replace(")","")
                natures=natures.replace("[","")
                natures=natures.replace("]","")
                natures=natures.replace(",,",",")
                natures=natures.replace(" ","")
                naturesl=natures.split(',')
                lenn=len(naturesl)
                randnat=rand.randint(0,lenn-1)
                nature=naturesl[randnat]
                c.execute(f"select ability from abilities where poke like '%{snum}%'")
                abilities=c.fetchall()
                abilities=str(abilities)
                abilities=abilities.replace("(","")
                abilities=abilities.replace(")","")
                abilities=abilities.replace("[","")
                abilities=abilities.replace("]","")
                abilities=abilities.replace("'","")
                abilities=abilities.replace(",,",",")
                alist=abilities.split(',')
                alen=len(alist)
                arand=rand.randint(0,alen-1)
                ability=alist[arand]
                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,item,Nature,Natures,Ability ) VALUES(1,{snum},5,1,{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{author},0,'','','','','None',{nature},'None','{ability}');");
                conn.commit()
                c.close()
                await ctx.send("Congratulations on your first pokemon!")
            elif yesnostart.content.casefold().capitalize()=='N':
                 await ctx.send(f'Would you like {starters[0]}, {starters[1]}, or   {starters[2]}')
                 starter = await self.bot.wait_for("message",timeout=10000)
                 await ctx.send(f'So, you want the {starter.content} (y/n)')
                 yesnostart= await self.bot.wait_for("message",timeout=10000)
                    
            else:
                 await ctx.send('Try again!')
            c.close()
    @commands.command(name='unequip' , aliases=["ue"])
    async def unequip(self, ctx, item:str):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        if "Motor" in item:
            c.execute(f"select number from items where name='{item}' and Owner={ctx.author.id}")
            num=c.fetchone()
            num=str(num)
        
            if "None" in num:
                c.execute(f"insert into items(Owner,name,number) Values({ctx.author.id},'{item}',1);")
                conn.commit()
            else:
                num=num[1:-2]
                num=int(num)
                c.execute(f"update items set number={num+1} where name='{item}' and Owner={ctx.author.id}")
                conn.commit()
                c.execute(f"update Players set Equipped='None' where ID={ctx.author.id}")
                conn.commit()
            await ctx.send(f"You unequipped 1 {item}")
            
        elif "mega" in item:
            c.execute(f"select number from items where name='{item}' and Owner={ctx.author.id}")
            num=c.fetchone()
            num=str(num)
        
            if "None" in num:
                c.execute(f"insert into items(Owner,name,number) Values({ctx.author.id},'{item}',1);")
                conn.commit()
            else:
                num=num[1:-2]
                num=int(num)
                c.execute(f"update items set number={num+1} where name='{item}' and Owner={ctx.author.id}")
                conn.commit()
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                poke=poke
                await ctx.send(poke)
                c.execute(f"update Owned_Pokes set item='None' where Number_Caught={select} and Owner={ctx.author.id}")
                
                conn.commit()
            c.execute(f"select selected from Players where ID={ctx.author.id}")
            selected=c.fetchone()
            selected = str(selected)
            selected=selected[1:-2]
            select=int(selected)
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
            poke=c.fetchone()
            poke=str(poke)
            poke=poke[1:-5]
            await ctx.send(poke)
            c.execute(f"update Owned_Pokes set poke_id={poke} where Number_Caught={selected} and Owner={ctx.author.id}")
            conn.commit()
            await ctx.send(f"You unequipped 1 {item} and your Pokemon deformed!")
        c.close()
    @commands.command(name='equip' , aliases=["e"])
    async def equip(self, ctx, item:str):
        await ctx.send("You can equip items to your pokemon this way!") 
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select name from items where owner={ctx.author.id}")
        itemslist=c.fetchall()
        itemslist=str(itemslist)
        itemslist=itemslist[2:-3]
        c.execute(f"select selected from Players where ID={ctx.author.id}")
        selected=c.fetchone()
        selected = str(selected)
        selected=selected[1:-2]
        select=int(selected)
        c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
        poke=c.fetchone()
        poke=str(poke)
        poke=poke[1:-2]
        haveitem=False
        c.execute(f"select Name from Pokes where Number={poke}")
        name=c.fetchone()
        name=str(name)     
        if item in itemslist and 'Mega-' not in name :
            await ctx.send(item)
            await ctx.send(f"You are trying to equip a {item}")
            haveitem= True
            c.execute(f"select number from items where Owner={ctx.author.id} and name='{item}'")
            num=c.fetchone()
            num=str(num)
            num=num[1:-2]
            await ctx.send(num)
            nu=int(num)
            c.execute(f"update items set number={nu-1} where name='{item}' and Owner={ctx.author.id}")
            conn.commit()
            if nu-1<1:
                c.execute(f"delete from items where Owner={ctx.author.id} and number={nu-1} and name='{item}'")
                conn.commit()
            if('mega-stone' in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                c.execute(f"select level from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                level=c.fetchone()
                level=str(level)
                level=level[1:-2]
                level=int(level)
                await ctx.send(level)
                if level>4:
                    c.execute(f"update Owned_Pokes set item='mega-stone' where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    
                else:
                    await ctx.send("You cant mega an egg!")    
            elif("tm" in item or "Tm" in item or "TM" in item):
                await ctx.send("Which move would you like for it to learn?")
                move = await self.bot.wait_for("message",timeout=1000)  
                while move.author.id != ctx.author.id:
                   await ctx.send("Which move would you like for it to learn?")
                   move= await self.bot.wait_for("message",timeout=1000)
                if move.author.id == ctx.author.id:
                    await ctx.send("Which move slot?")
                    slot = await self.bot.wait_for("message",timeout=1000)
                    while slot.author.id != ctx.author.id:
                       await ctx.send("Which move slot?")
                       slot = await self.bot.wait_for("message",timeout=1000) 
                    
                    learnslot="" 
                    await ctx.send(slot.content)                       
                    if "1" in slot.content:
                       learnslot="move1"
                    elif "2" in slot.content:
                       learnslot="move2"
                    elif "3" in slot.content:
                       learnslot="move3"
                    elif "4" in slot.content:
                       learnslot="move4"
                    await ctx.send(learnslot)
                    c.execute(f"select selected from Players where ID={ctx.author.id}")
                    select=c.fetchone()
                    select=str(select)
                    select=select[1:-2]
                    await ctx.send(select)
                    c.execute(f"update Owned_Pokes set {learnslot}='{move.content}' where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send(f"You Pokemon has learnt {move.content}!")
            elif('Destiny' in item or "destiny" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                c.execute(f"update Owned_Pokes set item='Destiny-knot' where Number_Caught={select} and Owner={ctx.author.id}")
                conn.commit()
            elif('Gender' in item or "gender" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                c.execute(f"select gender from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                gender=c.fetchone()
                newgender=""
                gender=str(gender)
                if 'Fe' in gender:
                    newgender="Male"
                elif "Male" in gender:
                    newgender="Female"
                else:
                    randgender=rand.randint(0,1)
                    if randgender==0:
                        newgender="Male"
                    else:
                        newgender="Female"
                c.execute(f"update Owned_Pokes set gender='{newgender}' where Number_Caught={select} and Owner={ctx.author.id}")
                conn.commit()      
            elif('everstone' in item or "Everstone" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                c.execute(f"update Owned_Pokes set item='Everstone' where Number_Caught={select} and Owner={ctx.author.id}")
                conn.commit()         
            elif('alolan' in item or "Alolan" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                c.execute(f"update Owned_Pokes set item='alolan-stone' where Number_Caught={select} and Owner={ctx.author.id}")
                conn.commit()
            elif('hp-up' in item or "Hp-up" in item):
                itemmsg=ctx.message
                itemmsg=str(itemmsg.content)
                itemmsg=itemmsg.replace("-equip ","")
                itemmsg=itemmsg.replace(" ",",")
                options=itemmsg.split(',')
                options.append('-')
                if "-" in options[2]:
                    count=1
                else:
                    count=int(options[2])
                    await ctx.send(str(count))
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select Ev1,Ev2,Ev3,Ev4,Ev5,Ev6 from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                evs=c.fetchall()
                evs=str(evs)
                evs=evs.replace("(","")
                evs=evs.replace(")","")
                evs=evs.replace("[","")
                evs=evs.replace("]","")
                evs=evs.replace(",,",",")
                totalevs=evs.split(',')
                if int(totalevs[0])+int(totalevs[1])+int(totalevs[2])+int(totalevs[3])+int(totalevs[4])+int(totalevs[5])>=500:
                    await ctx.send("you have reached your max evs for this pokemon")
                elif int(totalevs[0])>=245 or (int(totalevs[0])+count)> 252:
                    await ctx.send("you cannot raise this ev any higher")
                else:
                    newev=int(totalevs[0])+(10*count)
                    c.execute(f"update Owned_Pokes set Ev1={newev} where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send("you have added evs to your pokemon's health") 
            elif('protein' in item or "Protein" in item):
                
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select Ev1,Ev2,Ev3,Ev4,Ev5,Ev6 from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                evs=c.fetchall()
                evs=str(evs)
                evs=evs.replace("(","")
                evs=evs.replace(")","")
                evs=evs.replace("[","")
                evs=evs.replace("]","")
                evs=evs.replace(",,",",")
                totalevs=evs.split(',')
                if int(totalevs[0])+int(totalevs[1])+int(totalevs[2])+int(totalevs[3])+int(totalevs[4])+int(totalevs[5])>=500:
                    await ctx.send("you have reached your max evs for this pokemon")
                elif int(totalevs[1])>=245:
                    await ctx.send("you cannot raise this ev any higher")
                else:
                    newev=int(totalevs[1])+10
                    c.execute(f"update Owned_Pokes set Ev2={newev} where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send("you have added evs to your pokemon's attack")
            elif('iron' in item or "Iron" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select Ev1,Ev2,Ev3,Ev4,Ev5,Ev6 from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                evs=c.fetchall()
                evs=str(evs)
                evs=evs.replace("(","")
                evs=evs.replace(")","")
                evs=evs.replace("[","")
                evs=evs.replace("]","")
                evs=evs.replace(",,",",")
                totalevs=evs.split(',')
                if int(totalevs[0])+int(totalevs[1])+int(totalevs[2])+int(totalevs[3])+int(totalevs[4])+int(totalevs[5])>=500:
                    await ctx.send("you have reached your max evs for this pokemon")
                elif int(totalevs[2])>=245:
                    await ctx.send("you cannot raise this ev any higher")
                else:
                    newev=int(totalevs[2])+10
                    c.execute(f"update Owned_Pokes set Ev3={newev} where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send("you have added evs to your pokemon's defense")   
            elif('calcium' in item or "Calcium" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select Ev1,Ev2,Ev3,Ev4,Ev5,Ev6 from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                evs=c.fetchall()
                evs=str(evs)
                evs=evs.replace("(","")
                evs=evs.replace(")","")
                evs=evs.replace("[","")
                evs=evs.replace("]","")
                evs=evs.replace(",,",",")
                totalevs=evs.split(',')
                if int(totalevs[0])+int(totalevs[1])+int(totalevs[2])+int(totalevs[3])+int(totalevs[4])+int(totalevs[5])>=500:
                    await ctx.send("you have reached your max evs for this pokemon")
                elif int(totalevs[3])>=245:
                    await ctx.send("you cannot raise this ev any higher")
                else:
                    newev=int(totalevs[3])+10
                    c.execute(f"update Owned_Pokes set ev4={newev} where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send("you have added evs to your pokemon's Special Attack")              
            elif('Zinc' in item or "zinc" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select ev1,ev2,ev3,ev4,ev5,ev6 from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                evs=c.fetchall()
                evs=str(evs)
                evs=evs.replace("(","")
                evs=evs.replace(")","")
                evs=evs.replace("[","")
                evs=evs.replace("]","")
                evs=evs.replace(",,",",")
                totalevs=evs.split(',')
                if int(totalevs[0])+int(totalevs[1])+int(totalevs[2])+int(totalevs[3])+int(totalevs[4])+int(totalevs[5])>=500:
                    await ctx.send("you have reached your max evs for this pokemon")
                elif int(totalevs[4])>=245:
                    await ctx.send("you cannot raise this ev any higher")
                else:
                    newev=int(totalevs[4])+10
                    c.execute(f"update Owned_Pokes set ev5={newev} where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send("you have added evs to your pokemon's special defense")
            elif('Ev-reset' in item or "ev-reset" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"update Owned_Pokes set Ev1=0,Ev2=0,Ev3=0,Ev4=0,Ev5=0,Ev6=0 where Number_Caught={select} and Owner={ctx.author.id}")
                conn.commit()            
            elif('Carbos' in item or "carbos" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected),
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select ev1,ev2,ev3,ev4,ev5,ev6 from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                evs=c.fetchall()
                evs=str(evs)
                evs=evs.replace("(","")
                evs=evs.replace(")","")
                evs=evs.replace("[","")
                evs=evs.replace("]","")
                evs=evs.replace(",,",",")
                totalevs=evs.split(',')
                if int(totalevs[0])+int(totalevs[1])+int(totalevs[2])+int(totalevs[3])+int(totalevs[4])+int(totalevs[5])>=500:
                    await ctx.send("you have reached your max evs for this pokemon")
                elif int(totalevs[5])>=245:
                    await ctx.send("you cannot raise this ev any higher")
                else:
                    newev=int(totalevs[5])+10
                    c.execute(f"update Owned_Pokes set ev6={newev} where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send("you have added evs to your pokemon's Speed")
            elif('Ability' in item or 'ability' in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                poke=poke[1:-2]
                c.execute(f"select ability from abilities where poke like '%{poke}%'")
                abilitylist=c.fetchall()
                abilitylist=str(abilitylist)
                await ctx.send(abilitylist)
                abilitylist=abilitylist.replace(")","")
                abilitylist=abilitylist.replace("(","")
                abilitylist=abilitylist.replace("]","")
                abilitylist=abilitylist.replace("[","")
                abilitylist=abilitylist.replace("'","")
                abilitylist=abilitylist.replace(",,",",")
                abilities=abilitylist.split(',')
                abilitylen=len(abilities)
                randabil=rand.randint(0,abilitylen-1)
                ability=abilities[randabil]
                
                c.execute(f"select ability from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                if ability in poke:
                       randabil=rand.randint(0,abilitylen-1)
                       ability=abilities[randabil]
                
                c.execute(f"update Owned_Pokes set ability='{ability}' where Number_Caught={select} and Owner={ctx.author.id}")
                conn.commit()
                await ctx.send(f" You have changed your pokemons ability to {ability}")
            elif('Nature' in item or "nature" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select Nature from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                await ctx.send(f"Your pokemon's nature is {poke}, what would you like to change it to?")
                nat = await self.bot.wait_for("message",timeout=1000)  
                while nat.author.id != ctx.author.id:
                   await ctx.send("Your pokemon's nature is {poke}, what would you like to change it to?")
                   nat= await self.bot.wait_for("message",timeout=1000)
                c.execute(f"select nature from Natures")
                naturelist=c.fetchall()
                naturelist=str(naturelist)
                if nat.content in naturelist:
                    c.execute(f"update Owned_Pokes set Nature='{nat.content}' where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send(f"You have changed your pokemon's nature to {nat.content}")
                else:
                    await ctx.send("That is not a valid nature")
            elif("Motorcycle" in item):
                c.execute(f"update Players set Equipped='Motorcycle' where ID={ctx.author.id}")
                conn.commit()
                await ctx.send("You have equipped a motorcycle!") 
            elif("Trade-evolver" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                poke=poke[1:-2]
                await ctx.send(poke)
                c.execute(f"Select newpokemon from tradeevos where oldpokemon={poke}")
                newpoke=c.fetchone()
                newpoke=str(newpoke)
                newpoke=newpoke[1:-2]
                if 'o' in newpoke:
                    await ctx.send("This pokemon has no trade evolution!")
                else:
                    c.execute(f"update Owned_Pokes set poke_id={newpoke} where Owner={ctx.author.id} and Number_Caught={select}")
                    conn.commit()
                    await ctx.send("Your pokemon evolved!")        
            elif("Bike" in item):
                c.execute(f"update Players set Equipped='Bike' where ID={ctx.author.id}")
                conn.commit()
                await ctx.send("You have equipped a Bike!")            
            elif("Rare-candy" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                await ctx.send(poke)
                c.execute(f"select level from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                level=c.fetchone()
                level=str(level)
                level=level[1:-2]
                await ctx.send(level)
                lv=int(level)
                
                if lv<100 and lv>4:
                    lv=lv+1
                    c.execute(f"update Owned_Pokes set level={lv} where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send(f"Your pokemon has leveled to {str(lv)} with a Rare Candy!")
                else:
                    await ctx.send("Your pokemon cant level up anymore or is an egg!")
            elif("Mega-candy" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                await ctx.send(poke)
                c.execute(f"select level from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                level=c.fetchone()
                level=str(level)
                level=level[1:-2]
                await ctx.send(level)
                lv=int(level)
                
                if lv<91 and lv>4:
                    lv=lv+10
                    c.execute(f"update Owned_Pokes set level={lv} where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send(f"Your pokemon has leveled to {str(lv)} with a Rare Candy!")
                else:
                    await ctx.send("Your pokemon is too high of a level to use a Mega-candy or it is an egg!")
            elif("Ultra-candy" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                await ctx.send(poke)
                c.execute(f"select level from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                level=c.fetchone()
                level=str(level)
                level=level[1:-2]
                lv=int(level)
                
                if lv>4:
                    lv=100
                    c.execute(f"update Owned_Pokes set level={lv} where Number_Caught={select} and Owner={ctx.author.id}")
                    conn.commit()
                    await ctx.send(f"Your pokemon has leveled to {str(lv)} with a Rare Candy!")
                else:
                    await ctx.send("Your pokemon is too high of a level to use a Mega-candy or it is an egg!")
            elif("Lucky-egg" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                await ctx.send(poke)
                c.execute(f"update Owned_Pokes set item='{item}' where Number_Caught={select} and Owner={ctx.author.id}")
                conn.commit()
                
            elif("Life-orb" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                c.execute(f"update Owned_Pokes set item='{item}' where Number_Caught={select} and Owner={ctx.author.id}")
                conn.commit()
                await ctx.send(poke)
                
            elif("Thick-staff" in item):
                c.execute(f"select selected from Players where ID={ctx.author.id}")
                selected=c.fetchone()
                selected = str(selected)
                selected=selected[1:-2]
                select=int(selected)
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={select} and Owner={ctx.author.id}")
                poke=c.fetchone()
                poke=str(poke)
                await ctx.send(poke)
                c.execute(f"update Owned_Pokes set item='{item}' where Number_Caught={select} and Owner={ctx.author.id}")
                conn.commit()
                                        
                     
        if("Mega-" in name):
            await ctx.send("You cannot equip items to a mega pokemon!")        
        if(haveitem == False):
            await ctx.send(f"You do not have any {item}'s")
        c.close()     
    @commands.command(name='donate' , aliases=["d"])
    async def donate(self, ctx):
        await ctx.send("https://ko-fi.com/S6S6QTB5")
    @commands.command(name='redeem' , aliases=["r"])   
    @commands.cooldown(1, 180,commands.BucketType.user)
    async def redeem(self, ctx, redeemable:str):
        author=ctx.author.id
        a=ctx.author
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select redeems from Players where ID={author}")
        deemamt=c.fetchone()
        deemamt=str(deemamt)
        deemamt=deemamt[1:-2]
        await ctx.send(deemamt)
        deemamt=int(str(deemamt))
        
        if redeemable.casefold().capitalize()=='Credits' and deemamt>0:
            try:
                await bank.deposit_credits(a, 4000)
                await ctx.send("you have redeemed 4000 BlazeBucks!")
                deems=int(deemamt)-1
                await ctx.send(str(deems))
                c.execute(f"update Players set redeems={int(deems)} where ID={author}")
                conn.commit()
            except ValueError:
                await ctx.send('You could not redeem')
                return False
            else:
                return True
            await ctx.send("you have redeemed 4000 credits!")
            deems=int(deemamt)-1
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            c = conn.cursor()
            c.execute(f"update Players set redeems={int(deems)} where ID={author}")
            conn.commit()
        elif 'i' == redeemable.casefold():
            it=ctx.message
            item=it.content
            item=str(item)
            item=item.replace("-redeem i ","")
            await ctx.send(item)
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            c = conn.cursor()
            c.execute(f"select name from shop")
            itemlist=c.fetchall()
            itemlist=str(itemlist)
            itemlist=itemlist.replace("(","")
            itemlist=itemlist.replace(")","")
            itemlist=itemlist.replace("[","")
            itemlist=itemlist.replace("]","")
            itemlist=itemlist.replace(",,",",")
            itemlist=itemlist.replace("'","")
            
                
            if item in itemlist or 'Ultra-candy' in item:
                selecteditem=item.casefold()
                c.execute(f"select number from Pokes where Name='{str(redeemable)}'")
                deemedpoke=c.fetchone()
                deemedpoke=str(deemedpoke)
                deemedpoke=deemedpoke[1:-2]
                c.execute(f"select redeems from Players where ID='{author}'")
                deemamt=c.fetchone()
                deemamt=str(deemamt)
                deemamt=deemamt[1:-2]
                if 'Ultra-candy' in item:
                    deems=int(deemamt)-3
                else:     
                    deems=int(deemamt)-1 
                c.execute(f"update Players set redeems={int(deems)} where ID={author}")
                conn.commit()
                c.execute(f"select number from items where name='{item}' and Owner={ctx.author.id}")
                num=c.fetchone()
                num=str(num)
        
                if "None" in num:
                    c.execute(f"insert into items(Owner,name,number) Values({ctx.author.id},'{item}',1);")
                    conn.commit()
                else:
                    num=num[1:-2]
                    num=int(num)
                    c.execute(f"update items set number={num+1} where name='{item}' and Owner={ctx.author.id}")
                    conn.commit()
                await ctx.send(f"You redeemed an "+item)
                c.close()
            else:
                await ctx.send("That item does not exist")
                
                
        else:
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            c = conn.cursor()
            c.execute(f"select number from Pokes where Name='{str(redeemable)}'")
            deemedpoke=c.fetchone()
            deemedpoke=str(deemedpoke)
            deemedpoke=deemedpoke[1:-2]
            c.execute(f"select redeems from Players where ID='{author}'")
            deemamt=c.fetchone()
            deemamt=str(deemamt)
            deemamt=deemamt[1:-2]
            await ctx.send(f" You are trying to redeem a {deemedpoke}")
            
            if deemedpoke.isdigit()== False or '101010' in deemedpoke:
                await ctx.send("That pokemon doesn't exist!")
            elif deemamt<='0':
                await ctx.send(str(deemamt))
                await ctx.send("You dont have any redeems!")
            elif "Mega-" in redeemable:
                await ctx.send("You cannot redeem a mega!")    
            else:
                
                conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
                c = conn.cursor()
                level=5
                hp=rand.randint(0,31)
                atk=rand.randint(0,31)
                df=rand.randint(0,31)
                sp_atk=rand.randint(0,31)
                sp_def=rand.randint(0,31)
                speed=rand.randint(0,31)
                c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE Owner={author}")
                numberofpokes=c.fetchall()
                noofpokes=len(numberofpokes)
                newnumberofpokes=noofpokes+1
                itemdrop='None'
                shinyrand=rand.randint(0,1000)
                genderrand=rand.randint(0,1)
                if shinyrand==0:
                    shiny='True'
                else:
                    shiny='False'
                if genderrand==0:
                    gender='Male'
                else:
                    gender='Female'
                c.execute(f"select nature from natures")
                allnatures=c.fetchall()
                allnatures=str(allnatures)
                allnatures=allnatures.replace("[","")
                allnatures=allnatures.replace("]","")
                allnatures=allnatures.replace("(","")
                allnatures=allnatures.replace(")","")
                allnatures=allnatures.replace(",,",",")
                naturelist=allnatures.split(',')
                natlen=len(naturelist)
                randnat=rand.randint(0,natlen-1)
                nature=naturelist[randnat]
                nature=nature.replace("'","")
                c.execute(f"select ability from abilities where poke like '%{deemedpoke}%'")
                abilitylist=c.fetchall()
                abilitylist=str(abilitylist)
                await ctx.send(abilitylist)
                abilitylist=abilitylist.replace(")","")
                abilitylist=abilitylist.replace("(","")
                abilitylist=abilitylist.replace("]","")
                abilitylist=abilitylist.replace("[","")
                abilitylist=abilitylist.replace("'","")
                abilitylist=abilitylist.replace(",,",",")
                abilities=abilitylist.split(',')
                abilitylen=len(abilities)
                randabil=rand.randint(0,abilitylen-1)
                ability=abilities[randabil]
                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,gender,item,Nature,Natures,shiny,ability  ) VALUES({newnumberofpokes},{deemedpoke},{level},{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{author},0,'','','','','{gender}','{itemdrop}','{nature}','None','{shiny}','{ability}');")
                conn.commit()
                deems=int(deemamt)-1 
                await ctx.send(str(deems))
                c.execute(f"update Players set redeems={int(deems)} where ID={author}")
                conn.commit()
                c.close()
                
    @commands.command(name='deem' , aliases=["dmp"])
    @checks.is_owner()
    async def deem(self,ctx,person:discord.Member,amt:int,creds:int):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select redeems from Players where ID={person.id}")
        deems1=c.fetchone()
        deems1=str(deems1)
        deems1=deems1[1:-2]
        if 'o' in deems1:
            c.execute(f"update Players set redeems={amt} where ID={person.id}")
            conn.commit()
            await bank.deposit_credits(person, creds)
        else:
            deems=int(deems1)+amt
            c.execute(f"update Players set redeems={deems} where ID={person.id}")
            conn.commit()
            await bank.deposit_credits(person, creds)
        c.close()
    
    @commands.command(name='kenseionly' , aliases=["ko"])
    @checks.is_owner()
    async def kenseionly(self, ctx, poke,player:discord.Member,hp,atk,df,sp_atk,sp_df,speed,shiny:str):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        
        pokenum=poke
        if 'T' in shiny:
            pokenum=poke+'-shiny'
        
        c.execute(f"Select Name from pokes where Number={poke}")
        spawnpokes=c.fetchone()
        spawnpokes=str(spawnpokes)
        spawnpokes[4:-2]
        spawnedpoke=spawnpokes
        spawnedpoke=spawnedpoke[2:-3]    
        await ctx.send(spawnedpoke)
        await ctx.send(f"http://157.245.8.88/html/dex/media/pokemon/sugimori/{pokenum}.png")
        
       
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={player.id}")
                       
        numberofpokes=c.fetchall()
        c.close()
        noofpokes=len(numberofpokes)
        newnumberofpokes=noofpokes+1
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
              
        await ctx.send('Did you catch it?')
        c = conn.cursor()
        c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny  ) VALUES({newnumberofpokes},{poke},5,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_df},{speed},0,0,0,0,0,0,0,{player.id},'0','','','','','{shiny}');");
        conn.commit()
        await ctx.send('waiting..')
        c.close()
        await ctx.send("You caught it!")
    @commands.command(name='buy' , aliases=["b"])
    async def buy(self, ctx, item):   
        buychoice=ctx.message
        buychoice=str(buychoice.content)
        buychoice=buychoice.replace("-buy ","")
        buychoice=buychoice.replace(" ",",")
        options=buychoice.split(',')
        options.append('-')
        if "m" in options[0]or "market" in options[0] or "M" in options[0] or "Market" in options[0]:
            await ctx.send("You can buy pokemon from the market this way!")
        elif "i" in options[0]or "item" in options[0] or "I" in options[0] or "Items" in options[0]:
            item=options[1]
            if options[2]=='-':
                numi=1
            else:
                numi=int(options[2])
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            c = conn.cursor()
            c.execute(f"select cost from shop where name='{item.capitalize()}'")
            costs=c.fetchone()
            costs=str(costs)
            costs=costs.replace("(","")
            costs=costs.replace(")","")
            costs=costs.replace("'","")
            costs=costs.replace(",","")
            await bank.withdraw_credits(ctx.author, int(costs)*numi)
            c.execute(f"select number from items where name='{item}' and Owner={ctx.author.id}")
            num=c.fetchone()
            num=str(num)
        
            if "None" in num:
                c.execute(f"insert into items(Owner,name,number) Values({ctx.author.id},'{item}',{numi});")
                conn.commit()
            else:
                num=num[1:-2]
                num=int(num)
                c.execute(f"update items set number={num+int(numi)} where name='{item}' and Owner={ctx.author.id}")
                conn.commit()
            await ctx.send(f"You bought {numi} "+item)
            c.close()
        
            
    @commands.command(name='about' , aliases=["a"])
    async def about(self, ctx, num):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()   
        if(0==0):
            nu=num
            if nu.isdigit()==True:
                c.execute(f"select Number,Name,Type,HP,Attack,Defense,Sp_Atk,Sp_Def,Speed from Pokes where Number={nu}")
                info=c.fetchall()
                
                
            else:
                c.execute(f"select Number,Name,Type,HP,Attack,Defense,Sp_Atk,Sp_Def,Speed from Pokes where Name='{nu.capitalize()}'")
                info=c.fetchall()
            
            info=str(info)
            info=info.replace(")","").replace("(","").replace("]","").replace("[","").replace("'","").replace(",,",",")
            infos=info.split(',')
            embed = discord.Embed(title=f"About {infos[1]}")
            current=0
            titles=["Number","Name","Type","HP","Attack","Defense","Sp_Atk","Sp_Def","Speed"]
            for i in infos:
                embed.add_field(name=titles[current] , value=i, inline=True)
                current=current+1
            if 'shiny' not in ctx.message.content:
                img=infos[0]
            else:
                img=infos[0]+'-shiny'
            embed.set_image(url=f"http://157.245.8.88/html/dex/media/pokemon/sugimori/{img}.png")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)

            
        else:
            await ctx.send("Please try again")
    @commands.command(name='information' , aliases=["i"])
    async def information(self, ctx, num):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()    
        if "n" in num or "new" in num or "latest" in num:
            c.execute(f"select Number_Caught from Owned_pokes where Owner={ctx.author.id}")
            numofpokes=c.fetchall()
            numofpokes=str(numofpokes)
            numofpokes=numofpokes.replace("(","")
            numofpokes=numofpokes.replace(")","")
            numofpokes=numofpokes.replace("]","")
            numofpokes=numofpokes.replace("[","")
            numofpokes=numofpokes.replace(",,",",")
            pokelist=numofpokes.split(',')
            pokelen=len(pokelist)
            pokecaught=pokelen-1
            
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={pokecaught} and Owner={ctx.author.id}")
            pokenum=c.fetchone()
            pokenum=str(pokenum)
            pokenum=pokenum[1:-2]
            
            poke=int(pokenum)
        elif "s" in num or "selected" in num:
            c.execute(f"select selected from Players where ID={ctx.author.id}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            pokecaught=int(selected)
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={pokecaught} and Owner={ctx.author.id}")
            pokenum=c.fetchone()
            pokenum=str(pokenum)
            
            pokenum=pokenum[1:-2]
            poke=int(pokenum)
        else:
            pokecaught=num
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={pokecaught} and Owner={ctx.author.id}")
            pokeid=c.fetchone()
            pokeid=str(pokeid)
            pokeid=pokeid[1:-2]
            poke=int(pokeid)
        c.execute(f"select Name from Pokes where Number={poke}")
        name=c.fetchone()
        name=str(name)
        name=name[2:-3]
        c.execute(f"select HP,Attack,Defense,Sp_Atk,Sp_Def,Speed from Pokes where Name='{name}'")
        base=c.fetchall()
        base=str(base)
        base=base.replace("(","")
        base=base.replace(")","")
        base=base.replace("[","")
        base=base.replace("]","")
        base=base.replace(",,",",")
        bases=base.split(',')
        c.execute(f"select hp,atk,def,sp_atk,sp_def,speed,level,Ev1,Ev2,Ev3,Ev4,Ev5,Ev6,Gender,item,Nature,Shiny,EXP,ability,nick from Owned_Pokes where Number_Caught={pokecaught} and Owner={ctx.author.id}")
        pinfo=c.fetchall()
        pinfo=str(pinfo)
        pinfo=pinfo.replace("(","")
        pinfo=pinfo.replace(")","")
        pinfo=pinfo.replace("[","")
        pinfo=pinfo.replace("]","")
        pinfo=pinfo.replace(",,",",")
        pi=pinfo.split(',')
        hpiv=pi[0]
        atkiv=pi[1]
        defiv=pi[2]
        sp_atkiv=pi[3]
        sp_defiv=pi[4]
        speediv=pi[5]
        level=pi[6]
        hpev=pi[7]
        atkev=pi[8]
        defev=pi[9]
        sp_atkev=pi[10]
        sp_defev=pi[11]
        speedev=pi[12]
        gender=pi[13]
        item=pi[14]
        nature=pi[15]
        shiny=pi[16]
        exp=pi[17]
        ability=pi[18]
        nick=pi[19]
        total=(int(hpiv)+int(atkiv)+int(defiv)+int(sp_atkiv)+int(sp_defiv)+int(speediv))
        total=total*(0.537)
        total=round(total)
        hppower=(int(bases[0])+int(hpiv))*1.701+(int(hpev)/4)
        hppower=hppower*int(level)
        hppower=hppower/100
        hppower=hppower+int(level)+10
        atkpower=(int(bases[1])+int(atkiv))*1.771+(math.sqrt(int(atkev))/4)
        atkpower=atkpower*int(level)
        atkpower=atkpower/100
        atkpower=atkpower+5
        sp_atkpower=(int(bases[3])+int(sp_atkiv))*1.78+(math.sqrt(int(sp_atkev))/4)
        sp_atkpower=sp_atkpower*int(level)
        sp_atkpower=sp_atkpower/100
        sp_atkpower=sp_atkpower+5
        defpower=(int(bases[2])+int(defiv))*1.7755+(math.sqrt(int(defev))/4)
        defpower=defpower*int(level)
        defpower=defpower/100
        defpower=defpower+5
        sp_defpower=(int(bases[4])+int(sp_defiv))*1.835+(math.sqrt(int(sp_defev))/4)
        sp_defpower=sp_defpower*int(level)
        sp_defpower=sp_defpower/100
        sp_defpower=sp_defpower+5
        speedpower=(int(bases[5])+int(speediv))*1.8145+(math.sqrt(int(speedev))/4)
        speedpower=speedpower*int(level)
        speedpower=speedpower/100
        speedpower=speedpower+5
        nature=nature.replace(" ","")
        if 'on' not in nature:
            c.execute(f"select increases,decreases from Natures where nature={nature}")
            natchange=c.fetchall()
            natchange=str(natchange)
            natchange=natchange.replace("(","")
            natchange=natchange.replace(")","")
            natchange=natchange.replace("[","")
            natchange=natchange.replace("]","")
            natchange=natchange.replace(",,",",")
            changes=natchange.split(',')
            increases=changes[0]
            decreases=changes[1]
            if 'Attack' in increases:
                atkpower=atkpower*1.1
            if 'Attack' in decreases:
                atkpower=atkpower*0.9
            if 'Defense' in increases:
                defpower=defpower*1.1
            if 'Defense' in decreases:
                defpower=defpower*0.9
            if 'Sp_Atk' in increases:
                sp_atkpower=sp_atkpower*1.1
            if 'Sp_Atk' in decreases:
                sp_atkpower=sp_atkpower*0.9
            if 'Sp_Def' in increases:
                sp_defpower=sp_defpower*1.1
            if 'Sp_Def' in decreases:
                sp_defpower=sp_defpower*0.9
            if 'Speed' in increases:
                speedpower=speedpower*1.1
            if 'Speed' in decreases:
                speedpower=speedpower*0.9
        else:
            increases=int(level)
            decreases=int(level)
        
        if "Mega" in name:
            poke=str(poke)
            poke=poke[:-3]
            poke=poke+"-mega"
        if(int(level)<5):
            name="Egg"
            
        if (int(level)<5):
            poke='egg'
        if('T' in str(shiny)):
            poke=str(poke)+"-shiny"
        hp=math.floor(hppower)
        atk=math.floor(atkpower)
        df=math.floor(defpower)
        satk=math.floor(sp_atkpower)
        sdef=math.floor(sp_defpower)
        spd=math.floor(speedpower)
        info=f"""
 Level | {level} |
 Gender | {gender} |
 Nature | {nature} |
 Ability | {ability} |
 Item | {item} |
 EXP  | {exp}  |

|------STATS-------|

  Hp | {hp} | {hpiv} | {hpev} | 
  Atk | {atk} | {atkiv} | {atkev} | 
  Def | {df} | {defiv} | {defev} | 
  SAk | {satk} | {sp_atkiv} | {sp_atkev} |
  SDf | {sdef} | {sp_defiv} | {sp_defev} |
  Spd | {spd} | {speediv} | {speedev} |
  Total     {total}%"""
        embed = discord.Embed(title=f"{str(pokecaught)}  {name} {nick}", description=info, color=0x00ff00)
        embed.set_image(url=f"http://157.245.8.88/html/dex/media/pokemon/sugimori/{str(poke)}.png")
        embed.set_thumbnail(url=ctx.author.avatar_url)
                   
        try:
            await ctx.send(embed=embed)
        except:
            await ctx.send("There was an error. try selecting your pokemon, equipping a nature or ability capsule and try to info it again!")
        c.close()
    @commands.command(name='nickname' , aliases=["n","nick"])
    async def nickname(self, ctx,name:str):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()  
        c.execute(f"select selected from Players where ID={ctx.author.id}")
        selected=c.fetchone()
        selected = str(selected)
        selected=selected[1:-2]
        select=int(selected)
        c.execute(f"update Owned_Pokes set nick='{name}' where Number_Caught={select} and Owner={ctx.author.id}")
        conn.commit()
        c.close()
        await ctx.send(f"You have nicknamed your pokemon to {name}!")        
    @commands.command(name='pokes' , aliases=["p","pokemon"])
    async def pokes(self, ctx):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"Select Number_Caught from Owned_Pokes where {ctx.author.id}=Owner")
        pokesraw=c.fetchall()
        pokesraw=str(pokesraw)
        pokesraw=pokesraw.replace("(","")
        pokesraw=pokesraw.replace(")","")
        pokesraw=pokesraw.replace("[","")
        pokesraw=pokesraw.replace("]","")
        pokesraw=pokesraw.replace("'","")
        pokesraw=pokesraw.replace(",,",",")
        pokesraw=pokesraw.replace(" ","")
        numberlist=pokesraw.split(',')
        pokelen=len(numberlist)
        current=1
        pokeinfos=""
        while current<pokelen:
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={current} and Owner={ctx.author.id}")
            pokeid=c.fetchone()
            pokeid=str(pokeid)
            pokeid=pokeid[1:-2]
            c.execute(f"select Name from Pokes where Number={pokeid}")
            name=c.fetchone()
            name=str(name)
            name=name[2:-3]
            name=name.replace(',','')
            c.execute(f"select level,nick,gender,Shiny from Owned_Pokes where Number_Caught={current} and Owner={ctx.author.id}")
            stuff=c.fetchall()
            stuff=str(stuff)
            stuff=stuff.replace("(","")
            stuff=stuff.replace(")","")
            stuff=stuff.replace("[","")
            stuff=stuff.replace("]","")
            stuff=stuff.replace(",,"," ")
            c.execute(f"select Hp,Atk,Def,Sp_atk,Sp_def,Speed from Owned_Pokes where Number_Caught={current} and Owner={ctx.author.id}")
            ivstuff=c.fetchall()
            ivstuff=str(ivstuff)
            ivstuff=ivstuff.replace("(","")
            ivstuff=ivstuff.replace(")","")
            ivstuff=ivstuff.replace("[","")
            ivstuff=ivstuff.replace("]","")
            ivstuff=ivstuff.replace(",,",",")
            ivs=ivstuff.split(',')
            total=0
            total=total+int(ivs[0])
            total=total+int(ivs[1])
            total=total+int(ivs[2])
            total=total+int(ivs[3])
            total=total+int(ivs[4])
            total=total+int(ivs[5])
            total=total*0.535
            totals=str(round(total))
            if current%25==0:
                var='.'
            else:
                var=""
            pokeinfos=pokeinfos+(str(current)+","+name+","+stuff+totals+"%"+"\n"+var)
            current=current+1
        
        pokeinfos=pokeinfos.replace("Male","♂️")
        pokeinfos=pokeinfos.replace("Female","♀️")
        pokeinfos=pokeinfos.replace("Tranny","⚥")
        pokeinfos=pokeinfos.replace("True","<:shinysm:630772825086754858>")
        pokeinfos=pokeinfos.replace("False","<:pknorm:630748557280018443>")
        pokeinfos=pokeinfos.replace("'","")
        pokeinfos=pokeinfos.replace(",","   ")
        await ctx.send("No.  Name Lv  Nickname  Gender  Shiny  IV %")
        await menu(ctx, pokeinfos.split('.'), DEFAULT_CONTROLS)
        """Embed.message_length = len(embed)""" 
        
        
        c.close()      
    @commands.command(name='trainer' , aliases=["profile"])
    async def trainer(self, ctx):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select redeems,nick,role,Equipped from Players where ID={ctx.author.id}")
        info1=c.fetchall()
        info1=str(info1)
        i1=info1.split(',')
        c.execute(f"select poke_id from Owned_Pokes where Owner={ctx.author.id}")
        p=c.fetchall()
        p=str(p)
        p2=p.split(',')
        roles=str(ctx.author.roles)
        rolelist=""" \n"""
        r=roles.split(',')
        for l in r:
            l=str(l)
            l=l[35:-2]
            rolelist=rolelist+l+"\n"
        

        
        
        pokelen=len(p2)
        pokelen=int(pokelen)/2
        pokelen=str(pokelen)
        pokelen=pokelen[:-2]
        c.execute(f"select Number_Caught from Owned_Pokes where Shiny='True' and Owner={ctx.author.id}")
        sget=c.fetchall()
        sget=str(sget)
        sget=sget.replace("(","")
        sget=sget.replace(")","")
        sget=sget.replace("[","")
        sget=sget.replace("]","")
        sget=sget.replace("'","")
        sget=sget.replace(",,",",")
        
        shinylist=sget.split(',')
        shinies=len(shinylist)-1
        
        embed = discord.Embed(title="-", description="Trainer info", color=0x00ff00)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="Name:" , value=i1[1][2:-1], inline=False)
        embed.add_field(name="Redeems:" , value=i1[0][2:], inline=False)
        embed.add_field(name="Equipped:" , value=i1[3][1:-3], inline=False)
        embed.add_field(name="Role:" , value=rolelist, inline=False)
        embed.add_field(name="Number of Pokes:" , value=pokelen, inline=False)
        embed.add_field(name="Shinies:", value=str(shinies), inline=False)
        await ctx.send(embed=embed)
        c.close()
    @commands.command(name='filter' , aliases=["f"])
    async def filter(self, ctx):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        inputf=ctx.message
        inputf=str(inputf.content)
        inputf=inputf.replace("-f ","")
        inputparam=inputf.replace(" ",",")
        filters=inputparam.split(',')
        if 'p' in filters[0] or 'P' in filters[0] or 'pokes' in filters[0] or 'Pokes' in filters[0] or 'pokemon' in filters[0] or 'Pokemon' in filters[0]:
            if 'type' in filters[1] or 'Type' in filters[1]:
                await ctx.send(f"filtering your pokemon for {filters[2]} type!")
                c.execute(f"select Number from Pokes where Type like '%{filters[2]}%'")
                total=c.fetchall()
                total=str(total)
                total=total[:-1]
                total=total.replace("[","")
                total=total.replace("]","")
                total=total.replace(")","")
                total=total.replace("(","")
                total=total.replace(",,",",")
                total=total.replace(" ","")
                totaltype=total.split(',')
                c.execute(f"select Number_Caught from Owned_Pokes where Owner={ctx.author.id}")
                nums=c.fetchall()
                nums=str(nums)
                nums=nums.replace("[","")
                nums=nums.replace("]","")
                nums=nums.replace(")","")
                nums=nums.replace("(","")
                nums=nums.replace(",,",",")
                nums=nums.replace(" ","")
                ntotal=nums.split(',')
                nlen=len(ntotal)
                count=1
                typelist=[]
                while count<nlen:
                    c.execute(f"select poke_id from Owned_Pokes where Number_Caught={count} and Owner={ctx.author.id}")
                    pokeid=c.fetchone()
                    pokeid=str(pokeid)
                    pokeid=pokeid[1:-2]
                    if pokeid in totaltype:
                        typelist.append(str(count))
                    count=count+1
                pokeinfo=""
                current=0
                for i in typelist:
                    c.execute(f"Select poke_id from Owned_Pokes where Number_Caught={i} and Owner={ctx.author.id}")
                    pid=c.fetchone()
                    pid=str(pid)
                    pid=pid[1:-2]
                    c.execute(f"select Name from Pokes where Number={pid}")
                    name=c.fetchone()
                    name=str(name)
                    name=name[2:-3]
                    c.execute(f"select level,nick,gender,shiny from Owned_Pokes where Number_Caught={i} and Owner={ctx.author.id}")
                    stuff=c.fetchall()
                    stuff=str(stuff)
                    stuff=stuff.replace("(","")
                    stuff=stuff.replace(")","")
                    stuff=stuff.replace("[","")
                    stuff=stuff.replace("]","")
                    stuff=stuff.replace(",,","")
                    stuff=stuff.replace(","," ")
                    stuff=stuff.replace("'","")
                    stuff=stuff.replace("Male","♂️")
                    stuff=stuff.replace("Female","♀️")
                    stuff=stuff.replace("Tranny","⚥")
                        
                    stuff=stuff.replace("True","<:shinysm:630772825086754858>")
                    stuff=stuff.replace("False","<:pknorm:630748557280018443>")
                    if current%24==1:
                        pokeinfo=str(pokeinfo)+str(i)+" "+str(name)+" "+str(stuff)+'.'+'\n'
                    else:
                        pokeinfo=str(pokeinfo)+str(i)+" "+str(name)+" "+str(stuff)+'\n'
                    current=current+1
                await menu(ctx, pokeinfo.replace('🚫','🚫 \n').replace("✨","✨\n").split('.'), DEFAULT_CONTROLS)
            elif 'legend' in filters[1] or 'Legend' in filters[1] or 'l' in filters[1] or 'L' in filters[1]:
                legends=[144,145,146,150,151,243,244,245,249,250,251,377,378,379,380,381,382,383,384,385,386,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,638,639,640,641,642,643,644,645,646,647,648,649]
                legendcaught=[]
                count=1
                c.execute(f"Select Number_Caught from Owned_Pokes where Owner={ctx.author.id}")
                numbers=c.fetchall()
                numbers=str(numbers)
                numbers=numbers.replace("[","")
                numbers=numbers.replace("]","")
                numbers=numbers.replace(")","")
                numbers=numbers.replace("(","")
                numbers=numbers.replace(",,",",")
                shiny=""
                numlist=[]
                numbers=numbers[:-1]
                nums=numbers.split(",")
                for n in nums:
                    c.execute(f"select poke_id from Owned_Pokes where Owner={ctx.author.id} and Number_Caught={int(n)}")
                    pid=c.fetchone()
                    pid=str(pid)
                    pid=pid[1:-2]
                    pid=int(pid)
                    if pid in legends:
                        numlist.append(n)
                if len(numlist)>1:
                    for d in numlist:
                    
                        if '"' not in d:
                            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                            num=c.fetchone()
                            num=str(num)
                            num=num[1:-2]
                            c.execute(f"select Name from Pokes where Number={num}")
                            name=c.fetchone()
                            name=str(name)
                            name=name[2:-3]
                            c.execute(f"select level,nick,gender,Shiny from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                            stuff=c.fetchall()
                            stuff=str(stuff)
                            stuff=stuff.replace("(","")
                            stuff=stuff.replace(")","")
                            stuff=stuff.replace("[","")
                            stuff=stuff.replace("]","")
                            stuff=stuff.replace(",,","")
                            stuff=stuff.replace(","," ")
                            stuff=stuff.replace("'","")
                            if count%24==1:
                                shiny=shiny+d+"   "+name+" "+stuff+"."+','
                            else:                            
                                shiny=shiny+d+"   "+name+" "+stuff+','
                            count=count+1
                            shiny=shiny.replace("Male","♂️")
                            shiny=shiny.replace("Female","♀️")
                            shiny=shiny.replace("Tranny","⚥")
                            
                            shiny=shiny.replace("True","<:shinysm:630772825086754858>")
                            shiny=shiny.replace("False","<:pknorm:630748557280018443>")
                    await menu(ctx, shiny.replace(',','\n').split('.'), DEFAULT_CONTROLS)
 
                else:
                    await ctx.send("You have no legendaries!")
            elif 'iv' in filters[1].lower():
                await ctx.send(f"sorting your pokes by IVS")
                count=1
                c.execute(f"select Number_Caught from Owned_Pokes where Owner={ctx.author.id}")
                pokes=c.fetchall()
                pokes=str(pokes)
                pokes=pokes[1:-2]
                pokes=pokes.replace("(","")
                pokes=pokes.replace(")","")
                pokes=pokes.replace("[","")
                pokes=pokes.replace("]","")
                pokes=pokes.replace("'","")
                pokes=pokes.replace(",,",",")
                pokeslist=pokes.split(',')
                plen=len(pokeslist)
                sortedlist=[]
                sortedpokes=[]
                while count<plen:
                    c.execute(f"select hp,atk,def,sp_atk,sp_def,speed,level,Ev1,Ev2,Ev3,Ev4,Ev5,Ev6,Gender,item,Nature,Shiny,EXP,ability,nick from Owned_Pokes where Number_Caught={count} and Owner={ctx.author.id}")
                    pinfo=c.fetchall()
                    pinfo=str(pinfo)
                    pinfo=pinfo.replace("(","")
                    pinfo=pinfo.replace(")","")
                    pinfo=pinfo.replace("[","")
                    pinfo=pinfo.replace("]","")
                    pinfo=pinfo.replace(",,",",")
                    pi=pinfo.split(',')
                    hpiv=pi[0]
                    atkiv=pi[1]
                    defiv=pi[2]
                    sp_atkiv=pi[3]
                    sp_defiv=pi[4]
                    speediv=pi[5]
                    level=pi[6]
                    hpev=pi[7]
                    atkev=pi[8]
                    defev=pi[9]
                    sp_atkev=pi[10]
                    sp_defev=pi[11]
                    speedev=pi[12]
                    gender=pi[13]
                    item=pi[14]
                    nature=pi[15]
                    shiny=pi[16]
                    exp=pi[17]
                    ability=pi[18]
                    nick=pi[19]
                    total=(int(hpiv)+int(atkiv)+int(defiv)+int(sp_atkiv)+int(sp_defiv)+int(speediv))
                    total=total*(0.537)
                    total=round(total)
                    sortedlist.append(total)
                    sortedpokes.append(count)
                    count=count+1
                completelist=[]
                completelist[0].append(sortedpokes)
                completelist[1].append(sortedlist)
                await ctx.send(str(completelist))
                await ctx.send(str(completelist[1][1]))
                    
            elif 'name' in filters[1] or 'Name' in filters[1] or 'n' in filters[1] or 'N' in filters[1]:
                await ctx.send(f"filtering your pokemon for {filters[2]}!")
                c.execute(f"select Number from Pokes where Name='{filters[2]}'")
                name=c.fetchone()
                name=str(name)
                name=name.replace("[","")
                name=name.replace("]","")
                name=name.replace(")","")
                name=name.replace("(","")
                name=name.replace("'","")
                name=name.replace(",","")
                names=int(name)
                shiny=""
                c.execute(f"select Number_Caught from Owned_Pokes where Owner={ctx.author.id} and poke_id={names}")
    
                shinylist=c.fetchall()
                shinylist=str(shinylist)
                shinylist=shinylist.replace("[","")
                shinylist=shinylist.replace("]","")
                shinylist=shinylist.replace(")","")
                shinylist=shinylist.replace("(","")
                shinylist=shinylist.replace("'","")
                shinylist=shinylist.replace(",,",",")
                shinylist=shinylist[:-1]
                shinyselected=shinylist.split(',')
                count=0
                for d in shinyselected:
                    
                    if '"' not in d:
                        c.execute(f"select poke_id from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                        num=c.fetchone()
                        num=str(num)
                        num=num[1:-2]
                        c.execute(f"select Name from Pokes where Number={num}")
                        name=c.fetchone()
                        name=str(name)
                        name=name[2:-3]
                        c.execute(f"select level,nick,gender,Shiny from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                        stuff=c.fetchall()
                        stuff=str(stuff)
                        stuff=stuff.replace("(","")
                        stuff=stuff.replace(")","")
                        stuff=stuff.replace("[","")
                        stuff=stuff.replace("]","")
                        stuff=stuff.replace(",,","")
                        stuff=stuff.replace(","," ")
                        stuff=stuff.replace("'","")
                        if count%24==1:
                            shiny=shiny+d+"   "+name+" "+stuff+"."+','
                        else:                            
                            shiny=shiny+d+"   "+name+" "+stuff+','
                        count=count+1
                        shiny=shiny.replace("Male","♂️")
                        shiny=shiny.replace("Female","♀️")
                        shiny=shiny.replace("Tranny","⚥")
                        
                        shiny=shiny.replace("True","<:shinysm:630772825086754858>")
                        shiny=shiny.replace("False","<:pknorm:630748557280018443>")
                await menu(ctx, shiny.replace(',','\n').split('.'), DEFAULT_CONTROLS)
            elif 'shiny' in filters[1] or 'Shiny' in filters[1] or 's' in filters[1] or 'S' in filters[1]:
                shiny=" "
                await ctx.send(f"filtering your pokemon for Shiny Pokes!")
                c.execute(f"select Number_Caught from Owned_Pokes where Owner={ctx.author.id} and Shiny='True'")
    
                shinylist=c.fetchall()
                shinylist=str(shinylist)
                shinylist=shinylist.replace("[","")
                shinylist=shinylist.replace("]","")
                shinylist=shinylist.replace(")","")
                shinylist=shinylist.replace("(","")
                shinylist=shinylist.replace("'","")
                shinylist=shinylist.replace(",,",",")
                shinylist=shinylist[:-1]
                shinyselected=shinylist.split(',')
                count=0
                for d in shinyselected:
                    
                    if '"' not in d:
                        c.execute(f"select poke_id from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                        num=c.fetchone()
                        num=str(num)
                        num=num[1:-2]
                        c.execute(f"select Name from Pokes where Number={num}")
                        name=c.fetchone()
                        name=str(name)
                        name=name[2:-3]
                        c.execute(f"select level,nick,gender from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                        stuff=c.fetchall()
                        stuff=str(stuff)
                        stuff=stuff.replace("(","")
                        stuff=stuff.replace(")","")
                        stuff=stuff.replace("[","")
                        stuff=stuff.replace("]","")
                        stuff=stuff.replace(",,","")
                        stuff=stuff.replace(","," ")
                        stuff=stuff.replace("'","")
                        if count%24==1:
                            shiny=shiny+d+"   "+name+" "+stuff+"."+','
                        else:                            
                            shiny=shiny+d+"   "+name+" "+stuff+','
                        count=count+1
                        shiny=shiny.replace("Male","♂️")
                        shiny=shiny.replace("Female","♀️")
                        shiny=shiny.replace("Tranny","⚥")
                        
                        shiny=shiny.replace("True","<:shinysm:630772825086754858>")
                        shiny=shiny.replace("False","<:pknorm:630748557280018443>")
                await menu(ctx, shiny.replace(',','\n').split('.'), DEFAULT_CONTROLS)
            elif 'mega' in filters[1] or 'Mega' in filters[1] or 'm' in filters[1] or 'M' in filters[1]:
                shiny=" "
                await ctx.send(f"filtering your pokemon for Mega Pokes!")
                c.execute(f"select Number_Caught from Owned_Pokes where Owner={ctx.author.id} and item='mega-stone'")
    
                shinylist=c.fetchall()
                shinylist=str(shinylist)
                shinylist=shinylist.replace("[","")
                shinylist=shinylist.replace("]","")
                shinylist=shinylist.replace(")","")
                shinylist=shinylist.replace("(","")
                shinylist=shinylist.replace("'","")
                shinylist=shinylist.replace(",,",",")
                shinylist=shinylist[:-1]
                shinyselected=shinylist.split(',')
                count=0
                for d in shinyselected:
                    
                    if '"' not in d:
                        c.execute(f"select poke_id from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                        num=c.fetchone()
                        num=str(num)
                        num=num[1:-2]
                        c.execute(f"select Name from Pokes where Number={num}")
                        name=c.fetchone()
                        name=str(name)
                        name=name[2:-3]
                        c.execute(f"select level,nick,gender,shiny from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                        stuff=c.fetchall()
                        stuff=str(stuff)
                        stuff=stuff.replace("(","")
                        stuff=stuff.replace(")","")
                        stuff=stuff.replace("[","")
                        stuff=stuff.replace("]","")
                        stuff=stuff.replace(",,","")
                        stuff=stuff.replace(","," ")
                        stuff=stuff.replace("'","")
                        if count%24==1:
                            if 'Mega' in name:
                                shiny=shiny+d+"   "+name+" "+stuff+"."+','
                        else:
                            if 'Mega' in name:                            
                                shiny=shiny+d+"   "+name+" "+stuff+','
                        count=count+1
                        shiny=shiny.replace("Male","♂️")
                        shiny=shiny.replace("Female","♀️")
                        shiny=shiny.replace("Tranny","⚥")
                        shiny=shiny.replace("True","<:shinysm:630772825086754858>")
                        shiny=shiny.replace("False","<:pknorm:630748557280018443>")
                
                await menu(ctx, shiny.replace(',','\n').split('.'), DEFAULT_CONTROLS)            
            elif 'gender' in filters[1] or 'Gender' in filters[1] or 'g' in filters[1] or 'G' in filters[1]:
                shiny=" "
                await ctx.send(f"filtering your pokemon for {filters[2]} Pokes!")
                c.execute(f"select Number_Caught from Owned_Pokes where Owner={ctx.author.id} and gender='Male'")
    
                shinylist=c.fetchall()
                shinylist=str(shinylist)
                shinylist=shinylist.replace("[","")
                shinylist=shinylist.replace("]","")
                shinylist=shinylist.replace(")","")
                shinylist=shinylist.replace("(","")
                shinylist=shinylist.replace("'","")
                shinylist=shinylist.replace(",,",",")
                shinylist=shinylist[:-1]
                shinyselected=shinylist.split(',')
                count=0
                for d in shinyselected:
                    
                    if '"' not in d:
                        c.execute(f"select poke_id from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                        num=c.fetchone()
                        num=str(num)
                        num=num[1:-2]
                        c.execute(f"select Name from Pokes where Number={num}")
                        name=c.fetchone()
                        name=str(name)
                        name=name[2:-3]
                        c.execute(f"select level,nick,gender,shiny from Owned_Pokes where Number_Caught={d} and Owner={ctx.author.id}")
                        stuff=c.fetchall()
                        stuff=str(stuff)
                        stuff=stuff.replace("(","")
                        stuff=stuff.replace(")","")
                        stuff=stuff.replace("[","")
                        stuff=stuff.replace("]","")
                        stuff=stuff.replace(",,","")
                        stuff=stuff.replace(","," ")
                        stuff=stuff.replace("'","")
                        if count%24==1:
                            shiny=shiny+d+"   "+name+" "+stuff+"."+','
                        else:                            
                            shiny=shiny+d+"   "+name+" "+stuff+','
                        count=count+1
                        shiny=shiny.replace("Male","♂️")
                        shiny=shiny.replace("Female","♀️")
                        shiny=shiny.replace("Tranny","⚥")
                        shiny=shiny.replace("True","<:shinysm:630772825086754858>")
                        shiny=shiny.replace("False","<:pknorm:630748557280018443>")
                
                await menu(ctx, shiny.replace(',','\n').split('.'), DEFAULT_CONTROLS)
        elif 'm' in filters[0] or 'M' in filters[0] or 'market' in filters[0] or 'Market' in filters[0] or 'gts' in filters[0] or 'GTS' in filters[0]:
            if 'type' in filters[1] or 'Type' in filters[1]:
                await ctx.send(f"filtering the market for {filters[2]} type!")
        else:
            await ctx.send("Incorrect command!")
    @commands.command(name='form' , aliases=["change"])
    async def form(self, ctx, form:str):
        await ctx.send("You can change forms this way")
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        
        if(form=="mega"):
            
            await ctx.send("Checking for a mega-stone on your selected pokemon.")
            c.execute(f"select selected from Players where ID={ctx.author.id}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            await ctx.send(selected)
            c.execute(f"select item from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
            item=c.fetchone()
            item=str(item)
            if 'mega-stone' in item:
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
                pokeid=c.fetchone()
                pokeid=str(pokeid)
                pokeid=pokeid[1:-2]
                await ctx.send(pokeid)
                c.execute(f"select Name from Pokes where Number={pokeid+'000'}")
                meganame=c.fetchone()
                meganame=str(meganame)
                meganame=meganame[2:-3]
                await ctx.send(meganame)
                c.execute(f"update Owned_Pokes set poke_id={pokeid+'000'} where poke_id={pokeid} and Owner={ctx.author.id} and Number_Caught={selected}")
                conn.commit()
        
                await ctx.send("You pokemon has Meg-Evolved to "+meganame)
            else:
                await ctx.send("You dont have a mega stone equipped!")
            
        elif(form=="mega-x"):
            await ctx.send("Checking for a mega-x-stone on your selected pokemon.")
            await ctx.send("Checking for a mega-stone on your selected pokemon.")
            c.execute(f"select selected from Players where ID={ctx.author.id}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            await ctx.send(selected)
            c.execute(f"select item from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
            item=c.fetchone()
            item=str(item)
            if 'Mega-X-Stone' in item:
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
                pokeid=c.fetchone()
                pokeid=str(pokeid)
                pokeid=pokeid[1:-2]
                await ctx.send(pokeid)
                c.execute(f"select Name from Pokes where Number={pokeid+'001'}")
                meganame=c.fetchone()
                meganame=str(meganame)
                meganame=meganame[2:-3]
                await ctx.send(meganame)
                c.execute(f"update Owned_Pokes set poke_id={pokeid+'001'} where poke_id={pokeid} and Owner={ctx.author.id}")
                conn.commit()
        
                await ctx.send("You pokemon has Meg-Evolved to "+meganame)
            else:
                await ctx.send("You dont have a mega x stone equipped!")
        elif(form=="mega-y"):
            await ctx.send("Checking for a mega-y-stone on your selected pokemon.")

            c.execute(f"select selected from Players where ID={ctx.author.id}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            await ctx.send(selected)
            c.execute(f"select item from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
            item=c.fetchone()
            item=str(item)
            if 'Mega-Y-Stone' in item:
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
                pokeid=c.fetchone()
                pokeid=str(pokeid)
                pokeid=pokeid[1:-2]
                await ctx.send(pokeid)
                c.execute(f"select Name from Pokes where Number={pokeid+'002'}")
                meganame=c.fetchone()
                meganame=str(meganame)
                meganame=meganame[2:-3]
                await ctx.send(meganame)
                c.execute(f"update Owned_Pokes set poke_id={pokeid+'002'} where poke_id={pokeid} and Owner={ctx.author.id}")
                conn.commit()
        
                await ctx.send("You pokemon has Meg-Evolved to "+meganame)
            else:
                await ctx.send("You dont have a mega y stone equipped!")
        if(form=="stone"):
            await ctx.send("Working on stone evos")
        if(form=="alolan"):
            
            await ctx.send("Checking for a alolan-stone on your selected pokemon.")
            c.execute(f"select selected from Players where ID={ctx.author.id}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            await ctx.send(selected)
            c.execute(f"select item from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
            item=c.fetchone()
            item=str(item)
            if 'alolan-stone' in item:
                c.execute(f"select poke_id from Owned_Pokes where Number_Caught={selected} and Owner={ctx.author.id}")
                pokeid=c.fetchone()
                pokeid=str(pokeid)
                pokeid=pokeid[1:-2]
                await ctx.send(pokeid)
                c.execute(f"select Name from Pokes where Number={pokeid}")
                alolan=c.fetchone()
                alolan=str(alolan)
                alolan=alolan[2:-3]
                await ctx.send(alolan)
                alolan=alolan.casefold().capitalize()
                alolan="Alolan-"+alolan
                c.execute(f"select Number from Pokes where Name='{alolan}'")
                newnum=c.fetchone()
                newnum=str(newnum)
                newnum=newnum[1:-2]
                await ctx.send(newnum)
                c.execute(f"update Owned_Pokes set poke_id={newnum} where Number_Caught={selected} and Owner={ctx.author.id}")
                conn.commit()      
                await ctx.send("You have converted your pokemon to an alolan form!")
        elif(form=="change"):
            await ctx.send("Looking for alternate forms for your selected pokemon.")
        else:
            await ctx.send("Please select a proper form")
        c.close()
    @commands.command(name='select' , aliases=["sp"])
    async def select(self, ctx,pokenum:int):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"Select poke_id from Owned_Pokes where {pokenum}= Number_Caught AND {ctx.author.id}=Owner")
        pid=c.fetchone()
        pid=str(pid)
        pid=pid[1:-2]
        c.close()
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select Name from Pokes where Number={pid}")
        name=c.fetchone()
        name=str(name)
       
        c.execute(f"select Level from Owned_Pokes where Number_Caught={pokenum} AND {ctx.author.id}=Owner")
        lv=c.fetchone()
        lv=str(lv)
        lv=lv[1:-2]
        await ctx.send(lv)
        if int(lv)<5:
            name=  "egg"
        c.close()
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"Update Players set selected={pokenum} where ID={ctx.author.id}")
        conn.commit()
        name=name.replace("(","")
        name=name.replace(")","")
        name=name.replace("'","")
        name=name.replace(",","")
        c.close()     
        await ctx.send(f"You have selected your {name}!")
        c.close()
    @commands.command(name='party' , aliases=["team"])
    async def party(self, ctx, target:str,slot:int):
        if 'add' in target:
            await ctx.send('You can add pokemon this way!')
            spot='poke'+str(slot)
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            c = conn.cursor()
            c.execute(f"Select selected from Players where ID='{ctx.author.id}'")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            await ctx.send(str(selected))
            c.execute(f"select poke1,poke2,poke3,poke4,poke5,poke6 from Players where ID='{ctx.author.id}'")
            te=c.fetchall()
            te=str(te)
            if selected in te:
                await ctx.send("This pokemon is already in your party!")
            else:
                c.execute(f"Update Players set {spot}={selected} where ID='{ctx.author.id}'")
            conn.commit()
            c.close() 
            
        elif 'show' in target:
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            c = conn.cursor()
            c.execute(f"select poke1,poke2,poke3,poke4,poke5,poke6 from Players where ID='{ctx.author.id}'")
            team =c.fetchall()
       
            team=str(team)
            team =team[2:-2]
            pokes=team.split(',')
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={pokes[0]} and Owner='{ctx.author.id}'")
            poke1=c.fetchone()
            poke1=str(poke1)
            poke1=poke1[1:-2]
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={pokes[1]} and Owner='{ctx.author.id}'")
            poke2=c.fetchone()
            poke2=str(poke2)
            poke2=poke2[1:-2]
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={pokes[2]} and Owner='{ctx.author.id}'")
            poke3=c.fetchone()
            poke3=str(poke3)
            poke3=poke3[1:-2]
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={pokes[3]} and Owner='{ctx.author.id}'")
            poke4=c.fetchone()
            poke4=str(poke4)
            poke4=poke4[1:-2]
            print(poke4)
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={pokes[4]} and Owner='{ctx.author.id}'")
            poke5=c.fetchone()
            poke5=str(poke5)
            poke5=poke5[1:-2]
            print(poke5)
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught='{pokes[5]}' and Owner='{ctx.author.id}'")
            poke6=c.fetchone()
            poke6=str(poke6)
            poke6=poke6[1:-2]
            print(poke6)
            poke01="None"
            poke02="None"
            poke03="None"
            poke04="None"
            poke05="None"
            poke06="None"
            if(poke1 != 'o'):
                c.execute(f"select Name from pokes where Number={poke1}")
                poke01 = c.fetchone()
                poke01=str(poke01)
                poke01=poke01[2:-3]
                print(poke01)
            if(poke2 != 'o'):
                c.execute(f"select Name from pokes where Number={poke2}")
                poke02 = c.fetchone()
                poke02=str(poke02)
                poke02=poke02[2:-3]
                print(poke02)
            if(poke3 != 'o'):               
                c.execute(f"select Name from pokes where Number={poke3}")
                poke03 = c.fetchone()
                poke03=str(poke03)
                poke03=poke03[2:-3]
                print(poke03)
            if(poke4 != 'o'):
                c.execute(f"select Name from pokes where Number={poke4}")
                poke04 = c.fetchone()
                poke04=str(poke04)
                poke04=poke04[2:-3]
                print(poke04)
            if(poke5 != 'o'):
                c.execute(f"select Name from pokes where Number={poke5}")
                poke05 = c.fetchone()
                poke05=str(poke05)
                poke05=poke05[2:-3]
                print(poke05)
            if(poke6 != 'o'):
                c.execute(f"select Name from pokes where Number={poke6}")
                poke06 = c.fetchone()
                poke06=str(poke06)
                poke06=poke06[2:-3]
                print(poke06)
            c.close()
            pokesd=f"""
                ```
                   |  {poke01+pokes[0]}  |  {poke02+pokes[1]}  | {poke03+pokes[2]}   |
                    ---------------------------
                   |  {poke04+pokes[3]}  |  {poke05+pokes[4]}  |  {poke06+pokes[5]}  |
                    ```"""
            
            embed = discord.Embed(title="-", description="Party", color=0x00ff00)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.add_field(name="Poke 1:" , value=poke01+"   #"+pokes[0] , inline=True)
            embed.add_field(name="Poke 2:" , value=poke02+"   #"+pokes[1] , inline=True)
            embed.add_field(name="Poke 3:" , value=poke03+"   #"+pokes[2] , inline=True)
            embed.add_field(name="Poke 4:" , value=poke04+"   #"+pokes[3] , inline=True)
            embed.add_field(name="Poke 5:" , value=poke05+"   #"+pokes[4] , inline=True)
            embed.add_field(name="Poke 6:" , value=poke06+"   #"+pokes[5] , inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send('That is not a valid command!')
        c.close()
    @commands.command(name='breed' , aliases=["pokesex"])
    @commands.cooldown(1, 180,commands.BucketType.user)
    @charge(amount=350)    
    async def breed(self, ctx, poke1:int,poke2:int):
        await ctx.send(ctx.author.mention+" has paid 350 Blazibucks to the daycare!")
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select poke_id from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
        num1=c.fetchone()
        num1=str(num1)
        num1=num1[1:-2]
        c.execute(f"select poke_id from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
        num2=c.fetchone()
        num2=str(num2)
        num2=num2[1:-2]
        num1=int(num1)
        num2=int(num2)
        c.execute(f"select Name from Pokes where Number={num1}")
        name1=c.fetchone()
        name1=str(name1)
        name1=name1[2:-3]
        c.execute(f"select Name from Pokes where Number={num2}")
        name2=c.fetchone()
        name2=str(name2)
        name2=name2[2:-3]
        shinyrand=rand.randint(0,50)
        if shinyrand==0:
            shiny='True'
        else:
            shiny='False' 
        genderrand=rand.randint(0,1)
        if genderrand==0:
            gender='Male'
        else:
            gender='Female'        
        c.execute(f"select gender from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")        
        gender1=c.fetchone()
        gender1=str(gender1)
        if 'None' in gender1:
            gender1=gender1[1:-2]
        else:
            gender1=gender1[2:-3]
        c.execute(f"select gender from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")        
        gender2=c.fetchone()
        gender2=str(gender2)
        if 'None' in gender2:
            gender2=gender2[1:-2]
        else:
            gender2=gender2[2:-3]
        accepted1=["Male","Tranny","None"]
        accepted2=["Female","Tranny","None"]
        c.execute(f"select nature from Natures")
        natures=c.fetchall()
        natures=str(natures)
        natures=natures.replace("(","")
        natures=natures.replace(")","")
        natures=natures.replace("[","")
        natures=natures.replace("]","")
        natures=natures.replace(" ","")
        natures=natures.replace(",,",",")
        naturelist=natures.split(',')
        lenn=len(naturelist)
        randnat=rand.randint(0,lenn-1)
        nature=naturelist[randnat]
        c.execute(f"select ability from abilities where poke like '%{poke2}%'")
        abilities=c.fetchall()
        abilities=str(abilities)
        abilities= abilities.replace("(","")
        abilities= abilities.replace(")","")
        abilities= abilities.replace("[","")
        abilities= abilities.replace("]","")
        abilities= abilities.replace(" ","")
        abilities= abilities.replace(",,",",")
        abilitylist=abilities.split(',')
        lena=len(abilitylist)
        randa=rand.randint(0,lena-1)
        ability=abilitylist[randa]
        if gender1 in accepted1 and gender2 in accepted2:
            await ctx.send("gonna try to breed")
            c.execute(f"select egg_1 from Pokes where Number={num1}")
            egg11=c.fetchone()
            egg11=str(egg11)
            egg11=egg11[2:-3]
            c.execute(f"select egg_2 from Pokes where Number={num1}")
            egg12=c.fetchone()
            egg12=str(egg12)
            egg12=egg12[2:-3]
            c.execute(f"select egg_1 from Pokes where Number={num2}")
            egg21=c.fetchone()
            egg21=str(egg21)
            egg21=egg21[2:-3]
            c.execute(f"select egg_2 from Pokes where Number={num2}")
            egg22=c.fetchone()
            egg22=str(egg22)
            egg22=egg22[2:-3]
            hp=""
            atk=""
            df=""
            sp_atk=""
            sp_def=""
            speed=""
            eventpokes=['Bulbaween','Ivyween','Veenuween','Mimiween']
            if  'Mega' not in name1 and 'Mega' not in name2 and 'ween' not in name1 and 'ween' not in name2: 
                if egg11==egg21 or egg11==egg22 or egg12==egg21 or egg22==egg22 or '-' in egg11 or '-' in egg12 or '-' in egg21 or '-' in egg22:
                    c.execute(f"select Hp,Atk,Def,Sp_atk,Sp_def,Speed from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")        
                    ivs1=c.fetchall()
                    ivs1=str(ivs1)
                    ivs1=ivs1.replace("(","")
                    ivs1=ivs1.replace(")","")
                    ivs1=ivs1.replace("[","")
                    ivs1=ivs1.replace("]","")
                    ivs1=ivs1.replace(" ","")
                    ivs1=ivs1.replace(",,",",")
                    stats1=ivs1.split(',')
                    c.execute(f"select Hp,Atk,Def,Sp_atk,Sp_def,Speed from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")        
                    ivs2=c.fetchall()
                    ivs2=str(ivs2)
                    ivs2=ivs2.replace("(","")
                    ivs2=ivs2.replace(")","")
                    ivs2=ivs2.replace("[","")
                    ivs2=ivs2.replace("]","")
                    ivs2=ivs2.replace(" ","")
                    ivs2=ivs2.replace(",,",",")
                    stats2=ivs2.split(',')
                    c.execute(f"select item from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")   
                    item1=c.fetchone()
                    item1=str(item1)
                    item1=item1[2:-3]
                    c.execute(f"select item from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")   
                    item2=c.fetchone()
                    item2=str(item2)
                    item2=item2[2:-3]
                    dstat=False
                    nature1=False
                    nature2=False
                    if 'Destiny' in item1 or 'Destiny' in item2:
                        dstat=True
                    if 'Everstone' in item1:
                        nature1=True
                        c.execute(f"select nature from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                        natures=c.fetchone()
                        natures=str(natures)
                        natures=natures.replace("(","")
                        natures=natures.replace(")","")
                        natures=natures.replace("[","")
                        natures=natures.replace("]","")
                        natures=natures.replace(" ","")
                        natures=natures.replace(",,",",")
                        natures=natures.replace(",","")
                        nature=natures
                        nature="'"+nature+"'"
                    if 'Everstone' in item2:
                        nature2=True
                        c.execute(f"select nature from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                        natures=c.fetchone()
                        natures=str(natures)
                        natures=natures.replace("(","")
                        natures=natures.replace(")","")
                        natures=natures.replace("[","")
                        natures=natures.replace("]","")
                        natures=natures.replace(" ","")
                        natures=natures.replace(",,",",")
                        natures=natures.replace(",","")
                        nature=natures
                        nature="'"+nature+"'"
                    breedchance=rand.randint(0,5)
                    if breedchance==0 and dstat==True:
                        newivs=rand.sample(range(6),5)
                        if 0 in newivs:

                            hp=stats1[0]
                        if 1 in newivs:

                            atk=stats1[1]
                        if 2 in newivs:

                            df=stats1[2] 
                        if 3 in newivs:

                            sp_atk=stats1[3]
                        if 4 in newivs:

                            sp_def=stats1[4]
                        if 5 in newivs:

                            speed=stats1[5]
                        if 0 not in newivs:

                            hp=rand.randint(0,31) 
                        if 1 not in newivs:

                            atk=rand.randint(0,31)
                        if 2 not in newivs:

                            df=rand.randint(0,31)
                        if 3 not in newivs:

                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:

                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:

                            speed=rand.randint(0,31)
                        
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                            if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught ,HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()
                            else:
                                await ctx.send("You cannot breed an egg!")
                        else:
                            await ctx.send("you cannot breed a mega!")                        
                    if breedchance==1 and dstat==True:
                        newivs=rand.sample(range(6),5)
                        totalmale=4
                        totalfemale=1
                        currentmale=0
                        currentfemale=0
                     
                        if 0 in newivs:
                            
                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<=totalmale: 
                                hp=stats1[0]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<=totalfemale:
                                hp=stats2[0]              
                        if 1 in newivs:
                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                atk=stats1[1]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                atk=stats2[1] 
                        if 2 in newivs:
                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                df=stats1[2]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                df=stats2[2] 
                        if 3 in newivs:
                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_atk=stats1[3]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                sp_atk=stats2[3] 
                        if 4 in newivs:
                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_def=stats1[4]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                sp_def=stats2[4] 
                        if 5 in newivs:
                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                speed=stats1[5]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                speed=stats2[5] 
                        if 0 not in newivs:
                            hp=rand.randint(0,31) 
                        if 1 not in newivs:
                            atk=rand.randint(0,31)
                        if 2 not in newivs:
                            df=rand.randint(0,31)
                        if 3 not in newivs:
                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:
                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:
                            speed=rand.randint(0,31)
                        await ctx.send(f"hp{hp} atk{atk} def{df} sp atk{sp_atk} sp def{sp_def} speed{speed} ability {ability} nature{nature}")
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                        if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]     
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()     
                    if breedchance==2 and dstat==True:
                        newivs=rand.sample(range(6),5)
                        totalmale=4
                        totalfemale=1
                        currentmale=0
                        currentfemale=0
                         
                        if 0 in newivs:

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                hp=stats1[0]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                hp=stats2[0]              
                        if 1 in newivs:
                            
                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                atk=stats1[1]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                atk=stats2[1] 
                        if 2 in newivs:
                            genderpass=rand.randint(0,1)
                            
                            if genderpass==0 and currentmale<totalmale+1: 
                                df=stats1[2]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                df=stats2[2] 
                        if 3 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_atk=stats1[3]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                sp_atk=stats2[3] 
                        if 4 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_def=stats1[4]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<=totalfemale:
                                sp_def=stats2[4] 
                        if 5 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                speed=stats1[5]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                speed=stats2[5] 
                        if 0 not in newivs:

                            hp=rand.randint(0,31) 
                        if 1 not in newivs:

                            atk=rand.randint(0,31)
                        if 2 not in newivs:

                            df=rand.randint(0,31)
                        if 3 not in newivs:
                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:

                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:

                            speed=rand.randint(0,31)
                        
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                        if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]
                        
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()    
                    if breedchance==3 and dstat==True:
                        newivs=rand.sample(range(6),5)
                        await ctx.send(str(newivs)) 
                        totalmale=3
                        totalfemale=2
                        currentmale=0
                        currentfemale=0
                         
                        if 0 in newivs:

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                hp=stats1[0]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                hp=stats2[0]              
                        if 1 in newivs:

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                atk=stats1[1]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                atk=stats2[1] 
                        if 2 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                df=stats1[2]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                df=stats2[2] 
                        if 3 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_atk=stats1[3]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                sp_atk=stats2[3] 
                        if 4 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_def=stats1[4]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<=totalfemale:
                                sp_def=stats2[4] 
                        if 5 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                speed=stats1[5]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                speed=stats2[5] 
                        if 0 not in newivs:

                            hp=rand.randint(0,31) 
                        if 1 not in newivs:

                            atk=rand.randint(0,31)
                        if 2 not in newivs:

                            df=rand.randint(0,31)
                        if 3 not in newivs:

                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:

                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:

                            speed=rand.randint(0,31)
                        
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                        if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()
                    if breedchance==4 and dstat==True:
                        newivs=rand.sample(range(6),5)
                        await ctx.send(str(newivs)) 
                        totalmale=2
                        totalfemale=3
                        currentmale=0
                        currentfemale=0
                         
                        if 0 in newivs:

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                hp=stats1[0]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                hp=stats2[0]              
                        if 1 in newivs:

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                atk=stats1[1]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                atk=stats2[1] 
                        if 2 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                df=stats1[2]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                df=stats2[2] 
                        if 3 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_atk=stats1[3]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                sp_atk=stats2[3] 
                        if 4 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_def=stats1[4]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<=totalfemale:
                                sp_def=stats2[4] 
                        if 5 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                speed=stats1[5]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                speed=stats2[5] 
                        if 0 not in newivs:

                            hp=rand.randint(0,31) 
                        if 1 not in newivs:

                            atk=rand.randint(0,31)
                        if 2 not in newivs:

                            df=rand.randint(0,31)
                        if 3 not in newivs:

                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:

                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:

                            speed=rand.randint(0,31)
                        
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                        if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()
                    if breedchance==5 and dstat==True:
                        newivs=rand.sample(range(6),5)
                        await ctx.send(str(newivs)) 
                        totalmale=5
                        totalfemale=0
                        currentmale=0
                        currentfemale=0
                         
                        if 0 in newivs:

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                hp=stats1[0]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                hp=stats2[0]              
                        if 1 in newivs:

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                atk=stats1[1]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                atk=stats2[1] 
                        if 2 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                df=stats1[2]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                df=stats2[2] 
                        if 3 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_atk=stats1[3]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                sp_atk=stats2[3] 
                        if 4 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_def=stats1[4]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<=totalfemale:
                                sp_def=stats2[4] 
                        if 5 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                speed=stats1[5]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                speed=stats2[5] 
                        if 0 not in newivs:

                            hp=rand.randint(0,31) 
                        if 1 not in newivs:

                            atk=rand.randint(0,31)
                        if 2 not in newivs:

                            df=rand.randint(0,31)
                        if 3 not in newivs:

                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:

                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:

                            speed=rand.randint(0,31)
                        
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                        if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()                         
                
                    breedchance=rand.randint(0,3)
                    if breedchance==0 and dstat==False:
                        newivs=rand.sample(range(6),3)
                        await ctx.send(str(newivs))
                        if 0 in newivs:

                            hp=stats1[0]
                        if 1 in newivs:

                            atk=stats1[1]
                        if 2 in newivs:

                            df=stats1[2] 
                        if 3 in newivs:

                            sp_atk=stats1[3]
                        if 4 in newivs:

                            sp_def=stats1[4]
                        if 5 in newivs:

                            speed=stats1[5]
                        if 0 not in newivs:

                            hp=rand.randint(0,31) 
                        if 1 not in newivs:

                            atk=rand.randint(0,31)
                        if 2 not in newivs:

                            df=rand.randint(0,31)
                        if 3 not in newivs:

                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:

                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:

                            speed=rand.randint(0,31)
                        
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                        if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()                        
                    if breedchance==1 and dstat==False:
                        newivs=rand.sample(range(6),3)
                        await ctx.send(str(newivs))
                        totalmale=2
                        totalfemale=1
                        currentmale=0
                        currentfemale=0
                         
                        if 0 in newivs:
                            genderpass=rand.randint(0,1)

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<=totalmale: 
                                hp=stats1[0]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<=totalfemale:
                                hp=stats2[0]              
                        if 1 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                atk=stats1[1]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                atk=stats2[1] 
                        if 2 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                df=stats1[2]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                df=stats2[2] 
                        if 3 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_atk=stats1[3]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                sp_atk=stats2[3] 
                        if 4 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_def=stats1[4]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                sp_def=stats2[4] 
                        if 5 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                speed=stats1[5]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                speed=stats2[5] 
                        if 0 not in newivs:

                            hp=rand.randint(0,31) 
                        if 1 not in newivs:

                            atk=rand.randint(0,31)
                        if 2 not in newivs:

                            df=rand.randint(0,31)
                        if 3 not in newivs:

                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:

                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:

                            speed=rand.randint(0,31)
                        await ctx.send(f"hp{hp} atk{atk} def{df} sp atk{sp_atk} sp def{sp_def} speed{speed} ability {ability} nature{nature}")
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                        if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP ,Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()     
                    if breedchance==2 and dstat==False:
                        newivs=rand.sample(range(6),3)
                        await ctx.send(str(newivs))
                        totalmale=2
                        totalfemale=1
                        currentmale=0
                        currentfemale=0
                         
                        if 0 in newivs:

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                hp=stats1[0]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                hp=stats2[0]              
                        if 1 in newivs:

                            genderpass=rand.randint(0,1)
                            if genderpass==0 and currentmale<totalmale+1: 
                                atk=stats1[1]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                atk=stats2[1] 
                        if 2 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                df=stats1[2]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                df=stats2[2] 
                        if 3 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_atk=stats1[3]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<totalfemale+1:
                                sp_atk=stats2[3] 
                        if 4 in newivs:
                            genderpass=rand.randint(0,1)

                            if genderpass==0 and currentmale<totalmale+1: 
                                sp_def=stats1[4]
                                currentmale=currentmale+1
                            elif genderpass==1 and currentfemale<=totalfemale:
                                sp_def=stats2[4] 
                        if 5 in newivs:
                            genderpass=rand.randint(0,1)

                        if genderpass==0 and currentmale<totalmale+1: 
                                speed=stats1[5]
                                currentmale=currentmale+1
                        elif genderpass==1 and currentfemale<totalfemale+1:
                                speed=stats2[5] 
                        if 0 not in newivs:

                            hp=rand.randint(0,31) 
                        if 1 not in newivs:

                            atk=rand.randint(0,31)
                        if 2 not in newivs:

                            df=rand.randint(0,31)
                        if 3 not in newivs:

                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:

                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:

                            speed=rand.randint(0,31)
                        await ctx.send(f"hp{hp} atk{atk} def{df} sp atk{sp_atk} sp def{sp_def} speed{speed} ability {ability} nature{nature}")
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                        if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()     
                    if breedchance==3 and dstat==False:
                        newivs=rand.sample(range(6),3)
                        await ctx.send(str(newivs))
                        if 0 in newivs:

                            hp=stats2[0]
                        if 1 in newivs:

                            atk=stats2[1]
                        if 2 in newivs:

                            df=stats2[2] 
                        if 3 in newivs:

                            sp_atk=stats2[3]
                        if 4 in newivs:

                            sp_def=stats2[4]
                        if 5 in newivs:

                            speed=stats2[5]
                        if 0 not in newivs:

                            hp=rand.randint(0,31) 
                        if 1 not in newivs:

                            atk=rand.randint(0,31)
                        if 2 not in newivs:

                            df=rand.randint(0,31)
                        if 3 not in newivs:

                            sp_atk=rand.randint(0,31)
                        if 4 not in newivs:

                            sp_def=rand.randint(0,31)
                        if 5 not in newivs:

                            speed=rand.randint(0,31)                      
                        
                        c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner={ctx.author.id}")
                        numberofpokes=c.fetchall()
                        noofpokes=len(numberofpokes)
                        newnumberofpokes=noofpokes+1
                        if 'Mega' not in name1 and 'Mega' not in name2:
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke1} and Owner={ctx.author.id}")
                            level1=c.fetchone()
                            level1=str(level1)
                            level1=level1[1:-2]
                            c.execute(f"select level from Owned_Pokes where Number_Caught={poke2} and Owner={ctx.author.id}")
                            level2=c.fetchone()
                            level2=str(level2)
                            level2=level2[1:-2]
                        if int(level1)>4 and int(level2)>5:
                                st=[]
                                st.append(hp)
                                st.append(atk)
                                st.append(df)
                                st.append(sp_atk)
                                st.append(sp_def)
                                st.append(speed)
                                at=[]
                                for s in st:
                                    ivchance=rand.randint(0,20)
                                    if int(s)>20:
                                        if ivchance==0:
                                            s=s
                                        else:
                                            stch=rand.randint(0,5)
                                            
                                            s=int(s)-stch
                                            s=str(s)
                                            at.append(s)
                                hp=at[0]
                                atk=at[1]
                                df=at[2]
                                sp_atk=at[3]
                                sp_def=at[4]
                                speed=at[5]
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,shiny,Nature,Ability,gender  ) VALUES({newnumberofpokes},{num2},1,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.author.id},'0','','','','','{shiny}',{nature},{ability},'{gender}');");
                                conn.commit()     
                else:
                    await ctx.send("Incompatible egg groups-- Your pokemon just don't like each other enough for that")
            else:
                await ctx.send("You cannot breed event pokes")          
        else:
            await ctx.send("Check your pokemon's genders")
    @commands.command(name='battle' , aliases=["fight"])
    @commands.cooldown(1, 7200,commands.BucketType.user)
    async def battle(self, ctx, opponent:discord.Member):
        await ctx.send("https://i.makeagif.com/media/3-22-2015/Z6oKLz.gif")
        await ctx.send(f"<@{opponent.id}>! {ctx.author.mention} has challenged you to a pokemon duel! Say Yes to Accept or Nah to Decline!")
        yesnoduel = await self.bot.wait_for("message",timeout=1300)
        while yesnoduel.author.id != opponent.id:
            yesnoduel = await self.bot.wait_for("message",timeout=1300) 
        if yesnoduel.content.casefold().capitalize()=="Yes":
            await ctx.send("Preparing for your duel..")
            duel='true'
        else:
            await ctx.send(f"{opponent.mention} has declined the duel!")     
        if(duel=='true'):
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            c = conn.cursor()
            c.execute(f"Select selected from Players where ID='{ctx.author.id}'")
            selected1=c.fetchone()
            c.execute(f"Select selected from Players where ID='{opponent.id}'")
            selected2=c.fetchone()
            selected1=str(selected1)
            selected1=selected1[1:-2]
            selected2=str(selected2)
            selected2=selected2[1:-2]
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={int(selected1)} and Owner={ctx.author.id}")
            pid1=c.fetchone()
            pid1=str(pid1)
            pid1=pid1[1:-2]
            c.execute(f"select poke_id from Owned_Pokes where Number_Caught={int(selected1)} and Owner={opponent.id}")
            pid2=c.fetchone()
            pid2=str(pid2)
            pid2=pid2[1:-2]
            c.execute(f"select Name from Pokes where Number={int(pid1)}")
            name1=c.fetchone()
            name1=str(name1)
            name1=name1[2:-3]
            c.execute(f"select Name from Pokes where Number={int(pid2)}")
            name2=c.fetchone()
            name2=str(name2)
            name2=name2[2:-3]
            await ctx.send(f"{name1} vs {name2}")
            c.execute(f"select level,Hp,Atk,Def,Sp_atk,Sp_def,Speed,item,move1,move2,move3,move4,nature,ability,ev1,ev2,ev3,ev4,ev5,ev6 from Owned_Pokes where Number_Caught={int(selected1)} and Owner={ctx.author.id}")
            stats1=c.fetchall()
            c.execute(f"select level,Hp,Atk,Def,Sp_atk,Sp_def,Speed,item,move1,move2,move3,move4,nature,ability,ev1,ev2,ev3,ev4,ev5,ev6 from Owned_Pokes where Number_Caught={int(selected2)} and Owner={opponent.id}")
            stats2=c.fetchall()
            stats1=str(stats1)
            stats2=str(stats2)
            stats1=stats1.replace("(","")
            stats1=stats1.replace(")","")
            stats1=stats1.replace("[","")
            stats1=stats1.replace("]","")
            stats1=stats1.replace(",,",",")
            stats1=stats1.replace("'","")
            stats2=stats2.replace("(","")
            stats2=stats2.replace(")","")
            stats2=stats2.replace("[","")
            stats2=stats2.replace("]","")
            stats2=stats2.replace(",,",",")
            stats2=stats2.replace("'","")
            s1=stats1.split(',')
            s2=stats2.split(',')
            level1=s1[0]
            hp1=s1[1]
            atk1=s1[2]
            def1=s1[3]
            spatk1=s1[4]
            spdef1=s1[5]
            speed1=s1[6]
            item1=s1[7]
            move11=s1[8]
            move12=s1[9]
            move13=s1[10]
            move14=s1[11]
            nature1=s1[12]
            ability1=s1[13]
            hpev=s1[14]
            atkev=s1[15]
            defev=s1[16]
            spatkev=s1[17]
            spdefev=s1[18]
            speedev=s1[19]
            c.execute(f"select HP,Attack,Defense,Sp_Atk,Sp_Def,Speed from Pokes where Name='{name1}'")
            base=c.fetchall()
            base=str(base)
            base=base.replace("(","")
            base=base.replace(")","")
            base=base.replace("[","")
            base=base.replace("]","")
            base=base.replace(",,",",")
            bases=base.split(',')
            hppower=(int(bases[0])+int(hp1))*1.701+(int(hpev)/4)
            hppower=hppower*int(level1)
            hppower=hppower/100
            hppower1=hppower+int(level1)+10
            atkpower=(int(bases[1])+int(atk1))*1.771+(math.sqrt(int(atkev))/4)
            atkpower=atkpower*int(level1)
            atkpower=atkpower/100
            atkpower1=atkpower+5
            sp_atkpower=(int(bases[3])+int(spatk1))*1.78+(math.sqrt(int(spatkev))/4)
            sp_atkpower=sp_atkpower*int(level1)
            sp_atkpower=sp_atkpower/100
            sp_atkpower1=sp_atkpower+5
            defpower=(int(bases[2])+int(def1))*1.7755+(math.sqrt(int(defev))/4)
            defpower=defpower*int(level1)
            defpower=defpower/100
            defpower1=defpower+5
            sp_defpower=(int(bases[4])+int(spdef1))*1.835+(math.sqrt(int(spdefev))/4)
            sp_defpower=sp_defpower*int(level1)
            sp_defpower=sp_defpower/100
            sp_defpower1=sp_defpower+5
            speedpower=(int(bases[5])+int(speed1))*1.8145+(math.sqrt(int(speedev))/4)
            speedpower=speedpower*int(level1)
            speedpower=speedpower/100
            speedpower1=speedpower+5
            
            level1=s1[0]
            hp2=s2[1]
            atk2=s2[2]
            def2=s2[3]
            spatk2=s2[4]
            spdef2=s2[5]
            speed2=s2[6]
            item2=s2[7]
            move21=s2[8]
            move22=s2[9]
            move23=s2[10]
            move24=s2[11]
            nature2=s2[12]
            ability2=s2[13]
            hpev=s2[14]
            atkev=s2[15]
            defev=s2[16]
            spatkev=s2[17]
            spdefev=s2[18]
            speedev=s2[19]
            c.execute(f"select HP,Attack,Defense,Sp_Atk,Sp_Def,Speed from Pokes where Name='{name2}'")
            base=c.fetchall()
            base=str(base)
            base=base.replace("(","")
            base=base.replace(")","")
            base=base.replace("[","")
            base=base.replace("]","")
            base=base.replace(",,",",")
            bases=base.split(',')
            hppower=(int(bases[0])+int(hp1))*1.701+(int(hpev)/4)
            hppower=hppower*int(level1)
            hppower=hppower/100
            hppower2=hppower+int(level1)+10
            atkpower=(int(bases[1])+int(atk1))*1.771+(math.sqrt(int(atkev))/4)
            atkpower=atkpower*int(level1)
            atkpower=atkpower/100
            atkpower2=atkpower+5
            sp_atkpower=(int(bases[3])+int(spatk1))*1.78+(math.sqrt(int(spatkev))/4)
            sp_atkpower=sp_atkpower*int(level1)
            sp_atkpower=sp_atkpower/100
            sp_atkpower2=sp_atkpower+5
            defpower=(int(bases[2])+int(def1))*1.7755+(math.sqrt(int(defev))/4)
            defpower=defpower*int(level1)
            defpower=defpower/100
            defpower2=defpower+5
            sp_defpower=(int(bases[4])+int(spdef1))*1.835+(math.sqrt(int(spdefev))/4)
            sp_defpower=sp_defpower*int(level1)
            sp_defpower=sp_defpower/100
            sp_defpower2=sp_defpower+5
            speedpower=(int(bases[5])+int(speed1))*1.8145+(math.sqrt(int(speedev))/4)
            speedpower=speedpower*int(level1)
            speedpower=speedpower/100
            speedpower2=speedpower+5
            await ctx.send(stats1+"\n"+stats2)
            await ctx.send(f"{name1}--{round(hppower1)} vs {name2}--{round(hppower2)}")
            while hppower1>1 and hppower2>1:
                await ctx.send(f"{ctx.author.mention} choose a move!")
                move1 = await self.bot.wait_for("message",timeout=300)
                while move1.author.id != ctx.author.id:
                    move1= await self.bot.wait_for("message",timeout=1000)
                    await ctx.send("BLAZI GONNA FUCK YOU UPPP")
                await ctx.send(f"{opponent.mention} choose a move!")
                move2 = await self.bot.wait_for("message",timeout=300)
                while move2.author.id != opponent.id:
                    move2= await self.bot.wait_for("message",timeout=1000)
                firstmove="move"+move1[-1:]
                secondmove="move"+move2[-1:]
                c.execute(f"select {firstmove} from Owned_Pokes where Number_Caught={selected1} and Owner={ctx.author.id}") 
                moveo=c.fetchone()
                moveo=str(moveo)[2:-3]
                c.execute(f"select {secondmove} from Owned_Pokes where Number_Caught={selected2} and Owner={ctx.author.id}") 
                movet=c.fetchone()
                movet=str(movet)[2:-3]
                c.execute(f"Select damage_class,damage_id,accuracy,type_id from Moves where identifier={moveo}")
                movestuff1=c.fetchall()
                c.execute(f"Select damage_class,damage_id,accuracy,type_id from Moves where identifier={movet}")
                movestuff2=c.fetchall()
                
                
                hppower1=0
                
    @commands.command(name="items", aliases=['it'])
    async def items(self,ctx):
        
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')        
        c = conn.cursor()
        c.execute(f"select number,name from items where owner={ctx.author.id}")
        items=c.fetchall()
        items=str(items)
        items=items.replace("(","")
        items=items.replace(")","")
        items=items.replace("'","")
        items=items.replace("[","")
        items=items.replace("]","")
        items=re.sub('(,[^,]*),', r'\1 ', items)
        items=re.sub('( [^ ]*) ', r'\1 ', items)
        items=items.replace(",","--")
        items=items.replace(" ","-")
        
        items=items.replace("---",".")
        items=items.replace("--","_")
        
        itemslist=items.split('`')
        count=0
        for i in itemslist:
            if count==10:
                i=i+'\n'
                count=0
            else:
                count= count+1        
        
        await menu(ctx, str(itemslist)[2:-2].replace('_','\n').replace('.','--').split('`'), DEFAULT_CONTROLS)
        
        c.close()
        
    @commands.command(name="sell" , aliases=["slp"])
    async def sell(self,ctx,poke:int,price:int):
        await ctx.send("You can sell pokemon to the global market this way!")   
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')        
        c = conn.cursor()
        c.execute(f"select poke_id from Owned_Pokes where Number_Caught={poke} and Owner={ctx.author.id}")
        num=c.fetchone()
        num=str(num)
        num=num[1:-2]
        c.execute(f"select Name from Pokes where Number={num}")
        name=c.fetchone()
        name=str(name)
        name=name[2:-3]
        await ctx.send(name)
        c.execute(f"select level,hp,atk,def,sp_atk,sp_def,speed from Owned_Pokes where Number_Caught={poke} and Owner={ctx.author.id}")
        stats=c.fetchall()
        stats=str(stats)
        stats=stats[2:-3]
        stats.replace(")","")
        stat=stats.split(',')
        if ')' in stats[6]:
            stat6=stats[6][:-1]
        totalstats=0
        totalstats=totalstats+(int(stat[1])*0.537)
        totalstats=totalstats+(int(stat[2])*0.537)
        totalstats=totalstats+(int(stat[3])*0.537)
        totalstats=totalstats+(int(stat[4])*0.537)
        totalstats=totalstats+(int(stat[5])*0.537)
        totalstats=totalstats+(int(stat[6])*0.537)
        totaliv=int(round(totalstats))
        level=int(stats[0])
        c.execute(f"select number from market")
        numberlist=c.fetchall()
        numberlist=str(numberlist)
        numberlist=numberlist[2:-3]
        numberlist=numberlist.replace(")","")
        numberlist=numberlist.replace("(","")
        numberlist=numberlist.replace("]","")
        numberlist=numberlist.replace("[","")
        numberlist=numberlist.replace(",,",",")
       
        
        await ctx.send(f"list {numberlist}")
        numa=numberlist.split(',')
        numba=len(numa)
        await ctx.send(numba)
        numbl=int(numba)
        c.execute(f"insert into market(number, seller,name,iv,level,price)Values({numbl},{ctx.author.id},'{name}',{totaliv},{level},{price})")
        conn.commit()
        c.execute(f"delete from Owned_Pokes where Owner={ctx.author.id} and Number_Caught={poke}")
        conn.commit()
        c.execute(f"select Number_Caught from Owned_Pokes where Owner={ctx.author.id}")
        numlist=c.fetchall()
        numlist=str(numlist)
        numlist=numlist[2:-3]
        await ctx.send("numlist"+numlist)
        numlist=numlist.replace(")","")
        numlist=numlist.replace("(","")
        numlist=numlist.replace("]","")
        numlist=numlist.replace("[","")
        numlist=numlist.replace(",,",",")
        numlist=numlist.replace("'","")
        numb=numlist.split(',')
        
        current=1
        n=len(numb)
        numb=str(numb).replace("'","")
        numb=str(numb).replace(" ","")
        nu=numb.split(',')
        await ctx.send("numb"+str(nu))
        await ctx.send("current"+nu[current])
        await ctx.send(poke)
        while current<n:
            if ']' in nu[current]:
                co=int(nu[current][:-1])
            elif ',' in nu[current]:
                co=int(nu[current][:-1])
            else:
                co=int(nu[current])
            if int(co)>poke:
                numbno=co-1
                c.execute(f"update Owned_Pokes set Number_Caught={numbno} where Number_Caught={co} and Owner={ctx.author.id}")
                conn.commit()
            current=current+1
        c.execute(f"select poke1,poke2,poke3,poke4,poke5,poke6,selected from Players where ID={ctx.author.id}")
        partypokes=c.fetchall()
        partypokes=str(partypokes)
        partypokes=partypokes.replace("(","")
        partypokes=partypokes.replace(")","")
        partypokes=partypokes.replace("[","")
        partypokes=partypokes.replace("]","")
        partypokes=partypokes.replace(",,",",")
        party=partypokes.split(',')
        partyno=1
        
                     
        c.close()
        await ctx.send(f"You have put your {name} on the market for {price}")   
    @commands.command(name="market", aliases=['mp'])
    async def market(self,ctx):
        await ctx.send("https://3.bp.blogspot.com/-MgfLiUcvUxk/VqquHeOAkeI/AAAAAAAAA74/8jwU6Vh6Dgo/s640/tumblr_inline_mr2gi3H4e51rvwlfd.gif")
        await ctx.send("Welcome to the Global Pokemon Market! You can buy and sell pokemon here!")
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')        
        c = conn.cursor()
        c.execute(f"select number from market")
        market=c.fetchall()
        market=str(market)
        market=market.replace("(","")
        market=market.replace(")","")
        market=market.replace("[","")
        market=market.replace("]","")
        market=market.replace(",,",",")
        marketpokes=market.split(',')
        num=len(marketpokes)
        current=1
        
            
        await ctx.send("Number    |    Seller    |    Name    |   IV   |    Level    |    Cost")
        stuff=""
        while current<=num:
            c.execute(f"select * from market where number={current}")
            pokeinfos=c.fetchall()   
            pokeinfos=str(pokeinfos)
            pokeinfos=pokeinfos.replace("(","")
            pokeinfos=pokeinfos.replace(")","")
            pokeinfos=pokeinfos.replace("[","")
            pokeinfos=pokeinfos.replace("]","")
            pokeinfos=pokeinfos.replace(",,",",")
            pokeinfo=pokeinfos.split(',')         
            stuff=(stuff+str(pokeinfo)+'\n')
            
            current=current+1
        if (current>num):
            print("thats all")
            await ctx.send_interactive(pagify(stuff))
        if(num<1):
            await ctx.send("There are no pokemon in the market!")
            
        c.close()
    @commands.command(name="mart", aliases=['pm','shop','pokemart'])
    async def mart(self,ctx):
        await ctx.send("https://vignette.wikia.nocookie.net/pokemon/images/2/27/A_pok%C3%A9_mart_in_Omega_Ruby_%26_Alpha_Saphire.png~/revision/latest?cb=20151128233933")
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select name from shop")
        num=c.fetchall()
        num=str(num)
        num=num[1:-1]
        
        num=num.replace(")","")
        num=num.replace("(","")
        num=num.replace("'","")
        num=num.replace(",,",",")
        number=num.split(',')
        nitems=len(number)
        current=0
        lists=""
        await ctx.send("```*Cost -- Item*```")
        while current<nitems-1:
            c.execute(f"select cost from shop")
            stuff=c.fetchall()
            stuff=str(stuff)
            stuff=stuff[1:-1]
            stuff=stuff.replace("(","")
            stuff=stuff.replace(")","")
            stuff=stuff.replace(",,",",")
            s=stuff.split(',')
            lists=lists+str(s[current]).replace("'","")+"--"+number[current]+"\n"
            current=current+1
        lists="```"+lists+"```"
        await ctx.send_interactive(pagify(lists))
        c.close()
    @commands.command(name="eventmon" , aliases=["event"])
    async def eventmon(self,ctx):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')        
        c = conn.cursor()
        c.execute(f"select poke_id from Owned_Pokes where Owner={ctx.message.author.id}")
        pokes=c.fetchall()
        pokes=str(pokes)
        pokes=pokes.replace("(","")
        pokes=pokes.replace(")","")
        pokes=pokes.replace("[","")
        pokes=pokes.replace("]","")
        pokes=pokes.replace(",,",",")
        if '303030' in pokes:
            await ctx.send("You already have this event poke!")
        else:
            c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner='{ctx.message.author.id}'")
                        
            numberofpokes=c.fetchall()
            noofpokes=len(numberofpokes)
            newnumberofpokes=noofpokes+1
            level=rand.randint(5,10)
            hp=rand.randint(15,31)
            atk=rand.randint(15,31)
            df=rand.randint(15,31)
            sp_atk=rand.randint(15,31)
            sp_def=rand.randint(15,31)
            speed=rand.randint(15,31)    
            gender=rand.randint(0,1)
            if(gender==0):
                pickedg="Male"
            else:
                pickedg="Female"
            nature='Jolly'
            ability='None'
            c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,gender,item,Nature,Shiny,ability) VALUES({newnumberofpokes},303030,10,{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{ctx.message.author.id},0,'','','','','{pickedg}','None','{nature}','False','{ability}');");
            conn.commit()
            c.close()
            
    @commands.command(name="tourney" , aliases=["t"])
    async def tourney(self,ctx):
        cmds=ctx.message.content
        cmds=str(cmds)
        cmds=cmds.replace('-tourney','')
        cmds=cmds.replace('-t','')
        cmd=cmds.split(' ')
        clen=len(cmd)
        if clen==1:
            await ctx.send("http://pokepla.net:8085/")
        elif 'join' in cmd:
            await ctx.send("gonna add you..")
    @commands.command(name="spawn" , aliases=["look"])
    @charge(amount=80)
    @commands.cooldown(1, 1800,commands.BucketType.user)
    async def spawn(self,ctx,typeof:str):
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')        
        c = conn.cursor()
        c.execute(f"SELECT ID from Players where ID='{ctx.author.id}'")
        exists=c.fetchone()
        exists=str(exists)
        if("None" in exists):
            await ctx.send("Go see Oak First with -start!")
        else:
            await ctx.send(ctx.author.mention+" has been charged 80 BlaziBucks")
           
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            c = conn.cursor()
            c.execute(f"Select Name from Pokes where Type like '%{typeof}%'")
            spawnpokes=c.fetchall()
            spawnpokes=str(spawnpokes)
            spawnpokes[4:-2]
            spawns=spawnpokes.split(',), (')
            randspawn=len(spawns)
            spn=rand.randint(0,randspawn-1)
            spawnedpoke=spawns[spn]
            spawnedpoke=spawnedpoke[1:-1]
            
            c.execute(f"select selected from Players where ID={ctx.author.id}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            c.execute(f"select item from Owned_Pokes where Owner={ctx.author.id} and Number_Caught={selected}")
            items=c.fetchone()
            items=str(items)
            if 'Honey' in items or 'honey' in items:
                legends=[-234567890]
            else:
                legends=[144,145,146,150,151,243,244,245,249,250,251,377,378,379,380,381,382,383,384,385,386,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,638,639,640,641,642,643,644,645,646,647,648,649]
            if 'Mega' in spawnedpoke:
                spawnedpoke=spawnedpoke.replace("Mega-","")
                spawnedpoke=spawnedpoke.replace("-Y","")
                spawnedpoke=spawnedpoke.replace("-X","")
                spawnedpoke=spawnedpoke.replace("-y","")
                spawnedpoke=spawnedpoke.replace("-x","")
            else:
                spawnedpoke=spawnedpoke            
            c.execute(f"Select Number from pokes where Name='{spawnedpoke}'")
            poke=c.fetchone()
            poke=str(poke)
            poke=poke[1:-2]
            legendchance=rand.randint(0,1000)
            if poke in legends and legendchance ==0:
                spn=rand.randint(0,randspawn-1)
                spawnedpoke=spawns[spn]
                spawnedpoke=spawnedpoke[1:-1]
                c.execute(f"Select Number from pokes where Name='{spawnedpoke}'")
                poke=c.fetchone()
                poke=str(poke)
                poke=poke[1:-2]
            shinyrand=rand.randint(0,2000)
            if shinyrand==0:
                spoke=poke+"-shiny"
                shiny='True'
            else:
                spoke=poke
                shiny='False'
            embed = discord.Embed(title="Custom Spawns", description="spawning "+typeof, color=0x00ff00)
            embed.set_image(url=f"http://157.245.8.88/html/dex/media/pokemon/sugimori/{spoke}.png")
            embed.add_field(name="How to catch!", value="Say the pokemon's name to catch it!", inline=False)
            await ctx.send(embed=embed)
            catchtry = await self.bot.wait_for("message",timeout=1300)
            while catchtry.author.id != ctx.author.id and catchtry.channel != ctx.channel or catchtry.author.id != ctx.author.id:
                
                    
                    catchtry = await self.bot.wait_for("message",timeout=1300)                
            if catchtry.content.casefold().capitalize() in spawnedpoke or catchtry.content=='*':
                conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
                c = conn.cursor()
                c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner='{catchtry.author.id}'")
                        
                numberofpokes=c.fetchall()
                c.close()
                noofpokes=len(numberofpokes)
                newnumberofpokes=noofpokes+1
                conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
                level=rand.randint(5,10)
                hp=rand.randint(10,20)
                atk=rand.randint(10,20)
                df=rand.randint(10,20)
                sp_atk=rand.randint(10,20)
                sp_def=rand.randint(10,20)
                speed=rand.randint(10,20)    
                gender=rand.randint(0,1)
                if(gender==0):
                    pickedg="Male"
                else:
                    pickedg="Female"
                conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db') 
                c = conn.cursor()
                c.execute(f"select nature from natures")
                allnatures=c.fetchall()
                allnatures=str(allnatures)
                allnatures=allnatures.replace("[","")
                allnatures=allnatures.replace("]","")
                allnatures=allnatures.replace("(","")
                allnatures=allnatures.replace(")","")
                allnatures=allnatures.replace(",,",",")
                naturelist=allnatures.split(',')
                natlen=len(naturelist)
                randnat=rand.randint(0,natlen-1)
                nature=naturelist[randnat]
                nature=nature.replace("'","")
                nature=nature.replace(" ","")
                if ',' in nature:
                    nature='Jolly'
                
                c.execute(f"select ability from abilities where poke like '%{poke}%'")
                abilitylist=c.fetchall()
                abilitylist=str(abilitylist)
                abilitylist=abilitylist.replace(")","")
                abilitylist=abilitylist.replace("(","")
                abilitylist=abilitylist.replace("]","")
                abilitylist=abilitylist.replace("[","")
                abilitylist=abilitylist.replace("'","")
                abilitylist=abilitylist.replace(",,",",")
                abilities=abilitylist.split(',')
                abilitylen=len(abilities)
                randabil=rand.randint(0,abilitylen-1)
                ability=abilities[randabil]
                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,gender,item,Nature,Shiny,ability) VALUES({newnumberofpokes},{poke},{level},{newnumberofpokes},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{catchtry.author.id},0,'','','','','{pickedg}','None','{nature}','{shiny}','{ability}');");
                conn.commit()
                c.close()
                await ctx.send("You caught it!")        
            else:
                await ctx.send(f"{spawnedpoke} fled!")

            c.close()
    @commands.Cog.listener()
    async def on_message(self,message):
        if 'waifu' in message.content or 'asuna' in message.content or 'sao' in message.content or 'anime' in message.content:
            wai="♡♡ AAAAAAAAAAASSSSSSSSSSSSSSSUUUUUUUUUUUNNNNNNNNNNNAAAAAAAAAAAA♡♡"+"\n"
            await message.channel.send(wai*5 )
        conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
        c = conn.cursor()
        c.execute(f"select disabled from disables where disabled={int(message.channel.id)}")
        redirects=c.fetchone()
        redirect=str(redirects)
        if '-' in message.content or message.author.id==548295233138327583: 
            if 'on' in redirect:
                " "
            else:
                await message.delete()
                await message.delete()
        if '||' not in message.content:
            if 'fuck'.casefold() in message.content.lower() or 'damn'.casefold().lower() in message.content.lower() or 'shit'.casefold() in message.content.lower() or 'bitch'.casefold() in message.content.lower() or 'f u c k'.casefold() in message.content.lower() or 'd a m n'.casefold() in message.content.lower() or 's h i t'.casefold() in message.content.lower() or 'b i t c h'.casefold() in message.content.lower() or 'cock'.casefold() in message.content.lower() or  'c o c k'.casefold() in message.content.lower() or 'pussy'.casefold() in message.content.lower() or 'p u s s y'.casefold() in message.content.lower():
                m=message.content
                m=str(m)
                m=m.lower()
                m=m.replace('-','_')
                m=m.replace('*','_')
                m=m.replace('^','_')
                m=m.replace(',','_')
                m=m.replace("cock".casefold(),"||cock||")
                m=m.replace("c o c k".casefold(),"||c o c k||")
                m=m.replace("pussy".casefold(),"||pussy||")
                m=m.replace("p u s s y".casefold(),"||p u s s y||")
                m=m.replace("fuck".casefold(),"||fuck||")
                m=m.replace("damn".casefold(),"||damn||")
                m=m.replace("shit".casefold(),"||shit||")
                m=m.replace("f u c k".casefold(),"||f u c k||")
                m=m.replace("d a m n".casefold(),"||d a m n||")
                m=m.replace("s h i t".casefold(),"||s h i t||")
                m=m.replace("bitch".casefold(),"||bitch||")
                m=m.replace("b i t c h".casefold(),"||b i t c h||")
                m=m.replace("f.u.c.k".casefold(),"||f u c k||")
                m=m.replace("d.a.m.n".casefold(),"||d.a.m.n||")
                m=m.replace("s.h.i.t".casefold(),"||s.h.i.t||")
                m=m.replace("b.i.t.c.h".casefold(),"||b.i.t.c.h||")
                m=m.replace("f_u_c_k".casefold(),"||f u c k||")
                m=m.replace("d_a_m_n".casefold(),"||d.a.m.n||")
                m=m.replace("s_h_i_t".casefold(),"||s.h.i.t||")
                m=m.replace("b_i_t_c_h".casefold(),"||b_i_t_c_h||")
                m=m.replace("f_u_c_k".casefold(),"||f u c k||")
                m=m.replace("d_a_m_n".casefold(),"||d.a.m.n||")
                m=m.replace("s_h_i_t".casefold(),"||s.h.i.t||")
                m=m.replace("b_i_t_c_h".casefold(),"||b_i_t_c_h||")
                m=m.replace("FUCK".casefold(),"||FUCK||")
                m=m.replace("DAMN".casefold(),"||DAMN||")
                m=m.replace("SHIT".casefold(),"||shit||")
                m=m.replace("F U C K".casefold(),"||f u c k||")
                m=m.replace("D A M N".casefold(),"||d a m n||")
                m=m.replace("S H I T".casefold(),"||s h i t||")
                m=m.replace("BITCH".casefold(),"||bitch||")
                m=m.replace("B I T C H".casefold(),"||b i t c h||")
                m=m.replace("F.U.C.K".casefold(),"||f u c k||")
                m=m.replace("D.A.M.N".casefold(),"||d.a.m.n||")
                m=m.replace("S.H.I.T".casefold(),"||s.h.i.t||")
                m=m.replace("B.I.T.C.H".casefold(),"||b.i.t.c.h||")
                m=m.replace("F_U_C_K".casefold(),"||f u c k||")
                m=m.replace("D_A_M_N".casefold(),"||d.a.m.n||")
                m=m.replace("S_H_I_T".casefold(),"||s.h.i.t||")
                m=m.replace("B_I_T_C_H".casefold(),"||b_i_t_c_h||")
                m=m.replace("f_u_c_k".casefold(),"||f u c k||")
                m=m.replace("d_a_m_n".casefold(),"||d.a.m.n||")
                m=m.replace("s_h_i_t".casefold(),"||s.h.i.t||")
                m=m.replace("b_i_t_c_h".casefold(),"||b_i_t_c_h||")
            elif 'ken' in message.content.lower() or 'jay' in message.content.lower() or 'sifu' in message.content.lower():
                
                if message.author.id !=548295233138327583 and message.content.author !=462416556853559306:
                    await message.channel.send(f"Pinging <@462416556853559306>")
            elif 'error' in message.content.lower() or 'admin' in message.content.lower():
                if 'Pinging' not in message.content:
                    await message.channel.send("Let your admin know of the error or message Ken about it")
            if '<@548295233138327583>' in message.content.lower() and 'battle' in message.content.lower():
                await asyncio.sleep(5)
                await message.channel.send('yes')
            elif '<@548295233138327583>' in message.content.lower() and 'battle' not in message.content.lower() and 'duel' not in message.content.lower():
                info="""Tutorial For Blazibot!
        
[1] To start just type -start
[2] You probably want to view it now, don't you? Well just type -i 1
[3] Maybe you want some credits to start your journey, just type -payday
[4] Okay dueling, at this point in time, you are allowed to duel yourself for some easy credits, however, this will get removed later on, dueling others works too, just type -battle @(player's name)
[5] Say you want a specific pokemon to spawn and it wont, just type -spawn (pokemon type) and a pokemon of that typing will spawn
[6] The market works, just items do not
[7] If you want to become a gym leader There are perks There are 5 open spots left, Normal, Steel, Ice, Electric, and Rock. If you dont want to be any of those, but you still wanna be one, you can be the co-leader, you would do the gym if the leader is sleeping or school
[8] Trading is not added yet too
[9] Kensei (the owner if the bot and amazing person) creates little easter eggs ever-now-and-then. He is the only one who knows that the answer is so everyone is racing to solve them. there are nice prizes wink
[10] To learn moves for your battling experiences, type -moveset and -learn (1-4) (move name) and if there is two words in the move name, put a - where the space is. Right now, pokemon moves are based on their type, so say I had a pikachu, that pikachu would be able to learn every electric move."""
                await message.channel.send("```"+info+"```")
        count=self.count
        count=count+1
        self.count=count
        print(str(count))
        mod=rand.randint(2,30)  
        
        if(0==0):
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            c = conn.cursor()
            c.execute(f"Select selected from Players where ID='{message.author.id}'")
            numselected=c.fetchone()
            numselected=str(numselected)
            numselected=numselected[1:-2]
            
            numselected=int(numselected)
           
            c.execute(f"Select poke_id, EXP,level from Owned_Pokes where Owner='{message.author.id}' and ID_Owned={numselected}")
            
            pokeidexp=c.fetchall()
            pokeidexp=str(pokeidexp)
            idexp=pokeidexp.split(',')
            idp=idexp[0]
            exp=idexp[1]
            exp=str(exp)
            lvl = idexp[2]
            lvl=lvl[:-2]
            idp=str(idp)[2:]
            c.execute(f"select Name from pokes where Number={idp}")
            pokename=c.fetchone()
            pokename = str(pokename)
            pokename=pokename[2:-3]
            c.execute(f"select item from Owned_Pokes where Number_Caught={numselected} and Owner= {message.author.id}")
            item=c.fetchone()
            item=str(item)
            c.execute(f"select Equipped from Players where ID= {message.author.id}")
            plitem=c.fetchone()
            plitem=str(plitem)
            
            di=int(lvl)*0.2              
            if int(lvl)<100:
                xpgain=int(lvl)*int(lvl)
                xpgain=xpgain-int(lvl)
                xpgain=xpgain
                xpgain=xpgain +15
                exp=exp[2:-1]
                exp=float(exp)
                if 'Lucky-egg' in item:
                    xpgain=xpgain*1.5
                
                if 'Motor' in plitem:
                    xpgain=xpgain*4.0
                
                elif 'Bike' in plitem:
                    xpgain=xpgain*2.0
                else:
                    xpgain=xpgain*1.0
                
                totalxp=int(xpgain+exp)
                if xpgain<1 or totalxp<1:
                    totalxp=15
                c.execute(f"update Owned_Pokes set EXP='{str(totalxp)}' where Owner='{message.author.id}' and ID_Owned={numselected}")
                conn.commit()
            
            c.execute(f"select experience from explv  where level='{lvl}' ")
            maxexp=c.fetchone()
            maxexp=str(maxexp)
            maxexp=maxexp[1:-1]
            maxexp=str(maxexp).strip("(").strip("'").strip(",")
            c.execute(f"Select EXP from Owned_Pokes where Owner='{message.author.id}' and ID_Owned={numselected}")
            totalexp=c.fetchone()
            totalexp=str(totalexp)[2:-3]
            t=int(totalexp)
            m= int(maxexp)
            if t>m:
                await message.channel.send(f"Your pokemon grew to {int(lvl)+1}")
                
                
                c.execute(f"update Owned_Pokes set EXP='0' where Owner='{message.author.id}'")
                conn.commit()
                c.execute(f"update Owned_Pokes set level='{int(lvl)+1}' where Owner='{message.author.id}' and ID_Owned={numselected};")
                conn.commit()
                lvl=int(lvl)+1
                if(lvl==5):
                    await message.channel.send("It hatched!")
            else:
                "do nothing"
            nu='#'+str(numselected)
            print(lvl)
            c.execute(f"select level from evos where pokemon ='{pokename}'")
            minevo=c.fetchone()
            minevo=str(minevo)
            minevo=str(minevo)[:-1]
            minevo=minevo[1:-1]
            minevo=str(minevo)
            print('min evo'+ minevo)
            if "o" in minevo:
                print('No evolution')
            else:
                "do nothing"
            if minevo.isdigit()==False:
                x='o'
            
            else:
                
               
                level=int(lvl)
                evo=str(minevo)            
                if(level>int(evo) and evo.isdigit()==True):
               
                    newnum=int(idp)
                    newnum = newnum+1
                
                    print(newnum)
                    c.execute(f"update Owned_Pokes set poke_id={newnum} where Owner='{message.author.id}' and ID_Owned={numselected};")
                    conn.commit()
                    await message.channel.send(f"Your {pokename} evolved!") 
                    c.close()
                else:
                    "do nothing"
       
        if(count==mod):
            sp=rand.randint(-17,809)       
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')
            Shiny='False'
            legends=[144,145,146,150,151,243,244,245,249,250,251,377,378,379,380,381,382,383,384,385,386,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,638,639,640,641,642,643,644,645,646,647,648,649]
            rate=rand.randint(0,1000)
            c = conn.cursor()
            c.execute(f"SELECT Name FROM Pokes WHERE number={sp}")
            if rate==0:
                dsp=str(sp)+"-shiny"
                Shiny='True'
            else:
                dsp=sp
            rate2=rand.randint(0,33)
            c.execute(f"select selected from Players where ID={message.author.id}")
            selected=c.fetchone()
            selected=str(selected)
            selected=selected[1:-2]
            c.execute(f"select item from Owned_Pokes where Owner={message.author.id} and Number_Caught={selected}")
            items=c.fetchone()
            items=str(items)
            if 'Honey' in items or 'honey' in items:
                legends=[-234567890]
            else:
                legends=[144,145,146,150,151,243,244,245,249,250,251,377,378,379,380,381,382,383,384,385,386,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,638,639,640,641,642,643,644,645,646,647,648,649]
            if sp in legends:
                rate2=rand.randint(0,1000)            
                if rate2==0:
                    sp=sp
                else:
                    randch=rand.randint(0,10)
                    if '-shiny' in str(dsp):
                        sp=int(dsp.replace('-shiny',''))+randch
                        sp=str(sp)+"-shiny"
                    else:
                        sp=sp+randch
            else:
                sp=sp
                
            c = conn.cursor()
            c.execute(f"SELECT Name FROM Pokes WHERE number={sp}")
            randName=c.fetchone()
            randompoke=(", ".join(randName))
            
            poke=str(randompoke)
            if "Mega" in randompoke:
                randompoke=randompoke.replace("Mega-","")
                randompoke=randompoke.replace("-Y","")
                randompoke=randompoke.replace("-y","")
                randompoke=randompoke.replace("-X","")
                randompoke=randompoke.replace("-x","")
                c.execute(f"SELECT Number FROM Pokes WHERE Name={randompoke}")
                sp=c.fetchone()
                sp=str(sp)
                sp=sp[1:-2]
            
            embed = discord.Embed(title="Random Spawns", description="Random Spawn", color=0x00ff00)
            
            embed.set_image(url=f"http://157.245.8.88/html/dex/media/pokemon/sugimori/{str(sp)}.png")
            
            embed.add_field(name="Catch:", value="Say the Pokemon's name to catch it!!", inline=False)
            c.execute(f"select redirect_channel from redirects where channel_id={int(message.channel.id)}")
            redirects=c.fetchone()
            redirect=str(redirects)
            
            if 'on' in redirect:
                chan=message.channel
                await chan.send(embed=embed)
            else:
                chan=message.guild.get_channel(int(redirect[1:-2]))
                await chan.send(embed=embed)
            tries=0
                         
            catchtry = await self.bot.wait_for("message",timeout=1300)
            conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db')        
            c = conn.cursor()
            c.execute(f"SELECT ID from Players where ID='{message.author.id}'")
            exists=c.fetchone()
            exists=str(exists)
            if('o' in exists):
                await chan.send("Go see Oak First with -start!")
            else:
                
                tries=0
                c.execute(f"select name from items where Owner={catchtry.author.id}")
                items=c.fetchall()
                items=str(items)
                items=items.replace("(","")
                items=items.replace(")","")
                items=items.replace("[","")
                items=items.replace("]","")
                items=items.replace(",,",",")
                while catchtry.content.casefold().capitalize()!=randompoke.casefold().capitalize() and tries<6:
                       catchtry = await self.bot.wait_for("message",timeout=1300)
                       if catchtry.channel == chan:
                            
                            tries=tries+1
                if(catchtry.content.casefold().capitalize() in randompoke.casefold().capitalize()):
                    if(catchtry.author.id!=548295233138327583):              
                        if(tries<6):
                                await chan.send(f"<@{catchtry.author.id}> is fighting the {randompoke}")
                            
                                level=rand.randint(5,75)
                                hp=rand.randint(0,31)
                                atk=rand.randint(0,31)
                                df=rand.randint(0,31)
                                sp_atk=rand.randint(0,31)
                                sp_def=rand.randint(0,31)
                                speed=rand.randint(0,31)
                                conn = sqlite3.connect('/home/kensei/Desktop/blazi/blazedb.db') 
                                c = conn.cursor()
                                c.execute(f"SELECT Number_Caught FROM Owned_Pokes WHERE owner='{catchtry.author.id}'")                        
                                numberofpokes=c.fetchall()
                                numberofpokes=str(numberofpokes)
                                numberofpokes=numberofpokes.replace("(","")
                                numberofpokes=numberofpokes.replace(")","")
                                numberofpokes=numberofpokes.replace("[","")
                                numberofpokes=numberofpokes.replace("]","")
                                numberofpokes=numberofpokes.replace(",,",",")
                                
                                pokesl=numberofpokes.split(',')
                                
                                noofpokes=len(pokesl)
                                newnumberofpokes=noofpokes+1
                                              
                                gender=rand.randint(0,1)
                                if(gender==0):
                                    pickedg="Male"
                                else:
                                    pickedg="Female"
                                c = conn.cursor()
                                c.execute(f"select nature from natures")
                                allnatures=c.fetchall()
                                allnatures=str(allnatures)
                                allnatures=allnatures.replace("[","")
                                allnatures=allnatures.replace("]","")
                                allnatures=allnatures.replace("(","")
                                allnatures=allnatures.replace(")","")
                                allnatures=allnatures.replace(",,",",")
                                naturelist=allnatures.split(',')
                                natlen=len(naturelist)
                                randnat=rand.randint(0,natlen-1)
                                nature=naturelist[randnat]
                                nature=nature.replace("'","")
                                nature=nature.replace(" ","")
                                if ',' in nature:
                                    nature='Jolly'
                                c.execute(f"select ability from abilities where poke like '%{sp}%'")
                                                                
                                abilitylist=c.fetchall()
                                abilitylist=str(abilitylist)
                                abilitylist=abilitylist.replace(")","")
                                abilitylist=abilitylist.replace("(","")
                                abilitylist=abilitylist.replace("]","")
                                abilitylist=abilitylist.replace("[","")
                                abilitylist=abilitylist.replace("'","")
                                abilitylist=abilitylist.replace(",,",",")
                                abilities=abilitylist.split(',')
                                abilitylen=len(abilities)
                                if abilitylen>2:
                                    randabil=rand.randint(0,abilitylen-1)
                                    ability=abilities[randabil]
                                
                                else:
                                    ability="none"
                                
                                c.execute(f"INSERT into Owned_Pokes(ID_Owned , poke_id , level , Number_Caught , HP , Atk , Def , Sp_Atk , Sp_Def , Speed , Ev1 , Ev2 , Ev3 , Ev4 , Ev5 , Ev6 , FORM , Owner,EXP,move1,move2,move3,move4,gender,item,Nature,shiny,ability) VALUES({newnumberofpokes-1},{int(sp)},{int(level)},{int(newnumberofpokes-1)},{hp},{atk},{df},{sp_atk},{sp_def},{speed},0,0,0,0,0,0,0,{catchtry.author.id},0,'','','','','{pickedg}','None','{nature}','{Shiny}','{ability}');");
                                conn.commit()
                            
                                await chan.send("You caught it")
                            
                                c.close()
                        elif(tries>=6):
                                await chan.send("it fled!")
                    else:
                        "keep going"
        elif(count>mod):
            self.count=0
        c.close()
def setup(bot):
    bot.add_cog(blaze(bot))
