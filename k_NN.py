import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import transpose
def k_nn(a:np.ndarray,size:int,x1:float,x2:float,k:int):
    distance=[]
    h={}
    for i in range(size):
        tmp=(a[i,0]-x1)**2+(a[i,1]-x2)**2
        distance.append(tmp)
        h[tmp]=i
    distance.sort()
    dem=0
    for i in range(k):
        if a[h[distance[i]],2]==0:
            dem-=1
        else:
            dem+=1
    if dem>0:
        return 1
    elif dem<0: 
        return 0
    else:
        if a[h[distance[0]],2]==0:
            return 0
        else:
            return 1
def k_nnnew(a:np.ndarray,new:list,k:int):
    r=a.shape
    row=r[0]
    column=r[1]
    kq=a[:,column-1]
    tmp=a[:,0]-new[0]
    traindata=tmp**2
    for i in range(1,column-1):
        tmp=a[:,i]-new[i]
        traindata+=tmp**2
    results={}    
    for i in range(row):
        results[float(traindata[i])]=i
    dem=0
    l=list(traindata)
    l.sort()
    for i in range(k):
        if kq[results[l[i]]]==1:
            dem+=1
        else:
            dem-=1
    if dem>0:
        return 1
    elif dem<0:
        return 0
    else:
        if kq[results[l[0]]]==1:
            return 1
        else:
            return 0

with open ("C:/Users/Admin/Pictures/daxuly/mixture.txt","r") as fp:
    a=fp.readline()
    data=np.loadtxt(fp,dtype=float,delimiter=',')
    fp.close()
c=data.shape
row=c[0]
column=c[1]
a=int(row*0.1)
b=int(row*0.8)
validation=data[0:30] ## 10% data
traindata=data[30:170] ## 70% data
testset=data[170:] ## 20% data
## tính phần trăm dự đoán chính xác
ptr=0
k=13
for i in range(30):
    tmp=k_nnnew(traindata,validation[i,:],k)
    if tmp==int(validation[i,column-1]):
        ptr+=1
ptr=ptr/30*100
print("phan tram du doan chinh xac cua ",k,"_nn la:",ptr,"%")



