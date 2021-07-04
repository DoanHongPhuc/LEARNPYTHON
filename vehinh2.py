from typing import Dict
import matplotlib.pyplot as plt
import json
from numpy import numarray
with open("C:/Users/Admin/Pictures/daxuly/downs.txt","r") as fp:
    data=fp.read()
    fp.close()
dict=json.loads(data)
score=sorted(dict.values(),reverse=True)
author=sorted(dict,key=dict.__getitem__,reverse=True)
numb=range(len(score))
plt.bar(numb,score,align='center')
plt.xticks(numb,author,rotation=70)
plt.xlabel("TAC GIA")
plt.ylabel("DIEM SO ")
plt.title("TAC GIA CO LUOT THICH CAO NHAT")
for x,y in zip(numb,score):
    plt.text(x+0.01, y+0.05, '%d' % y, ha='center', va= 'bottom')
plt.ylim(0, score[0] + 20)
plt.show()