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
#import system
from datetime import timedelta
from time import gmtime, strftime
from django.utils.html import escape
import subprocess
from subprocess import call

#Defines
def welcome(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+user+"'")
    if(sql.rowcount < 1):
        timefmo = format(datetime.datetime.now().replace(microsecond=0))
        ntime = format(int(time.time()))
        sql.execute("insert into `userdata` (`user`, `money`, `firstjoin`, `lastmoney`) values ('"+ user+"', 20,'"+ timefmo +"', "+ntime+")")
        conn.commit()
        return user+" ai primit 20 belly"
    sql.close()
    conn.close()
def getuserid(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        return row[0]
    else:
        return 0
def getmoneybank(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        value = row[11]
        return value
    else:
        return 0
def getmoney(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        value = row[2]
        return value
    else:
        return 0
def getWin(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
        row = sql.fetchone()
        return row[9]
    else:
        return False
def getBattle(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `userdata` where `user`='"+format(user)+"'")
        row = sql.fetchone()
        return row[8]
    else:
        return False
def getLose(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
def addbl(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
def changesetting(name, value):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    if(value.capitalize() == "True" or value.capitalize() == "False"):
        sql.execute("UPDATE `setting` SET `value`='"+value.capitalize()+"' WHERE `name`='"+name+"'")
        conn.commit()
        return "Comanda a fost executata cu success!"
    else:
        return "Nu am putut executa comanda"
#define Shits
def dosql(query):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute(query)
    conn.commit()
    sql.close()
    conn.close()
def finalstrike(user, user1):
    name = getAvatarName(user)
    name1 = getAvatarName(user1)
    clas = getAvatarClass(user)
    if(clas == 1):
        msg = random.choice(magefinal)
    elif(clas == 2):
        msg = random.choice(swordfinal)
    else:
        msg = random.choice(archerfinal)
    final = name+msg+name1
    return final
def strike(user, user1):
    name = getAvatarName(user)
    name1 = getAvatarName(user1)
    clas = getAvatarClass(user)
    if(clas == 1):
        msg = random.choice(mage)
    elif(clas == 2):
        msg = random.choice(sword)
    else:
        msg = random.choice(archer)
    final = name+msg+name1
    return final
def isbl(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
def globalmute():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("SELECT * FROM `setting` WHERE `name`='offline'")
    row = sql.fetchone()
    if(row[2] == "True"):
        return "True"
    else:
        return "False"
def getAccess(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
def userexist(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
def setmoney(user, money):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    if(userexist(user)):
        sql.execute("UPDATE `userdata` SET `money`="+format(money)+" where `user`='"+user+"'")
        conn.commit()
        sql.close()
        conn.close()
    else:
        room.message("Nu te cunosc! Dispari!")
def haveinv(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
def invlisti(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
    if(sql.rowcount == 1):
        row = sql.fetchone()
        text = "<b>"+user+" Inventory's</b><br/>Slot1:"+iid2name(row[2])+"<br/>Slot2:"+iid2name(row[3])+"<br/>Slot3:"+iid2name(row[4])+"<br/>Slot4:"+iid2name(row[5])+"<br/>Slot5:"+iid2name(row[6])+"<br/>Slot6:"+iid2name(row[7])+"<br/>Slot7:"+iid2name(row[8])+"<br/>Slot8:"+iid2name(row[9])+"<br/>Slot9:"+iid2name(row[10])+"<br/>Slot10:"+iid2name(row[11])
        return text
    else:
        text = "You don't have inventory"
def iid2name(id):
    if(id == "empty"):
        return "empty"
    else:
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
        sql = conn.cursor()
        sql.execute("select * from `item` where `id`='"+format(id)+"'")
        if(sql.rowcount == 1):
            row = sql.fetchone()
            return "<b>"+row[1]+"</b>"
        else:
            return "Error: 4o4"
def emptyslot(user, slot):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
    if(sql.rowcount == 1):
        row = sql.fetchone()
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
def findemptyslot(user):
    slot = 2
    while(emptyslot(user, slot) is False):
        slot = slot + 1
    if(slot < 12):
        return slot
    else:
        return 0
def getAccessPower(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
        return 20
    elif(value == 2):
        return 6
    else:
        return 15
def recalc(clas, level, user):
    if(clas == 1):
        level = int(level)
        b = calcavatareq(getuserid(user))
        hp = int(getbasehp(1)) + (level * 3) + (level / 2) + b['bonushp']
        hp = int(hp)
        dmg = int(getbasedmg(1)) + level + (level / 2) + b['bonusdmg']
        dmg = int(dmg)
        #print(format(dmg)+" dmg|hp "+format(hp))
        #HP
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
        b = calcavatareq(getuserid(user))
        hp = int(getbasehp(2)) + (level * 3) + (level / 2) + b['bonushp']
        hp = int(hp)
        dmg = int(getbasedmg(2)) + level + (level / 2) + b['bonusdmg']
        dmg = int(dmg)
        #print(format(dmg)+" dmg|hp "+format(hp))
        #HP
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
        b = calcavatareq(getuserid(user))
        hp = int(getbasehp(3)) + (level * 3) + (level / 2) + b['bonushp']
        hp = int(hp)
        dmg = int(getbasedmg(3)) + level + (level / 2) + b['bonusdmg']
        dmg = int(dmg)
        #print(format(dmg)+" dmg|hp "+format(hp))
        #HP
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
        sql = conn.cursor()
        sql.execute("UPDATE `inventory` SET `hp`="+format(hp)+" where `userid`="+format(getuserid(user)))
        conn.commit()
        #DMG
        sql.execute("UPDATE `inventory` SET `power`="+format(dmg)+" where `userid`="+format(getuserid(user)))
        conn.commit()
        sql.close()
        conn.close()
def sethp(user, hp):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("UPDATE `inventory` SET `hp`="+format(hp)+" where `userid`="+format(getuserid(user)))
    conn.commit()
    sql.close()
    conn.close()
def setdmg(user, dmg):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("UPDATE `inventory` SET `power`="+format(dmg)+" where `userid`="+format(getuserid(user)))
    conn.commit()
    sql.close()
    conn.close()
def setlevel(user, level):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("UPDATE `inventory` SET `level`="+format(level)+" where `userid`="+format(getuserid(user)))
    conn.commit()
    sql.close()
    conn.close()
def getAvatarName(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
    xpreq = 100 * (level+1**3.5)
    return xpreq
def getAvatarPower(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
        row = sql.fetchone()
        return row[16]
    else:
        return False
def getAvatarHP(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
        row = sql.fetchone()
        return row[17]
    else:
        return False
def getAvatarLevel(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
        row = sql.fetchone()
        return row[13]
    else:
        return False
def getAvatarXP(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    if(haveavatar(user)):
        sql.execute("select * from `inventory` where `userid`="+format(getuserid(user)))
        row = sql.fetchone()
        return row[14]
    else:
        return False
def getAvatarClass(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
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
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    clas = int(getAvatarClass(user))
    actual = int(getAvatarXP(user))
    value = int(value)
    update = int(actual + value)
    level = int(getAvatarLevel(user))
    xpreq = int(lvlreq(level))
    if(level >= 99):
        return False
    else:
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
            setAvatarXP(user, 0)
            sql.close()
            conn.close()
            return True
def setAvatarXP(user, value):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    value = int(value)
    sql.execute("UPDATE `inventory` SET `xp`="+format(value)+" where `userid`='"+format(getuserid(user))+"'")
    conn.commit()
    sql.close()
    conn.close()
def addWin(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    win = int(getWin(user)) + 1
    battle = int(getBattle(user)) + 1
    sql.execute("UPDATE `userdata` SET `battle`="+format(battle)+", `win`="+format(win)+" where `user`='"+format(user)+"'")
    conn.commit()
    sql.close()
    conn.close()
def addLose(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    lose = int(getLose(user)) + 1
    battle = int(getBattle(user)) + 1
    sql.execute("UPDATE `userdata` SET `battle`="+format(battle)+", `lose`="+format(lose)+" where `user`='"+format(user)+"'")
    conn.commit()
    sql.close()
    conn.close()
def addBatttle(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    battle = int(getBattle(user)) + 1
    sql.execute("UPDATE `userdata` SET `battle`="+format(battle)+" where `user`='"+format(user)+"'")
    conn.commit()
    sql.close()
    conn.close()
#Item Functions
def caneq(clas, itemid):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("SELECT * FROM `item` where `id`="+itemid)
    row = sql.fetchone()
    if(row[4] == clas):
        return True
    else:
        return False
def calcavatareq(userid):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("SELECT * FROM `inventory` WHERE `userid`="+format(userid))
    row = sql.fetchone()
    equip = [row[18], row[19], row[20], row[21], row[22], row[23] ]
    bhp = 0
    bdmg = 0
    for eq in equip:
        sql.execute("SELECT * FROM `item` WHERE `id`="+format(eq))
        data = sql.fetchone()
        bhp = bhp + int(data[6])
        bdmg = bdmg + int(data[5])
    return {'bonushp':bhp, 'bonusdmg':bdmg }
def listshopi(user):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("SELECT * FROM `item`")
    user = user
    lista = []
    text = "<b>Shop List</b><br/>Nume | Clasa | DMG | HP | Pret<br/>"
    lista.append(text)
    for row in sql:
        iid = format(row[0])
        iname = format(row[1])
        iclass = format(num2class(row[4]))
        imetadmg = format(row[5])
        imetahp = format(row[6])
        iprice = format(row[7])
        if(iid is not "0"):
            text = iname+" | "+iclass+" | "+imetadmg+" | "+imetahp+" | "+iprice+"<br/>"
            lista.append(text)
    return ''.join(lista)
def existitembyname(name):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("SELECT * FROM `item` WHERE `name`='"+name+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        return row[0]
    else:
        return 0
def additem(user, itemid, slot):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    slot = slot - 2
    sql.execute("UPDATE `inventory` SET `slot"+format(slot)+"`='"+format(itemid)+"' WHERE `userid`='"+format(user)+"'")
    conn.commit()
def getitemprice(itemid):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("select * from `item` where `id`='"+format(itemid)+"'")
    if(sql.rowcount == 1):
        row = sql.fetchone()
        value = row[7]
        return value
    else:
        return 0
def getequipname(name):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("SELECT * FROM `item` WHERE `id`="+format(name))
    row = sql.fetchone()
    return row[1]
def getAvatarEQ(userid):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='wiensubs_chatangobot', passwd='MyFuckedPassword', db='wiensubs_chatangobot')
    sql = conn.cursor()
    sql.execute("SELECT * FROM `inventory` WHERE `userid`="+format(userid))
    row = sql.fetchone()
    msg = "Helmet: "+getequipname(row[18])+"<br/>Chestplate: "+getequipname(row[19])+"<br/>LeftH: "+getequipname(row[20])+"<br/>RightH: "+getequipname(row[21])+"<br/>Leggis: "+getequipname(row[22])+"<br/>Boots: "+getequipname(row[23])
    return msg
#replyes
sword = [" scoate sabia din teca și aplica o lovitura critica pe ", " prinde sabia cu doua măini si o trece prin armura lui ", " arunca sabia  și scoate cele doua pumnale pe care le înfige în "]
swordfinal = [" scoate sabia și il decapiteaza pe ", " ridica sabia și îl despica pe "]
mage = [" ridica bagheta rosteste doua vraji și il ametește pe ", " invoaca doi demoni care il ranesc pe "]
magefinal = [" scoate CODEX-ul și invoaca un meteorit asupra lui ", " ridica bagheta și o înfige in capul lui "]
archer = [" scoate o săgeata otravita și o trage spre capul lui ", " lanseaza clasica ploaie de sageși asupra lui "]
archerfinal = [" scoate o săgeata din tolba și o infige in capul lui ", " foloseste arcul ca sa il ștranguleze pe "]