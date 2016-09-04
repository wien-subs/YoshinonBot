import ch
import time
from time import strftime
import random
import re
import binascii
import datetime
import os
import sys
import urllib
import json
import http.client
import pymysql
import youtube
from datetime import timedelta
from time import gmtime, strftime
#replyes
sword = [" scoate sabia din teca si aplica o lovitura critica pe ", " prinde sabia cu două mâini si o trece prin armura lui ", " aruncă sabia și scoate cele două pumnale pe care le învige în "]
swordfinal = [" scoate sabia și il decapitează pe ", " ridica sabia și îl despică pe "]
mage = [" ridică bagheta rosteste două vraji și il ametește pe ", " invoacă doi demoni care il rănesc pe "]
magefinal = [" scoate CODEX-ul și cheama un meteorit asupra lui ", " ridică bagheta și o înfige in capul lui "]
archer = [" scoate o sâgeată otrăvită și o înfige in coapsa lui ", " lansează clasica ploaie de săgeți asupra lui "]
archerfinal = [" scoate o sâgeată din tolbă și o infige in capul lui ", " foloseste arcul ca să il ștranguleze pe "]
#Defines
def getuserid(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        return row[0]
    else:
        return 0
def getmoneybank(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        value = row[11]
        return value
    else:
        return 0
def getmoney(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        value = row[2]
        return value
    else:
        return 0
def getWin(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
        row = sql.fetchone()
        return row[9]
    else:
        return False
def getBattle(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
        row = sql.fetchone()
        return row[8]
    else:
        return False
def getLose(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
        row = sql.fetchone()
        return row[10]
        sql.close()
        conn.close()
    else:
        return False
        sql.close()
        conn.close()
def isbl(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `blacklist` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        return True
        sql.close()
        conn.close()
    else:
        return False
        sql.close()
        conn.close()
def addbl(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(isbl(user)):
        return False
        sql.close()
        conn.close()
    else:
        sql.execute("INSERT INTO `blacklist` (`user`) values('"+format(user)+"')")
        conn.commit()
        return True
        sql.close()
        conn.close()
def removebl(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(isbl(user)):
        sql.execute("DELETE FROM `blacklist` WHERE `user`='"+format(user)+"'")
        conn.commit()
        return True
        sql.close()
        conn.close()
    else:
        return False
        sql.close()
        conn.close()
#define Shits
def userexist(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        sql.close()
        conn.close()
        return True
    else:
        sql.close()
        conn.close()
        return False
def haveinv(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
    if(sql.rowcount == 1):
        sql.close()
        conn.close()
        return True
    else:
        sql.close()
        conn.close()
        return False
def haveavatar(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
    if(sql.rowcount == 1):
        row = sql.fetchone()
        if(row[12] == "no"):
            return False
            sql.close()
            conn.close()
        else:
            sql.close()
            conn.close()
            return True
    else:
        sql.close()
        conn.close()
        return False
def emptyslot(user, slot):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
    if(sql.rowcount == 1):
        row = sql.fetchone()
        if(slot.isdecimal()):
            slot = int(slot)
            if(row[slot] == "empty"):
                sql.close()
                conn.close()
                return True
            else:
                sql.close()
                conn.close()
                return False
        else:
            sql.close()
            conn.close()
            return False
    else:
        sql.close()
        conn.close()
        return False
def getAccessPower(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        access = int(row[3])
        if(access == 5):
            access = "Owner"
            return access
        elif(access == 4):
            access = "Admin"
            return access
        elif(access == 3):
            access = "Moderator"
            return access
        elif(access == 2):
            access = "V.I.P."
            return access
        else:
            access = "User"
            return access
    else:
        access = "Nu l-am gait pe "+user
        return access
    sql.close()
    conn.close()
def getAccess(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        access = int(row[3])
        return access
    else:
        return 0
    sql.close()
    conn.close()
def setmoney(user, money):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(userexist(user)):
        sql.execute("UPDATE `userdata` SET `money`="+format(money)+" where `user`='"+user+"'")
        conn.commit()
        sql.close()
        conn.close()
    else:
        room.message("Nu te cunosc! Dispari!")
def class2num(value):
    if(value == "mage"):
        return 1
    elif(value == "swordman"):
        return 2
    elif(value == "archer"):
        return 3
    else:
        return False
def num2class(value):
    if(value == 1):
        return "mage"
    elif(value == 2):
        return "swordman"
    elif(value == 3):
        return "archer"
    else:
        return False
def getbasehp(value):
    if(value == 1):
        return 50
    elif(value == 2):
        return 100
    else:
        return 75
def getbasedmg(value):
    if(value == 1):
        return 15
    elif(value == 2):
        return 5
    else:
        return 10
def recalc(clas, level, user):
    if(clas == 1):
        level = int(level)
        hp = int(getbasehp(1)) + (level * 3) + (level / 2)
        hp = int(hp)
        dmg = int(getbasedmg(1)) + level + (level / 2)
        dmg = int(dmg)
        print(format(dmg)+" dmg|hp "+format(hp))
        #HP
        conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
        sql = conn.cursor()
        sql.execute("UPDATE `inventory` SET `hp`="+format(hp)+" where `userid`="+format(getuserid(user)))
        conn.commit()
        #DMG
        sql.execute("UPDATE `inventory` SET `power`="+format(dmg)+" where `userid`="+format(getuserid(user)))
        conn.commit()
        sql.close()
        conn.close()
    if(clas == 2):
        level = int(level)
        hp = int(getbasehp(2)) + (level * 3) + (level / 2)
        hp = int(hp)
        dmg = int(getbasedmg(2)) + level + (level / 2)
        dmg = int(dmg)
        print(format(dmg)+" dmg|hp "+format(hp))
        #HP
        conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
        sql = conn.cursor()
        sql.execute("UPDATE `inventory` SET `hp`="+format(hp)+" where `userid`="+format(getuserid(user)))
        conn.commit()
        #DMG
        sql.execute("UPDATE `inventory` SET `power`="+format(dmg)+" where `userid`="+format(getuserid(user)))
        conn.commit()
        sql.close()
        conn.close()
    if(clas == 3):
        level = int(level)
        hp = int(getbasehp(3)) + (level * 3) + (level / 2)
        hp = int(hp)
        dmg = int(getbasedmg(3)) + level + (level / 2)
        dmg = int(dmg)
        print(format(dmg)+" dmg|hp "+format(hp))
        #HP
        conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
        sql = conn.cursor()
        sql.execute("UPDATE `inventory` SET `hp`="+format(hp)+" where `userid`="+format(getuserid(user)))
        conn.commit()
        #DMG
        sql.execute("UPDATE `inventory` SET `power`="+format(dmg)+" where `userid`="+format(getuserid(user)))
        conn.commit()
        sql.close()
        conn.close()
def sethp(user, hp):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("UPDATE `inventory` SET `hp`="+format(hp)+" where `userid`="+format(getuserid(user)))
    conn.commit()
    sql.close()
    conn.close()
def setdmg(user, dmg):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("UPDATE `inventory` SET `power`="+format(dmg)+" where `userid`="+format(getuserid(user)))
    conn.commit()
    sql.close()
    conn.close()
def setlevel(user, level):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("UPDATE `inventory` SET `level`="+format(level)+" where `userid`="+format(getuserid(user)))
    conn.commit()
    sql.close()
    conn.close()
def getAvatarName(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
    if(sql.rowcount == 1):
        row = sql.fetchone()
        if(row[12] == "no"):
            return False
            sql.close()
            conn.close()
        else:
            sql.close()
            conn.close()
            return row[12]
    else:
        sql.close()
        conn.close()
        return False
def lvlreq(level):
    xpreq = 100 * (level+1**2.3)
    return xpreq
def getAvatarPower(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
        row = sql.fetchone()
        return row[16]
    else:
        return False
def getAvatarHP(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
        row = sql.fetchone()
        return row[17]
    else:
        return False
def getAvatarLevel(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
        row = sql.fetchone()
        return row[13]
    else:
        return False
def getAvatarXP(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
        row = sql.fetchone()
        return row[14]
    else:
        return False
def getAvatarClass(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
        row = sql.fetchone()
        return row[15]
    else:
        return False
def getAvatarBonus(user):
    if(haveavatar(user)):
        if(getAvatarClass(user) == 1):
            bonus = int(getAvatarPower(user)) + int(getAvatarLevel(user))
            return int(bonus)
        if(getAvatarClass(user) == 2):
            bonus = (int(getAvatarPower(user)) + int(getAvatarLevel(user)))/3
            return int(bonus)
        if(getAvatarClass(user) == 3):
            bonus = (int(getAvatarPower(user)) + int(getAvatarLevel(user)))/2
            return int(bonus)
    else:
        return False
def giveAvatarXP(user, value):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    clas = int(getAvatarClass(user))
    actual = int(getAvatarXP(user))
    value = int(value)
    update = int(actual + value)
    level = int(getAvatarLevel(user))
    xpreq = int(lvlreq(level))
    if(update < xpreq):
        sql.execute("UPDATE `inventory` SET `xp`="+format(update)+" where `userid`='"+format(getuserid(user))+"'")
        conn.commit()
        sql.close()
        conn.close()
        return False
    else:
        level = level + 1
        recalc(clas, level, user)
        sql.execute("UPDATE `inventory` SET `level`="+format(level)+" where `userid`='"+format(getuserid(user))+"'")
        conn.commit()
        sql.close()
        conn.close()
        return True
def addWin(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    win = int(getWin(user)) + 1
    battle = int(getBattle(user)) + 1
    sql.execute("UPDATE `userdata` SET `battle`="+format(battle)+", `win`="+format(win)+" where `user`='"+format(user)+"'")
    conn.commit()
    sql.close()
    conn.close()
def addLose(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    lose = int(getLose(user)) + 1
    battle = int(getBattle(user)) + 1
    sql.execute("UPDATE `userdata` SET `battle`="+format(battle)+", `lose`="+format(lose)+" where `user`='"+format(user)+"'")
    conn.commit()
    sql.close()
    conn.close()
def addBatttle(user):
    conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
    sql = conn.cursor()
    battle = int(getBattle(user)) + 1
    sql.execute("UPDATE `userdata` SET `battle`="+format(battle)+" where `user`='"+format(user)+"'")
    sql.commit()
    sql.close()
    conn.close()
    ##

class bot(ch.RoomManager):
    def onInit(self):
        self.setNameColor("d20000")
        self.setFontColor("5e4035")
        self.setFontFace("Typewriter")
        self.setFontSize(12)
        self.enableBg()
        self.enableRecording()

    def onJoin(self, room, user, puid):
        conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
        sql = conn.cursor()
        sql.execute("select * from `userdata` where `user`='"+ user.name +"'")
        print(user.name+" | "+puid)
        if(sql.rowcount < 1):
            timefmo = format(datetime.datetime.now().replace(microsecond=0))
            ntime = format(int(time.time()))
            sql.execute("insert into `userdata` (`user`, `money`, `firstjoin`, `lastmoney`) values ('"+ user.name +"', 20,'"+ timefmo +"', "+ntime+")")
            conn.commit()
            room.message(user.name +" ai primit 20 belly")
        sql.close()
        conn.close()

    def onConnect(self, room):
        print("Connected to "+room.name)
        room.message("I'm back online!")

    def onReconnect(self, room):
        print("Reconnected")

    def onMessage(self, room, user, message):
        prefix = "/"
        self.safePrint(user.name + ': ' + message.body)
        if(isbl(user.name)):
            msgdata = "False"
        else:
            msgdata = message.body.split(" ",1)
        if len(msgdata) > 1:
            cmd, args = msgdata[0], msgdata[1]
        else:
            cmd, args = msgdata[0],""
        cmd=cmd.lower()
        if cmd=="/recalc":
            if(getAccess(user.name) > 1):
                clas = getAvatarClass(user.name)
                level = getAvatarLevel(user.name)
                recalc(clas, level, user.name)
                room.deleteUser(ch.User(user.name))
                room.message("Recalculated!")
            else:
                room.deleteUser(ch.User(user.name))
                room.message("Access insuficent!")
        elif cmd=="/rec" or cmd=="/reconnect":
            if(getAccess(user.name) > 3):
                room.deleteUser(ch.User(user.name))
                room.reconnect()
                room.message("Attemp to reconnect ... <br/> Open Shocket ... [OK] <br/> Enabling SSL ... [OK] <br/> Reconnection to SQLServer ... [OK] <br/> Enabling SHH ... [FAILED] <br/> Reconnected successfully!", True)
            else:
                room.deleteUser(ch.User(user.name))
                room.message("Nu ai suficent access")
        elif cmd=="/avatar" or cmd=="/minion":
            if(userexist(user.name) and haveavatar(user.name)):
                args = args.lower()
                ar = args.split(" ", 1)
                if(len(ar) > 0):
                    if(ar[0] == "status" or ar[0] == "info" or ar[0] == "stats"):
                        name = getAvatarName(user.name)
                        level = getAvatarLevel(user.name)
                        clas = getAvatarClass(user.name)
                        xpreq = lvlreq(level)
                        xp = getAvatarXP(user.name)
                        win = getWin(user.name)
                        lose = getLose(user.name)
                        room.message("====Avatar====<br/>"+"Nume: "+format(name)+"<br/> Level: "+format(level)+"<br/> XP: "+format(xp)+"/"+format(xpreq)+"<br/> Class: "+format(num2class(clas))+"<br/> Win: "+format(win)+"<br/> Lose:"+format(lose), True)
                    else:
                        room.message("Utilizare corecta: /avatar status/evolv, "+ar[0]+" nu se afla printre acestea :(")
                else:
                    room.message("Utilizare corecta: /avatar status/evolv")
            else:
                room.message("Nu ai un avatar, foloseste /create pentru a crea unul")
        elif cmd=="$bl" or cmd=="$blacklist":
            if(getAccess(user.name) > 2):
                args = args.lower()
                ar = args.split(" ", 2)
                if(len(ar) > 1):
                    if(ar[0] == "add" or ar[0] == "adauga"):
                        if(userexist(ar[1])):
                            if(getAccess(ar[1]) < 3):
                                if(isbl(ar[1])):
                                    room.message("Utilizatorul se afla deja in blacklist")
                                    room.deleteUser(ch.User(user.name))
                                else:
                                    addbl(ar[1])
                                    room.message("Utilizatorul <b>"+format(ar[1])+"</b> a fost adaugat in blacklist", True)
                                    room.deleteUser(ch.User(user.name))
                            else:
                                room.message("Nu ai cum sa adaugi un moderator in blacklist")
                                room.deleteUser(ch.User(user.name))
                        else:
                            room.message("Nu am gasit nici un utilizator")
                    elif(ar[0] == "remove" or ar[0] == "rm" or ar[0] == "sterge"):
                        if(userexist(ar[1]) and isbl(ar[1])):
                            removebl(ar[1])
                            room.message("Utilizatorul <b>"+format(ar[1])+"</b> a fost sters din blacklist", True)
                            room.deleteUser(ch.User(user.name))
                        else:
                            room.message("Nu am gasit utilizatorul sau este deja in blacklist")
                            room.deleteUser(ch.User(user.name))
                    else:
                        room.message("Utilizare corecta <b> /blacklist add/remove utilizator </b>", True)
                else:
                    room.message("Utilizare corecta <b> /blacklist add/remove utilizator </b>", True)
            else:
                room.message("Nu te ascult pe tine :(")
        elif cmd=="/slap" or cmd=="/slap":
            args=args.lower()
            if(len(args) > 2):
                ar = args[0:].split(" ", 1)
                arg = ar[0]
                if(len(ar[0]) > 1):
                    if(arg=="bot" or arg=="yoshinonbot" or arg=="yoshinon"):
                        if(getAccess(user.name) > 1):
                            slap = random.choice(["De ce mă lovești! Incetează! mă doare ;(", "Te rog loveste-mă mai cu milă ;(", "Nuuu mai da! Te ROGG!!!!!"])
                            random.choice(slap)
                        else:
                            room.message("Haha! Buna incercare! Yoshinon îi trage o palmă lui @"+user.name.capitalize())
                    else:
                        room.deleteUser(ch.User(user.name))
                        self.pm.message(ch.RoomManager(args),"Utilizatorul "+user.name.capitalize()+" te cauta pe http://"+room.name+".chatango.com ")
                        self.pm.message(ch.RoomManager(args),"Regard YoshinonBot [at] http://www.wien-subs.ro")
                        slap = random.choice([user.name.capitalize()+" ia tras o oltenească lui @"+ar[0].capitalize()+" de la luat mama dracu", user.name.capitalize()+" la lovit pe @"+ar[0].capitalize()+" cu o balenă", user.name.capitalize()+" ia tras un pumn lui @"+ar[0].capitalize()+" [K.O.]", user.name.capitalize()+" la lovit pe @"+ar[0].capitalize()+" cu o bucata de pizza", user.name.capitalize()+" ia tras un sut lui @"+ar[0].capitalize()+" de la trimis in China"])
                        room.message(slap)
                else:
                    room.message("Utilizare corecta /slap utilizator")
            else:
                room.message("Utilizare corecta /slap utilizator")
        elif cmd=="/duel" or cmd=="/lupta" or cmd=="/pvp" or cmd=="/taunt":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            ar = message.body
            if(userexist(user.name) and haveavatar(user.name)):
                data = ar.split(" ", 1)
                if(len(data) == 2):
                    if(userexist(data[1]) and haveavatar(data[1])):
                        if(user.name == data[1]):
                            room.message("For Fuck's Sake [!] Nu te poti sinucide :(")
                        else:
                            oneHP = int(getAvatarHP(user.name))
                            onePower = int(getAvatarPower(user.name))
                            oneLevel = int(getAvatarLevel(user.name))
                            twoHP = int(getAvatarHP(data[1]))
                            twoPower = int(getAvatarPower(data[1]))
                            twoLevel = int(getAvatarLevel(data[1]))
                            oneB = int(getAvatarBonus(user.name))
                            twoB = int(getAvatarBonus(data[1]))
                            runde = 0
                            while(oneHP > 0 or twoHP > 0):
                                lucky = int(random.choice([1,1,1,0,0,0,0,0]))
                                oneHP = oneHP - (twoPower*lucky + twoLevel/10 + oneB)
                                lucky = int(random.choice([1,1,1,0,0,0,0,0]))
                                twoHP = twoHP - (onePower*lucky + oneLevel/10 + twoB)
                                runde = runde + 1
                            if(oneHP == twoHP): #draw
                                addBatttle(user.name)
                                addBatttle(data[1])
                                xp = (runde*5)+ (oneB + twoB)/2
                                giveAvatarXP(user.name, int(xp))
                                room.message("Remiza! Ambi participatni au primit <b>"+format(int(xp))+"</b> XP", True)
                                self.pm.message(ch.RoomManager(data[1]), "Campionul tau "+getAvatarName(data[1])+" a fost provocat de "+getAvatarName(user.name)+"("+user.name+") si a fost remiză")
                            elif(oneHP > twoHP): #Primul #Provocatorul
                                addWin(user.name)
                                addLose(data[1])
                                onebani = int(getmoney(user.name))
                                twobani = int(getmoney(data[1]))
                                furt = int(twobani*0.08)
                                onebani = onebani + furt
                                twobani = twobani - furt
                                setmoney(user.name, onebani)
                                setmoney(data[1], twobani)
                                oxp = (runde*5)+ (oneB + twoB)
                                txp = ((runde*5)+ (oneB + twoB))/2
                                giveAvatarXP(user.name, int(oxp))
                                giveAvatarXP(data[1], int(txp))
                                room.message("<b>"+format(getAvatarName(user.name))+"</b> la invins pe <b>"+format(getAvatarName(data[1]))+"</b> si a primit "+format(furt)+" Belly",True)
                                room.message("<b>"+format(getAvatarName(user.name))+"</b> + "+format(int(oxp))+" | "+format(getAvatarName(data[1]))+" + "+format(int(txp))+ " au primit experianta", True)
                                self.pm.message(ch.RoomManager(data[1]), "Campionul tau "+getAvatarName(data[1])+" a fost provocat de "+getAvatarName(user.name)+"("+user.name+") si a fost învins")
                            else: #Doi # Provocatul
                                addWin(data[1])
                                addLose(user.name)
                                onebani = int(getmoney(user.name))
                                twobani = int(getmoney(data[1]))
                                furt = int(onebani*0.08)
                                onebani = onebani - furt
                                twobani = twobani + furt
                                setmoney(user.name, onebani)
                                setmoney(data[1], twobani)
                                oxp = (runde*5)+ (oneB + twoB)/4
                                txp = ((runde*5)+ (oneB + twoB))
                                giveAvatarXP(user.name, int(oxp))
                                giveAvatarXP(data[1], int(txp))
                                room.message("<b>"+format(getAvatarName(data[1]))+"</b> la invins pe <b>"+format(getAvatarName(user.name))+"</b> si a primit "+format(furt)+" Belly",True)
                                room.message("<b>"+format(getAvatarName(data[1]))+"</b> + "+format(int(txp))+" si "+format(getAvatarName(user.name))+" + "+format(int(oxp))+ " au primit experianta", True)
                                self.pm.message(ch.RoomManager(data[1]), "Campionul tau "+getAvatarName(data[1])+" a fost provocat de "+getAvatarName(user.name)+"("+user.name+") si a la învins")
                    else:
                        room.message("Uilizatorul nu exista sau nu are avatar.")
                else:
                    room.message("Utilizare corecta /duel utilizator")
            else:
                room.message("Trebuie sa ai avatar pentru a te duela!")                        
        elif cmd=="/create" or cmd=="/make":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            args=message.body
            if(userexist(user.name)):
                ar = args.split(" ", 2)
                print(ar)
                if(args == "/create" or args=="/make"):
                    room.message("Folosire corecta /make inv/avatar clasa nume")
                else:
                    if(ar[1] == "inventory" or ar[1] == "inv"):
                        if(haveinv(user.name) == False):
                            money = getmoney(user.name)
                            if(money > 499):
                                money = money - 500
                                setmoney(user.name, money)
                                print(format(getuserid(user.name)))
                                sql.execute("INSERT INTO `inventory` (`userid`) VALUES ("+format(getuserid(user.name))+")")
                                conn.commit()
                                sql.close()
                                conn.close()
                                room.message("@"+user.name+" Ti-am creeat inventarul! Il poti accesa cu comanda /inv")
                            else:
                                room.message("Trebuie sa ai cel putin 500 belly pentru a creea inventarul.")
                        else:
                            room.message("Ai deja un inventar. /inv")
                    elif(ar[1] == "avatar"):
                        if(haveinv(user.name)):
                            if(haveavatar(user.name) == False):
                                if(len(ar) > 1):
                                    ars = args.split(" ", 3)
                                    if(len(ars) > 3):
                                        if(haveavatar(user.name) == False):
                                            if(len(ars[3]) > 2):
                                                if(class2num(ars[2]) == False):
                                                    room.message("Folosire corecta /create avatar [mage/swordman/archer] nume")
                                                else:
                                                    value = class2num(ars[2])
                                                    #print("UPDATE `inventory` SET `avatar`='"+ars[3]+"', `power`='"+format(getbasedmg(value))+"', `hp`='"+format(getbasehp(value))+"', `level`='1', `class`='"+format(value)+"',  where `userid`="+format(getuserid(user.name)))
                                                    sql.execute("UPDATE `inventory` SET `avatar`='"+ars[3]+"', `power`='"+format(getbasedmg(value))+"', `hp`='"+format(getbasehp(value))+"', `level`='1', `class`='"+format(value)+"'  where `userid`="+format(getuserid(user.name)))
                                                    conn.commit()
                                                    room.message("Felicitari! Ai creat <b>"+ars[3]+"</b> cu clasa de <b>"+ars[2]+"</b>", True)
                                            else:
                                                room.message("Folosire corecta /create avatar [mage/swordman/archer] nume")
                                        else:
                                            room.message("Ai deja un avatar :( "+"["+getAccessLevel(user.name)+"] "+getAvatarName(user.name)+" ["+num2class(getAvatarClass(user.name))+"]")
                                    else:
                                        room.message("Folosire corecta /create avatar [mage/swordman/archer] nume")
                                else:
                                    room.message("Folosire corecta /create avatar [mage/swordman/archer] nume")
                            else:
                                room.message("Ai deja un avatar :( "+"[Lv. "+format(getAvatarLevel(user.name))+"] "+getAvatarName(user.name)+" ["+num2class(getAvatarClass(user.name))+"]")
                        else:
                            room.message("Nu ai un inventar. Foloseste /create inv")
                    else:
                        room.message("Nu inteleg ce vrei sa spui :(")
            else:
                room.message("Nu te cunosc! Inregistreaza-te!")
        elif cmd=="/topbank" or cmd=="/tb":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            sql.execute("select * from `userdata` order by `bank` desc limit 10")
            lista=[]
            c = 0
            row = sql.fetchone()
            text = "<b><u>Topul Bogatilor [BANK]</u></b> <br/>"
            lista.append(text)
            while row is not None:
                uuser = row[1]
                coin = row[11]
                coin = format(coin)
                c = c + 1
                text="["+format(c)+"] <b>"+uuser+"</b> cu <b>"+coin+"</b> belly<br/>"
                lista.append(text)
                row = sql.fetchone()
            room.message("".join(lista), True)
            sql.close()
            conn.close()
        elif cmd=="/bank" or cmd=="/banca":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            sql.execute("select * from `userdata` where `user`='"+user.name+"'")
            args=message.body
            if(userexist(user.name)):
                ar = args.split(" ", 2)
                if(len(ar) > 1):
                    if(len(ar[0]) > 1 and len(ar[1]) > 1):
                        if(ar[1] == "baga" or ar[1] == "add"):
                            value = ar[2]
                            if(value.isdigit()):
                                value = int(value)
                                if(value > 0):
                                    if(getmoney(user.name) >= value):
                                        money = int(getmoney(user.name))
                                        money = money - value
                                        bank = int(getmoneybank(user.name))
                                        bank = bank + value
                                        sql.execute("UPDATE `userdata` SET `money`="+format(money)+" where user='"+user.name+"'")
                                        conn.commit()
                                        sql.execute("UPDATE `userdata` SET `bank`="+format(bank)+" where user='"+user.name+"'")
                                        conn.commit()
                                        room.message("@"+user.name+", ai depus in banca "+format(value)+" belly, acum ai in banca "+format(bank)+" belly", True)
                                    else:
                                        room.message("Nu ai atata belly :(")
                                else:
                                    room.message("Valoarea trebuie sa fie pozitiva.")
                            else:
                                room.message("Trebuie sa introduci o vloare.")
                        elif(ar[1] == "scoate" or ar[1] == "remove" or ar[1] == "extrage"):
                            value = ar[2]
                            if(value.isdigit()):
                                value = int(value)
                                if(value > 0):
                                    if(getmoneybank(user.name) >= value):
                                        money = int(getmoney(user.name))
                                        bank = int(getmoneybank(user.name))
                                        bank = bank - value
                                        money = money + value
                                        sql.execute("UPDATE `userdata` SET `money`="+format(money)+" where user='"+user.name+"'")
                                        conn.commit()
                                        sql.execute("UPDATE `userdata` SET `bank`="+format(bank)+" where user='"+user.name+"'")
                                        conn.commit()
                                        room.message("@"+user.name+", ai scos din banca "+format(value)+" belly, acum ai in banca "+format(bank)+" belly", True)
                                    else:
                                        room.message("Nu ai atata belly")
                                else:
                                    room.message("Valoarea trebuie sa fie pozitiva")
                            else:
                                room.message("Trebuie sa introduci o valoare")
                        else:
                            room.message("Folosire corecta /bank baga/scoate valoare")
                    else:
                        room.message("Folosire corecta /bank baga/scoate valoare")
                else:
                    bank = getmoneybank(user.name)
                    room.message("@"+user.name+" ai in banca "+format(bank)+" belly")
            else:
                room.message("Nu te cunosc :(  Dispari!")
        elif cmd=="/bet":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            sql.execute("select * from `userdata` where `user`='"+user.name+"'")
            value=args.lower()
            if(sql.rowcount == 1):
                if(value.isdigit()):
                    row = sql.fetchone()
                    belly = int(row[2])
                    value = int(value)
                    if(value < belly):
                        if(value > 0):
                            chance = [5,3,3,2,2,2,0,0,0,0,0,0,0,0]
                            bet = random.choice(chance)
                            if(bet > 0):
                                bet = (value * bet)
                                belly = belly + bet
                                sql.execute("UPDATE `userdata` SET `money`="+format(belly)+" WHERE `user`='"+user.name+"'")
                                conn.commit()
                                room.message("Felicitari! "+user.name+" ai castigat <b>"+format(bet)+"</b><br/> Acum ai : "+format(belly), True)
                            else:
                                belly = belly - value
                                sql.execute("UPDATE `userdata` SET `money`="+format(belly)+" WHERE `user`='"+user.name+"'")
                                conn.commit()
                                room.message("Ai pierdut totul :(")
                        else:
                            room.message("Valorea trebuie sa fie mai mare ca 1")
                    else:
                        room.message("Nu poti paria ceea ce nu ai :(")
                else:
                    room.message("Trebuie sa introduci o valoare pozitiva.")
            else:
                room.message("Nu te cunosc :( ! Dispari!")
        elif cmd=="$clear" or cmd=="$sterge":
            u=user.name.lower()
            if getAccess(u)>=3 or u in room.modnames or u in room.ownername:
                if len(args) > 0:
                    x=args.lower()
                    room.clearUser(ch.User(x))
                    room.message("@%s i-au fost sterse mesajele." % args.capitalize())
                else:
                    room.message("Folosire corecta: /clear numele")
            else:
                room.message("Nu te ascult :( noob's")
        elif cmd=="$setaccess":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            room.deleteUser(ch.User(user.name))
            if getAccess(user.name) > 4:
                args=args.lower()
                if(len(args) > 3):
                    ar = args[0:].split(" ", 1)
                    if(len(ar[0]) > 1 and len(ar[1]) > 0 and len(ar[1]) < 6):
                        user, value = ar[0], ar[1]
                        if(value.isdigit()):
                            sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
                            if(sql.rowcount == 1):
                                sql.execute("update `userdata` set `access`="+format(value)+" where `user`='"+format(user)+"'")
                                conn.commit()
                                room.message("L-am promovat pe "+user+" la nivelul de access "+format(value))
                                sql.close()
                                conn.close()
                            else:
                                room.message("Nul cunosc pe "+user)
                        else:
                            room.message("Access este de la 1 la 4 :(")
                    else:
                        room.message("Utilizara corecta : $setaccess user value")
                else:
                    room.message("Utilizara corecta : $setaccess user value")
            else:
                room.message("Nu ai permisune! :(")
        elif cmd=="/fura" or cmd=="/jefuieste" or cmd=="/asedieaza":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            args=args.lower()
            room.deleteUser(ch.User(user.name))
            sql.execute("SELECT * FROM `userdata` where `user`='"+user.name+"'")
            if(sql.rowcount == 1):
                row = sql.fetchone()
                coin = row[2]
                timedb = int(row[7])
                ntime = int(time.time())
                timecalc = ntime-timedb
                ar = args[0:].split(" ", 1)
                paradatul = ar[0]
                sql.execute("SELECT * FROM `userdata` where `user`='"+paradatul+"'")
                if(sql.rowcount == 1):
                    row = sql.fetchone()
                    hcoin = row[2]
                    ptime = int(row[7])
                    if(hcoin > 9):
                        if(timecalc > 172800):
                            value = random.randint(0,25)
                            steal = hcoin * value / 100
                            steal = int(steal)
                            hcoin = hcoin - steal
                            ptimec = ntime-ptime
                            if(ptimec < 14400):
                                ptime = ptime
                            else:
                                ptimp = ntime + 14400
                            sql.execute("update `userdata` set `money`="+format(hcoin)+", `laststeal`="+format(int(ptime))+" where `user`='"+paradatul+"'")
                            conn.commit()
                            coin = coin + steal
                            sql.execute("update `userdata` set `money`="+format(coin)+", `laststeal`="+format(ntime)+" where `user`='"+user.name+"'")
                            conn.commit()
                            room.message("L-ai pradat pe "+paradatul+" si i-ai furat "+format(steal)+" belly. Acum ai "+format(coin)+" belly <br/> I-am redus timpul lui "+paradatul+" la 2 ore pentru praduire", True)
                        else:
                            ramas = 172800 - timecalc
                            m, s = divmod(ramas, 60)
                            h, m = divmod(m, 60)
                            d, h = divmod(h, 24)
                            room.message("Mai ai de asteptat "+format(d)+" zile "+format(h)+" ore "+format(m)+" minute "+format(s)+" secunde , nu e bine sa furi atata de mult :)")
                    else:
                        room.message("Utilizatorul "+paradatul+" nu merita sa fie jefuit! E prea sarac!")
                else:
                    room.message("Nu am gasit utilizatorul cu numele <b>"+paradatul+"</b>", True)
            else:
                room.message("Nu te cunosc! Dispari ;(")
        elif cmd=="/zar":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            room.deleteUser(ch.User(user.name))
            sql.execute("select * from `userdata` where `user`='"+user.name+"'")
            if(sql.rowcount == 1):
                row = sql.fetchone()
                timedb = int(row[6])
                ntime = int(time.time())
                timecalc = ntime-timedb
                if(timecalc > 300):
                    coin = random.randint(0,5)
                    ccoin = row[2]
                    ncoin = ccoin + coin
                    ncoin = format(ncoin)
                    ntime = format(ntime)
                    coin = format(coin)
                    user = row[1]
                    sql.execute("update `userdata` set `money`='"+ncoin+"', `lastzar`='"+ntime+"' where `user`='"+user+"' ")
                    conn.commit()
                    room.message("<b>"+user+"</b> ai dat cu zar-ul si ai primit <b>"+coin+"</b> belly! Acum ai <b>"+ncoin+"</b> belly!", True)
                else:
                    ramas = 300 - timecalc
                    minute = ramas / 60
                    minute = format(int(minute))
                    ramas = format(int(ramas/10))
                    room.message("Mai ai de asteptat "+ minute +" minute si "+ramas+" secunde pana sa poti da din nou cu zarul")
            else:
                room.message("Nu te-am gasit in baza de date :(")
        elif cmd=="$setbelly":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            room.deleteUser(ch.User(user.name))
            if getAccess(user.name) > 2:
                args=args.lower()
                if(len(args) > 3):
                    ar = args[0:].split(" ", 1)
                    user, value = ar[0], ar[1]
                    if(len(ar[0]) > 1 and len(ar[1]) > 1):
                        if(value.isdigit()):
                            sql.execute("select * from `userdata` where `user`='"+user+"'")
                            if(sql.rowcount == 1):
                                value = format(value)
                                sql.execute("update `userdata` set `money`="+value+" where `user`='"+user+"'")
                                conn.commit()
                                room.message("Am facut ce mi-ai cerut! @"+user+" -> "+value+" Belly")
                            else:
                                room.message("Nu am gasit utilizatorul cu numele '"+user+"'")
                        else:
                            room.message("Trebuie sa introduci un numar.")
                    else:
                        room.message("Folosire corecta <b>$setmoney utilizator valoare</b>", True)
                else:
                    room.message("Folosire corecta <b>$setmoney utilizator valoare</b>", True)
            else:
                room.message("Nu ai suficent access :(")
        elif cmd=="$setbank":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            room.deleteUser(ch.User(user.name))
            if getAccess(user.name) > 2:
                args=args.lower()
                if(len(args) > 3):
                    ar = args[0:].split(" ", 1)
                    user, value = ar[0], ar[1]
                    if(len(ar[0]) > 1 and len(ar[1]) > 1):
                        if(value.isdigit()):
                            sql.execute("select * from `userdata` where `user`='"+user+"'")
                            if(sql.rowcount == 1):
                                value = format(value)
                                sql.execute("update `userdata` set `bank`="+value+" where `user`='"+user+"'")
                                conn.commit()
                                room.message("Am facut ce mi-ai cerut! <b>@"+user+"</b> -> <b>"+value+"</b> Belly (bank)", True)
                            else:
                                room.message("Nu am gasit utilizatorul cu numele '"+user+"'")
                        else:
                            room.message("Trebuie sa introduci un numar.")
                    else:
                        room.message("Folosire corecta <b>$setbank utilizator valoare</b>", True)
                else:
                    room.message("Folosire corecta <b>$setbank utilizator valoare</b>", True)
            else:
                room.message("Nu ai suficent access :(")
        elif cmd=="$define":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            if getAccess(user.name) >= 0:
                args=message.body
                if(len(args) > 1):
                    ar = []
                    ar = args.split(" ", 3)
                    if(len(ar) > 3):
                        if(len(ar[1]) > 0 and len(ar[2]) > 0 and len(ar[3]) > 0):
                            if(ar[1] == "add"):
                                sql.execute("SELECT * FROM `definiti` WHERE `cuvant`='"+ar[1]+"'")
                                if(sql.rowcount == 0):
                                    if(len(ar[2]) > 1 and len(ar[3]) > 1):
                                        data = format(datetime.datetime.now().replace(microsecond=0))
                                        sql.execute("Insert into `definiti` (`cuvant`, `definitie`, `data`, `autor`) values ('"+ar[2]+"', '"+ar[3]+"', '"+data+"', '"+user.name+"')")
                                        conn.commit()
                                        room.message("Cuvantului <b>"+ar[2]+"</b> ia fost atribuita definitia "+ar[3], True)
                                    else:
                                        room.message("Cuvantul trebuie sa contina cel putin doua caractere")
                                else:
                                    room.message("Cuvantul este deja definit")
                            elif(ar[1] == "remove"):
                                if(ar[2] > 1):
                                    sql.execute("SELECT * FROM `definiti` WHERE `id`="+ar[2])
                                    if(sql.rowcount == 1):
                                        if(sql.getAccess(user.name) > 4):
                                            sql.execute("DELETE FROM `definiti` WHERE `id`="+ar[2])
                                            conn.commit()
                                            room.message("Am sters definitia cu id-ul"+ar[2])
                                        else:
                                            room.message("Nu te ascult pe tine :(")
                                    else:
                                        room.message("Nu am gasit definitia.")
                                else:
                                    room.message("Folosire corecta $define remove id")
                            else:
                                room.message("Nu stiu :(")
                        else:
                            room.message("Folosire corecta $define add/remove cuvant definitie 1")
                    else:
                        room.message("Folosire corecta $define add/remove cuvant definitie 2")
                else:
                    room.message("Folosire corecta $define add/remove cuvant definitie 3")
            else:
                room.message("Nu ai suficent access :(")
            sql.close()
            conn.close()
        elif cmd=="/ce":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            args=args.lower()
            if(len(args) > 1):
                sql.execute("SELECT * FROM `definiti` WHERE `cuvant` LIKE '%"+args+"%' ORDER BY `id` DESC LIMIT 5")
                if(sql.rowcount > 0):
                    row = sql.fetchone()
                    lista=[]
                    c = 0
                    text = "<b><u>Am gasit</u> :</b><br/>"
                    lista.append(text)
                    while row is not None:
                        id = row[0]
                        deff = row[2]
                        autor = row[4]
                        c = c + 1
                        text="["+format(c)+"] \""+deff+"\" de \""+autor+"\" (<b>"+format(id)+"</b>)<br/>"
                        lista.append(text)
                        row = sql.fetchone()
                    room.message("".join(lista),True)
                else:
                    room.message("Nu am gasit nimic :( ["+args+"]")
            else:
                room.message("Folosire corecta: /ce <b>termenul</b>", True)
        elif cmd=="/tf" or cmd=="/transfera":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            sql.execute("select * from `userdata` where `user`='"+user.name+"'")
            args=args.lower()
            if(len(args) > 3):
                if(sql.rowcount == 1):
                    ar = args[0:].split(" ", 1)
                    if len(ar) > 1:
                        to, value = ar[0], ar[1]
                        if(value.isdigit()):
                            value = int(value)
                            if(value > 0):
                                row = sql.fetchone()
                                coin = int(row[2])
                                coin = coin - value
                                if(coin > 0):
                                        sql.execute("select * from `userdata` where `user`='"+to+"'")
                                        if(sql.rowcount == 1):
                                            rowb = sql.fetchone()
                                            coinb = rowb[2]
                                            coinb = coinb + value
                                            sql.execute("update `userdata` set `money`='"+format(coin)+"' where `user`='"+user.name+"' ")
                                            conn.commit()
                                            sql.execute("update `userdata` set `money`='"+format(coinb)+"' where `user`='"+to+"' ")
                                            conn.commit()
                                            room.message("Utilizatorul @"+to+" a pirimit "+format(value)+" belly")
                                        else:
                                            room.message("Nu-l gasesc pe '"+to+"' in baza de date. :(")
                                else:
                                    room.message("Nu ai destule belly pentru a trimite. ["+format(value)+"]")
                            else:
                                room.message("Valorea trebuie sa fie pozitiva.")
                        else:
                            room.message("Te-am rugat sa introduci o valoare. Nu o litera.")
                    else:
                        room.message("Trebuie sa introduci un utilizator si o valoare.")
                else:
                    room.message("Huh! Nu te cunosc! Pleaca!")
            else:
                room.message("Folosire corecta <b>/tf utilizator valoare</b>", True)
            sql.close()
            conn.close()
        elif cmd=="/top":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            sql.execute("select * from `userdata` order by `money` desc limit 10")
            lista=[]
            c = 0
            row = sql.fetchone()
            text = "<b><u>Topul Bogatilor</u></b> <br/>"
            lista.append(text)
            while row is not None:
                uuser = row[1]
                coin = row[2]
                coin = format(coin)
                c = c + 1
                text="["+format(c)+"] <b>"+uuser+"</b> cu <b>"+coin+"</b> belly<br/>"
                lista.append(text)
                row = sql.fetchone()
            room.message("".join(lista), True)
            sql.close()
            conn.close()
        elif cmd=="/yt" or cmd=="/youtube":
           if args:
                room.message(youtube.yt(args),True)
           else:
                room.message("Ce sa caut?")
        elif cmd=="help" or cmd=="/help" or cmd=="ajutor":
            room.message("Uite aici o lista cu comenzi : <b>http://wien-subs.ro/bot.html </b>", True)
        elif cmd=="/nou":
          header = {
          'Content-Type':'application/x-www-form-urlencoded',
          'Host':'wien-subs.ro',
          'Origin':'http://wien-subs.ro/online/anime-ro-sub',
          'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.22 Safari/537.36'
          }
          conn = http.client.HTTPConnection("wien-subs.ro")
          conn.request("POST","/online/anime-ro-sub", None, header)
          url = conn.getresponse().read().decode()
          data=url.replace('\r',' ').replace('\n',' ').replace('\t',' ')          
          regex=re.findall(r'<h4 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h4>',data,re.DOTALL)
          regex2=re.findall(r'<div class="col-md-6"><i class="fa fa-clock-o"></i>(.*?)</div>',data,re.DOTALL)
          print(regex2)
          if not args:
             maxm=10
          else:
            try:
              if not int(args)> len(regex) and int(args)>0:
                maxm=int(args)
              else:
                room.message("Invalid ?")
                return
            except:
              maxm=10
          c=0
          num=1
          listu=[]
          while c<maxm:
            name=regex[c][1]
            link=regex[c][0]
            date=regex2[c]
            text="<b>["+str(num)+"]</b>: "+" "+name+" - "+link+" ("+date+")"
            listu.append(text)
            num=num+1
            c=c+1
          room.message("Episoade noi sunt: <br/> "+"<br/>".join(listu),True)
        elif cmd=="/cauta":
          args=args.lower().replace(" ","+")
          header = {
          'Content-Type':'application/x-www-form-urlencoded',
          'Host':'wien-subs.ro',
          'Origin':'http://www.wien-subs.ro/?s='+args,
          'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.22 Safari/537.36'
          }
          conn = http.client.HTTPConnection("wien-subs.ro")
          conn.request("POST", "/?s="+args, None, header)
          url = conn.getresponse().read().decode()
          data=url.replace('\r',' ').replace('\n',' ').replace('\t',' ')
          regex=re.findall(r'<h4 class="entry-title"><a href="(.*?)" rel="bookmark">(.*?)</a></h4>',data,re.DOTALL)
          num=1
          lista=[]
          c=0
          while c<len(regex):
             name=regex[c][1]
             link=regex[c][0]
             text="<b>["+str(num)+"]</b>: "+" "+name+" - "+link
             lista.append(text)
             num=num+1
             c=c+1
          room.message("Am cautat "+args+": <br/> "+"<br/>".join(lista),True)
        elif cmd=="/eu" or cmd == "/status" or cmd=="/stats":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            sql.execute("select * from `userdata` where `user`='"+user.name+"'")
            if(sql.rowcount == 1):
                row = sql.fetchone()
                coin = format(row[2])
                userdata = format(row[4])
                bank = getmoneybank(user.name)
                if(haveinv(user.name)):
                    inv = "<b>/inv</b>"
                else:
                    inv = "Nu"
                if(haveavatar(user.name)):
                    avatar = getAvatarName(user.name)
                    level = getAvatarLevel(user.name)
                else:
                    avatar = "Nu"
                    level = "0"
                room.message('Tu esti ' + user.name + ' !<br/> Te-am inregistrat -> ' +userdata+'.<br/>Ai gradul de -> '+getAccessPower(user.name)+' <br/> Ai adunat până acum -> '+coin+' belly <br/> Ai in banca -> '+format(bank)+' belly <br/> Inventory -> '+ format(inv) +'<br/>'+'Avatar -> '+'[Lv.'+format(level)+']'+ format(avatar), True)
            else:
                room.messsage("Nu te cunosc!")
        elif cmd=="/mc" or cmd=="/belly" or cmd=="/loli":
            conn = pymysql.connect(host='YourSQLdataBase', port=3306, user='YourDataBaseName', passwd='YourDataBasePassword', db='YourDataBaseName')
            sql = conn.cursor()
            sql.execute("select * from `userdata` where `user`='"+user.name+"'")
            if(sql.rowcount == 1):
                row = sql.fetchone()
                timedb = int(row[5])
                ntime = int(time.time())
                timecalc = ntime-timedb
                if(timecalc > 28800):
                    coin = random.randint(-31,31)
                    ccoin = row[2]
                    ncoin = ccoin + coin
                    if(ncoin < 0):
                        ncoin = 0
                        room.message("Îmi pare rău dar trebuie să o iei de la început, nu mai ai nici un belly")
                    ncoin = format(ncoin)
                    ntime = format(ntime)
                    coin = format(coin)
                    user = row[1]
                    sql.execute("update `userdata` set `money`='"+ncoin+"', `lastmoney`='"+ntime+"' where `user`='"+user+"' ")
                    conn.commit()
                    room.message("@"+user+" ai primit "+coin+" belly! Acum ai "+ncoin+" belly!")
                else:
                    ramas = 28800 - timecalc
                    m, s = divmod(ramas, 60)
                    h, m = divmod(m, 60)
                    room.message("Mai ai de asteptat "+format(h)+" ore si "+format(m)+" minute " +format(s)+" secunde")
            else:
                room.message("A aparut o eroare nu iti pot da belly :(")
        elif cmd=="bot" or cmd=="Yoshinon" or cmd=="auzi Yoshinon":
            room.message(random.choice(["Ce doresti?", "ia zi", "Eu!", "Spune?", "De ce ma cauti?", "Cu ce pot sa te ajut?", "Da-te dracu!"]))
        elif cmd=="/dictionar" or cmd=="/definitie" or cmd=="/cuvant":
          if args:
            url=urllib.request.urlopen("http://www.urbandictionary.com/define.php?term="+args)
            data=url.read().decode("utf-8")
            regex=re.findall(r'<div class=\'meaning\'>(.*?)</div>',data,re.DOTALL)
            regex2=re.findall(r'<div class=\'example\'>(.*?)</div>',data,re.DOTALL)
            if len(regex)>0:
              reps=regex[0]
              reps2=regex2[0]
              x=reps.replace("\n","")
              y=reps2.replace("\n","")
              room.message("Definitie: "+str(x)+"<br/>Exemplu: "+y,True)
            else:
              room.message("Din păcate nu am găsit nimic "+args+" :(")
        elif cmd=="/profil" or cmd=="/info":
          if args:
            try:
              args=args.lower()
              stuff=str(urllib.request.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
              age = re.findall('<strong>Age:</strong></span></td><td><span class="profile_text">(.*?)<br /></span></td>',stuff,re.DOTALL)
              if age:
                age=age[0]
              else:
                age="?"
              gender = re.findall('<strong>Gender:</strong></span></td><td><span class="profile_text">(.*?) <br /></span></td>',stuff,re.DOTALL)
              if gender[0] == 'M':
                gender = 'M'
              elif gender[0]== 'F':
                gender = 'F'
              else:
                gender = '?'
              location= re.findall('<strong>Location:</strong></span></td><td><span class="profile_text">(.*?) <br /></span>',stuff,re.DOTALL)
              if location:
                location=location[0]
              else:
                location= "?"
              picture = 'http://fp.chatango.com/profileimg/' + args[0] + '/' + args[1] + '/' + args + '/full.jpg'
              link = "http://"+args+".chatango.com"
              if(userexist(args)):
                money = getmoney(args)
                bank = getmoneybank(args)
                if(haveavatar(args)):
                    avatar = "[Lv."+format(getAvatarLevel(args))+"]"+getAvatarName(args)+" | "+num2class(getAvatarClass(args))
                else:
                    avatar = "no"
                add = "<br/>Belly: "+format(money)+"<br/> Bank Belly: "+format(bank)+"<br/> Avatar: "+avatar+"<br/>"
                inspect = '<b>Numele:</b> ' + args +'<br/> <b>Sexul:</b> '+ gender +'<br/> <b>Vârsta:</b> '+ age +'<br/>'+ "<br/> <b> Link: </b>"+link+"<br/>"+add+picture
                room.message(inspect,True)
              else:
                room.message(inspect,True)
            except Exception as e:
              room.message("ERROR | Access Denied")
          else:
            room.message("Nu ați introdus nici un nume. :(")   
        elif cmd=="/user":
            room.message("Ma joc cu: " + str(room.usercount) + " useri")
        elif cmd=="imi zice cineva un anime" or cmd=="vreau un anime" or cmd=="/anime" or cmd=="anime":
            conn = pymysql.connect(host='85.204.135.110', port=3306, user='proiecte', passwd='IoVaD43o7n3G', db='proiecte')
            sql = conn.cursor()
            sql.execute("select uid from `anime`")
            total = int(sql.rowcount)
            anime = random.randint(1, total)
            sql.execute("select * from `anime` where `uid`="+format(anime))
            row = sql.fetchone()
            room.message(row[1]+" : "+row[6])
        elif cmd=="/ms":
                room.message("cu placere ^^ <b>"+user.name+"</b>", True)
        elif cmd=="/invite":
            if len(args) > 0:
                room.deleteUser(ch.User(user.name))
                self.pm.message(ch.RoomManager(args), args+" intra si tu alaturi de noi! Pe http://"+room.name+".chatango.com ("+user.name+")")
                self.pm.message(ch.RoomManager(args), "Power by Wien-Subs © All Right Reserved, GNU-GPL")
                room.message("L-am invitat pe "+args)
            else:
                room.message("Trebuie sa introduci un nume de utilizator.")

rooms = ["wien-subsfansub"]

if __name__ == "__main__":
    bot.easy_start(rooms, "YourBotName", "YourBotPassword")