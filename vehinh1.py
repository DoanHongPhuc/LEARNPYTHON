from typing import Dict
import matplotlib.pyplot as plt
import json
from numpy import numarray
import matplotlib.figure
from numpy.lib.shape_base import tile 
def func(s:str)->str:
    dem=0
    for i in range(len(s)):
        if s[i]==' ':
            dem+=1
        if dem==3:
            s=s[0:i+1]+'\n'+s[i+1:]
    return s
with open("C:/Users/Admin/Pictures/daxuly/comments.txt","r") as fp:
    data=fp.read()
    fp.close()
dict=json.loads(data)
comments=sorted(dict.values(),reverse=True)
title=sorted(dict,key=dict.__getitem__,reverse=True)
numb=range(len(comments))
plt.bar(numb,comments,align='center')
for i in numb:
    title[i]=func(title[i])
plt.xticks(numb,title,rotation=45)
plt.xlabel("comments")
plt.ylabel("tille")
plt.title("luong comments cua cac bai vt")
for x,y in zip(numb,comments):
    plt.text(x+0.05,y+0.1, '%d' % y, ha='center', va= 'bottom')
plt.ylim(0, comments[0] + 50)
plt.show()