import json
import os
from os import path
from typing import Dict
path="C:/Users/Admin/Pictures/data"
FJoin=os.path.join
author={}
title={}
files = [FJoin(path, f) for f in os.listdir(path)]
for i in range(0,len(files)):
    with open(files[i],'rb') as fp:
        data=fp.read()
        fp.close()
    dict=json.loads(data)
    data=dict['data']['children']
    for j in range(0,25):
        baivt=data[j]['data']
        if baivt['title'] in title:
            break
        else:
            title[baivt['title']]=1
        if baivt['author'] not in author:
            author[baivt['author']]=baivt['score']
        else:
            author[baivt['author']]+=baivt['score']
hinhve=json.dumps(author)
with open("C:/Users/Admin/Pictures/daxuly/downs.txt",'w') as fp:
    fp.write(hinhve)
    fp.close()