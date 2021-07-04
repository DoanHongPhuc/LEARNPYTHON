import urllib.request
import json
import time
i=0
while i<10:
    webUrl=urllib.request.urlopen("https://old.reddit.com/r/unixporn/new/.json")
    data=webUrl.read()
    namefile=str(int(time.time()))
    linkfolder='C:/Users/Admin/Pictures/data/'+namefile+".txt"
    with open(linkfolder,'wb') as fp:
        fp.write(data)
        fp.close()
    i+=1
    time.sleep(15*60)