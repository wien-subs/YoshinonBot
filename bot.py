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
#load animelist#
animelist = []
f = open("anime.txt", "r")
for name in f.readlines():
    if len(name.strip())>0: animelist.append(name.strip())
f.close()
#End load#
#define Shits
def getAccessPower(user):
    conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
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
    conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
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
##

class bot(ch.RoomManager):
    def onInit(self):
        self.setNameColor("000033")
        self.setFontColor("000000")
        self.setFontFace("Typewriter")
        self.setFontSize(12)
        self.enableBg()
        self.enableRecording()

    def onJoin(self, room, user):
        conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
        sql = conn.cursor()
        sql.execute("select * from `userdata` where `user`='"+ user.name +"'")
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
        room.message("Key Hey! Sunt aici!")

    def onReconnect(self, room):
        print("Reconnected")

    def onMessage(self, room, user, message):
        cmds = message.body.startswith
        prefix = "/"
        self.safePrint(user.name + ': ' + message.body)
        with open ("textlog-" + room.name + ".txt", "a") as file:
            file.write(strftime("%Y-%m-%d %H:%M:%S") + ' ' + user.name + ': ' + message.body + "\n")
        msgdata = message.body.split(" ",1)
        if len(msgdata) > 1:
            cmd, args = msgdata[0], msgdata[1]
        else:
            cmd, args = msgdata[0],""
        cmd=cmd.lower()
        if len(cmd) >0:
            if cmd[0]==prefix:
                used_prefix = True
                cmd = cmd[1:]
            else:
                used_prefix= False
        else:
            return
        if cmd=="slap" or cmd=="slap":
            args=args.lower()
            if(len(args) > 3):
                ar = args[0:].split(" ", 1)
                arg = ar[0]
                if(len(ar[0]) > 1):
                    if(arg=="bot" or arg=="yoshinonbot" or arg=="yoshinon"):
                        if(GetAccess(user.name) > 1):
                            slap = random.choice(["De ce mă lovești! Incetează! mă doare ;(", "Te rog loveste-mă mai cu milă ;(", "Nuuu mai da! Te ROGG!!!!!"])
                            random.choice(slap)
                        else:
                            room.message("Haha! Buna incercare! Yoshinon îi trage o palmă lui @"+user.name.capitalize())
                    else:
                        slap = random.choice([user.name.capitalize()+" ia tras o oltenească lui @"+ar[0].capitalize()+" de la luat mama dracu", user.name.capitalize()+" la lovit pe @"+ar[0].capitalize()+" cu o balenă", user.name.capitalize()+" ia tras un pumn lui @"+ar[0].capitalize()+" [K.O.]", user.name.capitalize()+" la lovit pe @"+ar[0].capitalize()+" cu o bucata de pizza", user.name.capitalize()+" ia tras un sut lui @"+ar[0].capitalize()+" de la trimis in China"])
                        room.message(slap)
                else:
                    room.message("Utilizare corecta /slap utilizator")
            else:
                room.message("Utilizare corecta /slap utilizator")
        elif cmd=="bet" or cmd=="/bet":
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
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
                            chance = [5,3,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0]
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
                            room.message("Valorea trebuie sa fie pozitiva")
                    else:
                        room.message("Nu poti paria ceea ce nu ai :(")
                else:
                    room.message("Trebuie sa introduci o valoare pozitiva.")
            else:
                room.message("Nu te cunosc :( ! Dispari!")
        elif cmd=="clear" or cmd=="sterge":
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
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
            sql = conn.cursor()
            if getAccess(user.name) > 4:
                args=args.lower()
                if(len(args) > 3):
                    ar = args[0:].split(" ", 1)
                    if(len(ar[0]) > 1 and len(ar[1]) > 0 and len(ar[1]) < 6):
                        user, value = ar[0], ar[1]
                        if(value.isdigit()):
                            sql.execute("select * from `userdata` where `user`='"+user.name+"'")
                            if(sql.rowcount == 1):
                                sql.execute("update `userdata` set `access`="+format(value)+" where `user`='"+user.name+"'")
                                conn.commit()
                                room.message("L-am promovat pe "+user+" la nivelul de access "+format(value))
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
        elif cmd=="fura" or cmd=="jefuieste" or cmd=="asedieaza":
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
            sql = conn.cursor()
            args=args.lower()
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
                        room.message("Utilizatorul @"+paradatul+" nu merita sa fie jefuit! E prea sarac!")
                else:
                    room.message("Nu am gasit utilizatorul cu numele <b>"+paradatul+"</b>", True)
            else:
                room.message("Nu te cunosc! Dispari ;(")
        elif cmds("zar") or cmds("/zar") or cmds("sfarcuri"):
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
            sql = conn.cursor()
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
                    room.message("@"+user+" ai dat cu zar-ul si ai primit "+coin+" belly! Acum ai "+ncoin+" belly!")
                else:
                    ramas = 300 - timecalc
                    minute = ramas / 60
                    minute = format(int(minute))
                    ramas = format(int(ramas/10))
                    room.message("Mai ai de asteptat "+ minute +" minute si "+ramas+" secunde pana sa poti da din nou cu zarul")
            else:
                room.message("Nu te-am gasit in baza de date :(")
        elif cmd=="$setbelly":
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
            sql = conn.cursor()
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
                                room.message("Am facut ce mi-ai cerut! "+user+" -> "+value)
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
        elif cmd=="$define":
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
            sql = conn.cursor()
            if getAccess(user.name) > 1:
                args=message.body
                if(len(args) > 1):
                    ar = []
                    ar = args.split(" ", 3)
                    if(len(ar) > 3):
                        if(len(ar[1]) > 1 and len(ar[2]) > 1 and len(ar[3]) > 1):
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
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
            sql = conn.cursor()
            args=args.lower()
            if(len(args) > 1):
                sql.execute("SELECT * FROM `definiti` WHERE `cuvant` LIKE '%"+args+"%' ORDER BY `id` DESC LIMIT 5")
                if(sql.rowcount > 0):
                    row = sql.fetchone()
                    lista=[]
                    c = 0
                    text = "<b><u>Am gasit</u></b><br/>"
                    lista.append(text)
                    while row is not None:
                        id = row[0]
                        deff = row[2]
                        autor = row[4]
                        c = c + 1
                        text="["+format(c)+"] '"+deff+"' de '"+autor+"' (<b>"+format(id)+"</b>)<br/>"
                        lista.append(text)
                        row = sql.fetchone()
                    room.message("".join(lista),True)
                else:
                    room.message("Nu am gasit nimic :( ["+args+"]")
            else:
                room.message("Folosire corecta: /ce <b>termenul</b>", True)
        elif cmd == "tf" or cmd == "/tf" or cmd == "transfera" or cmd == "/transfera":
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
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
                                            room.message("Utilizatorul "+to+" a pirimit "+format(value)+" belly")
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
        elif cmd == "/top" or cmd == "top" or cmd == "perversi":
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
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
        elif cmd == "yt" or cmd == "youtube":
           if args:
                room.message(youtube.yt(args),True)
           else:
                room.message("Ce sa caut?")
        elif cmds("help") or cmds("/help") or cmds("ajutor") or cmds("admin"):
            room.message("Incerca sa scrii anime sau vreau anime pentru a primit un anime ales aleatoriu")
        elif cmd == "nou":
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
        elif cmd == "cauta":
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
        elif cmd == "eu" or cmd == "/eu" or cmd == "/info" or cmd == "info" or cmd == "/status" or cmd == "status" or cmds("stats") or cmds("/stats"):
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
            sql = conn.cursor()
            sql.execute("select * from `userdata` where `user`='"+user.name+"'")
            if(sql.rowcount == 1):
                row = sql.fetchone()
                coin = format(row[2])
                userdata = format(row[4])
                room.message('Tu esti ' + user.name + ' !<br/> Te-am inregistrat : ' +userdata+'.<br/>Ai gradul de : '+getAccessPower(user.name)+' <br/> Ai adunat până acum -> '+coin+' belly', True)
            else:
                room.messsage("Nu te cunosc!")
        elif cmds("mc") or cmds("loli") or cmds("belly") or cmds("/mc") or cmds("/loli") or cmds("/belly"):
            conn = pymysql.connect(host='your_host_address', port=3306, user='your_user_name', passwd='your_password', db='your_database_name')
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
                    minute = ramas / 60
                    ore = minute / 60
                    ore = format(int(ore))
                    minute = format(int(minute/10))
                    room.message("Mai ai de asteptat "+ ore +" ore si "+minute+" minute")
            else:
                room.message("A aparut o eroare nu iti pot da belly :(")
        elif cmds("pe mata") or cmds("o muie") or cmds("muie"):
            room.message(random.choice(["Dute la magunama si spunei despre mine :)", "Dute la harvu, iti face el!", "Intrebal pe naihaz daca e liber", "Haha! Eu doar dau muie!"]))
        elif cmds("bot") or cmds("Yoshinon") or cmds("auzi Yoshinon"):
            room.message(random.choice(["Ce doresti?", "ia zi", "Eu!", "Spune?", "De ce ma cauti?", "Cu ce pot sa te ajut?", "Da-te dracu!"]))
        elif cmds("pe cine iubesti"):
            room.message(random.choice(["Pe Yoshinon!! <3", "Pe toti :)", "singuur.. atat de singur"]))
        elif cmds("ce dragut") or cmds("ce cute"):
            room.message(random.choice(["Ooo :3", "Tu esti mai dragut/a :)", "chiar că sunt dragută "]))
        elif cmds("cine te-a facut?") or cmds("cine e creeatorul tau") or cmds("cine e creatorul tau"):
            room.message(random.choice(["Creator zici? De ce ai intreba asta?! Fmohican!", "Huh? Mohicanu'"]))
        elif cmd == "dictionar" or cmd == "definitie" or cmd == "cuvant":
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
        elif cmd == "profil" or cmd == "info":
          if args:
            try:
              args=args.lower()
              stuff=str(urllib.request.urlopen("http://"+args+".chatango.com").read().decode("utf-8"))
              age= re.findall('<strong>Age:</strong></span></td><td><span class="profile_text">(.*?)<br /></span></td>',stuff,re.DOTALL)
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
              inspect = '<b>Numele:</b> ' + args +'<br/> <b>Sexul:</b> '+ gender +'<br/> <b>Vârsta:</b> '+ age +'<br/>'+ "<br/> <b> Link: </b>"+link+"<br/>"+picture
              room.message(inspect,True)
            except Exception as e:
              room.message("ERROR | Access Denied.")
          else:
            room.message("Nu ați introdus nici un nume. :(")   
        elif cmd == "user" or cmd == "/user":
            room.message("Ma joc cu: " + str(room.usercount) + " useri")
        elif cmds("imi zice cineva un anime") or cmds("vreau un anime") or cmds("/anime") or cmds("anime") or cmds("un anime") or cmds("un anime fain") or cmds("vreau un anime fain") or cmds("pls un anime") or cmds("imi zice cineva un anime") or cmds("imi ziceti va rog un anime") or cmds("imi zice-ti va rog un anime") or cmds("imi zice cineva si mie un anime") or cmds("vreau anime"):
            readtext = open("anime.txt", "r")
            room.message(random.choice(readtext.readlines()))
            readtext.close
        elif cmds("/ms") or cmds("ms"):
                room.message("cu placere ^^")
        elif used_prefix and cmd=="announce" or cmd == "ac":
            if getAccess(user) > 1:
                if args:
                    for _room in self.rooms:
                        _room.message("http://peacockmedia.software/images/Announce_icon_128.png "+user.name.capitalize()+": "+args)
                else:
                    room.message("I've nothing to announce.")
            else:
                room.message("Nu ai permisiunea necesara :(")


rooms = ["wien-subsfansub"]

if __name__ == "__main__":
    bot.easy_start(rooms, "Yoshinonbot", "Florin12")
