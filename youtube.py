import urllib.request
import json
import random
import re
def youvid(args):
  try:
    search = args.split()
    url = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&key=AIzaSyBSnh-sIjd97_FmQVzlyGbcaYXuSt_oh84" % "+".join(search))
    udict = url.read().decode('utf-8')
    data = json.loads(udict)
    for d in data["items"]:
      link = "http://www.youtube.com/watch?v=" + d["id"]["videoId"]
      title = d["snippet"]["title"]
      uploader = d["snippet"]["channelTitle"]
      descript = d["snippet"]['description']
      k="<br/><br/><br/><b>Title</b>: %s <br/><b>Uploader</b>: %s<br/><b>Description</b>: %s<br/> %s" % (title, uploader, descript, link)
      print(k)
      return k
  except Exception as e:
    return "Nu am gasit nimic pentru "+args
  
def yt(args):
  try:
    search = args.split()
    url = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&key=AIzaSyBSnh-sIjd97_FmQVzlyGbcaYXuSt_oh84" % "+".join(search))
    udict = url.read().decode('utf-8')
    data = json.loads(udict)
    nest = []
    for d in data["items"]:
      nest.append(d)
    pick=random.choice(nest)
    link = "http://www.youtube.com/watch?v=" + pick["id"]["videoId"]
    title = pick["snippet"]["title"]
    uploader = pick["snippet"]["channelTitle"]
    descript = pick["snippet"]['description']
    k = "<br/><br/><br/><b>Title</b>: %s <br/><b>Uploader</b>: %s<br/><b>Description</b>: %s<br/> %s" % (title, uploader, descript, link)
    print(k)
    return k
  except Exception as e:
    return "Nu am gasit nimic pentru "+args
  
def desc1(x):
    try:
            vidid=str(x.split("/watch?v=")[1])[:11]
            url = urllib.request.urlopen("http://youtube.com/watch?v="+vidid)
            data = url.read().decode('utf-8')
            title=str(re.findall(r'<title>(.*?)</title>',data,re.DOTALL)[0])
            user= re.findall(r'<div class="yt-user-info">(.*?)" >(.*?)</a>',data,re.DOTALL)[0][1]
            k="<br/><br/><br/><b>Titlu</b>: %s <br/><b>Uploader</b>: %s" % (title, user)
            return str(k)
    except Exception as e:
        print(e)
      
def desc2(x):
    try:
            vidid=str(x.split("youtu.be/")[1])[:11]
            url = urllib.request.urlopen("http://youtube.com/watch?v="+vidid)
            data = url.read().decode('utf-8')
            title=str(re.findall(r'<title>(.*?)</title>',data,re.DOTALL)[0])
            user= re.findall(r'<div class="yt-user-info">(.*?)" >(.*?)</a>',data,re.DOTALL)[0][1]
            k="<br/><br/><br/><b>Titlu</b>: %s <br/><b>Uploader</b>: %s" % (title, user)
            return str(k)
    except Exception as e:
        print(e)
  
