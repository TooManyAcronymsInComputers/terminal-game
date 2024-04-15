import datetime
from utils import *

class player:
    def __init__(self, Health, Mp, Xp, Lvl, Defence, Damage):
        self.Health = Health
        self.Mp = Mp
        self.Xp = Xp
        self.Lvl = Lvl
        self.Defence = Defence
        self.Damage = Damage

def loadSave():
    from playerstats import player_health
    from playerstats import player_mp  
    from playerstats import player_xp 
    from playerstats import player_lvl   
    from playerstats import player_defence
    from playerstats import player_damage

    ps = player(player_health, player_mp, player_xp, player_lvl, player_defence, player_damage)

    return ps

def saveFunction(playerStats):

    phs = "player_health = " + str(playerStats.Health) +"\n"
    pms = "player_mp = " + str(playerStats.Mp) +"\n"
    pxs = "player_xp = " + str(playerStats.Xp) +"\n"
    pls = "player_lvl = " + str(playerStats.Lvl) +"\n"
    pdes = "player_defence = " + str(playerStats.Defence) +"\n"
    pdas = "player_damage = " + str(playerStats.Damage) +"\n"

    now = datetime.datetime.now()
    formatted = now.strftime("%A, %d %B, %Y %H:%M:%S")
    ls = "last_save = " + "str('" + formatted + "')" +"\n"

    now = datetime.datetime.now()
    formatted = now.strftime("%A, %d %B, %Y %H:%M:%S")
    from playerstats import last_save
    print("last time saved | ", last_save)
    print("do you wish to save?\n [y/n]")
    
    userInput = getchar()

    if userInput == ('n'):
        print("Exiting without saving.")
    elif userInput == ('y'):
        print("saving...")
        f = open("playerstats.py", "w")
        f.write(phs)
        f.write(pms)
        f.write(pxs)
        f.write(pls)
        f.write(pdes)
        f.write(pdas)
        f.write(ls)
        f.close()