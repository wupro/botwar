from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, urllib, urllib.parse
_session = requests.session()
botStart = time.time()
settings = {
    "line": "TOKEN SB",
    "pb1": "TOKEN KICKER 1",
    "pb2": "TOKEN KICKER 2",
    "kunci": False,
    "kata": "prank",
    "blacklist": {}
}
line = LINE(settings["line"])
line.log("Auth Token : " + str(line.authToken))
channelToken = line.getChannelResult()
pb1 = LINE(settings["pb1"])
pb1.log("Auth Token : " + str(pb1.authToken))
pb2 = LINE(settings["pb2"])
pb2.log("Auth Token : " + str(pb2.authToken))
oepoll = OEPoll(line)
lineProfile = line.getProfile()
lineSettings = line.getSettings()
myBOG = line.profile.mid
pb1BOG = pb1.getProfile().mid
pb2BOG = pb2.getProfile().mid
mid = line.getProfile().mid
Bots = [myBOG,pb1BOG,pb2BOG]
settings = {
    "kunci": False,
    "kata": "prank",
    "blacklist": {}
}
Drop_Xv = "ufe1707ae9b2ff7ab61505795b7995440" #ID_DROPING_BOTS
Xv_WIN = "ufe1707ae9b2ff7ab61505795b7995440" #ID_WINDOWS_XP
Xv_LAN = "ufe1707ae9b2ff7ab61505795b7995440" #ID_SERVER_LAN
Xv_Servic = "ufe1707ae9b2ff7ab61505795b7995440" #ID_PROV_SERVICE
Xv_DxD = "ufe1707ae9b2ff7ab61505795b7995440" #ID_SYSTEM_BOTS
Line_Import = [Drop_Xv,Xv_WIN,Xv_LAN,Xv_Servic,Xv_DxD] #ALL_IMPORTING
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)
def logError(text):
    line.log("[ ERROR ] " + str(text))
    tz = pytz.timezone("Asia/Taipei")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("PrankBots.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def command(text):
    pesan = text.lower()
    if settings["kunci"] == True:
        if pesan.startswith(settings["kata"]):
            prankbot = pesan.replace(settings["kata"],"")
        else:
            prankbot = "Undefined command"
    else:
        prankbot = text.lower()
    return prankbot
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            setKey = settings["kata"].title()
            if settings["kunci"] == False:
                 setKey = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        prankbot = command(text)
                        if prankbot == "abouts":
                            line.sendMessage(to,"|關於本機|\n|回覆訊息\n|翻群\n|踢人\n|進群\n|退群\n|主機退群\n|查看黑單\n|解黑\n|丟出機器友資\n|備份")
                        if prankbot == "backup":
                            try:
                                line.findAndAddContactsByMid(pb1BOG)
                                line.findAndAddContactsByMid(pb2BOG)
                                line.findAndAddContactsByMid(Drop_Xv)
                                line.findAndAddContactsByMid(Xv_WIN)
                                line.findAndAddContactsByMid(Xv_LAN)
                                line.findAndAddContactsByMid(Xv_Servic)
                                line.findAndAddContactsByMid(Xv_DxD)
                                pb1.findAndAddContactsByMid(myBOG)
                                pb1.findAndAddContactsByMid(pb2BOG)
                                pb1.findAndAddContactsByMid(Drop_Xv)
                                pb1.findAndAddContactsByMid(Xv_WIN)
                                pb1.findAndAddContactsByMid(Xv_LAN)
                                pb1.findAndAddContactsByMid(Xv_Servic)
                                pb1.findAndAddContactsByMid(Xv_DxD)
                                pb2.findAndAddContactsByMid(myBOG)
                                pb2.findAndAddContactsByMid(pb1BOG)
                                pb2.findAndAddContactsByMid(Drop_Xv)
                                pb2.findAndAddContactsByMid(Xv_WIN)
                                pb2.findAndAddContactsByMid(Xv_LAN)
                                pb2.findAndAddContactsByMid(Xv_Servic)
                                pb2.findAndAddContactsByMid(Xv_DxD)
                                line.sendMessage(to,"備份成功!")
                            except:
                                line.sendMessage(to,"備份成功!")
                        if prankbot == "in":
                            anggota = [pb1BOG,pb2BOG]
                            line.inviteIntoGroup(msg.to, anggota)
                            pb1.acceptGroupInvitation(msg.to)
                            pb2.acceptGroupInvitation(msg.to)
                        elif prankbot.startswith("kick "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        pb1.kickoutFromGroup(to,[ls])
                                        print (to,[ls])
                                    except:
                                        pb2.kickoutFromGroup(to,[ls])
                                        print (to,[ls])
                        elif prankbot == "banlist":
                                if settings["blacklist"] == {}:
                                    line.sendMessage(to,"尚未有黑名單!")
                                else:
                                    line.sendMessage(to,"═══════以下是黑單═══════")
                                    h = ""
                                    for i in settings["blacklist"]:
                                        h = line.getContact(i)
                                        line.sendContact(to,i)
                        elif prankbot == "clearban":
                            settings["blacklist"] = {}
                            line.sendMessage(to,"黑單已清空!")
                        elif prankbot == "mybots" or prankbot == "mybot":
                            line.sendContact(to, myBOG)
                            line.sendContact(to, pb1BOG)
                            line.sendContact(to, pb2BOG)
                        elif prankbot == "r":
                            profile = pb1.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb1.sendMessage(to, text)
                            profile = pb2.getProfile()
                            text = profile.displayName + "􀜁􀅔􏿿"
                            pb2.sendMessage(to, text)
                        elif prankbot == "bye":
                            pb1.leaveGroup(msg.to)
                            pb2.leaveGroup(msg.to)
                            line.sendMessage(to,"====我的作者=====")
                            line.sendContact(to, 'ufe1707ae9b2ff7ab61505795b7995440')
                            line.leaveGroup(msg.to)
                        elif prankbot == "out":
                            pb1.leaveGroup(msg.to)
                            pb2.leaveGroup(msg.to)
                        elif prankbot == "kikil":
                            if msg.toType == 2:
                                gs = line.getGroup(msg.to)
                                gs = pb1.getGroup(msg.to)
                                gs = pb2.getGroup(msg.to)
                                time.sleep(0.0002)
                                targets = []
                                for g in gs.members:
                                    if _name in g.displayName:
                                        targets.append(g.mid)
                                if targets == []:
                                    line.sendMessage(to,"規制!!!")
                                else:
                                     for target in targets:
                                         if not target in Bots:
                                             try:
                                                 klist=[pb1,pb2,line]
                                                 kicker=random.choice(klist)
                                                 kicker.kickoutFromGroup(to,[target])
                                                 print (to,[g.mid])
                                             except:
                                                 pass
        if op.type == 19 or op.type == 32:
            if myBOG in op.param3:
                if op.param2 in Bots:
                    pb1.inviteIntoGroup(op.param1,[op.param3])
                    line.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        pb1.inviteIntoGroup(op.param1,[op.param3])
                        pb2.kickoutFromGroup(op.param1,[op.param2])
                        line.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            pb1.kickoutFromGroup(op.param1,[op.param2])
                            pb2.inviteIntoGroup(op.param1,[op.param3])
                            line.acceptGroupInvitation(op.param1)
                        except:
                            pass
            if pb1BOG in op.param3: #BAGIAN BACKUP LEWAT QR
                if op.param2 in Bots:
                    pb1.inviteIntoGroup(op.param1,[op.param3])
                    line.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        line.updateGroup(G)
                        Ticket = line.reissueGroupTicket(op.param1)
                        pb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        G = pb2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        pb2.updateGroup(G)
                        Ticket = pb2.reissueGroupTicket(op.param1)
                        pb1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        pb1.kickoutFromGroup(op.param1,[op.param2])
            if pb2BOG in op.param3:
                if op.param2 in Bots:
                    pb1.inviteIntoGroup(op.param1,[op.param3])
                    line.acceptGroupInvitation(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        line.inviteIntoGroup(op.param1,[op.param3])
                        pb1.kickoutFromGroup(op.param1,[op.param2])
                        pb2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            pb1.inviteIntoGroup(op.param1,[op.param3])
                            pb2.acceptGroupInvitation(op.param1)
                        except:
                            pass
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
                try:
                    pb1.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        pb2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        line.kickoutFromGroup(op.param1,[op.param2])
    except Exception as error:
        logError(error)
        if op.type == 59:
            print (op)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
    except Exception as e:
        line.log("[SINGLE_TRACE] ERROR : " + str(e))
