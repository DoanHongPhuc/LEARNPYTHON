from typing import Dict
import matplotlib.pyplot as plt
import json
from numpy import numarray
with open("C:/Users/Admin/Pictures/daxuly/sub.txt","r") as fp:
    data=fp.read()
    fp.close()
dict=json.loads(data)
sub=sorted(dict.values(),reverse=True)
author=sorted(dict,key=dict.__getitem__,reverse=True)
numb=range(len(sub))
print(author)
plt.bar(numb,sub,align='center')
plt.xticks(numb,author,rotation=70)
plt.xlabel("bai viet")
plt.ylabel("%")
plt.title("Phan tram ung ho cua cac bai vt")
for x,y in zip(numb,sub):
    plt.text(x+0.01, y+0.05, '%d' % y, ha='center', va= 'bottom')
plt.ylim(0, sub[0] + 10)
plt.show()
