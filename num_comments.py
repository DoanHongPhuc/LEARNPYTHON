import json
import os
from os import path
from typing import Dict
def clrtitle(s:str)->str:
    i=0
    j=0
    for i in range(len(s)):
        if s[i]=='[':
            j=i
        if s[i]==']':
            i=i+2
            break
    s=s[:j]+s[i:]
    return s
path="C:/Users/Admin/Pictures/data"
FJoin=os.path.join
num_comments={}
files = [FJoin(path, f) for f in os.listdir(path)]
for i in range(0,len(files)):
    with open(files[i],'rb') as fp:
        data=fp.read()
        fp.close()
    dict=json.loads(data)
    data=dict['data']['children']
    for j in range(0,25):
        baivt=data[j]['data']
        s=clrtitle(baivt['title'])
        if s not in num_comments:
            num_comments[s]=baivt['num_comments']
        else:
            break
hinhve=json.dumps(num_comments)
with open("C:/Users/Admin/Pictures/daxuly/comments.txt",'w') as fp:
    fp.write(hinhve)
    fp.close()