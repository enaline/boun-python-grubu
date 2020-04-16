# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:05:47 2020

@author: Cihan
"""

def asm(a=10,b=15,c=2,d=0.51,e=0.25):
    
    """ a represents length of the edges.
            For instance, a=10: the area of the model will be 100.
        b represents number of ticks.
            For instance, b=40: there will be 40 generations in the model.
        c represents the number of colours.
            For instance, c=2: there will be 2 different groups in the model.
        d is the density of the same neighbour. It must be take a value between 0-1.
            For instance, d=0.51: agents will want %51 percent of their neighbours 
            from their group if there will be suitable condition.
        e is the density of the roads. It must be take a value between 0-1.
            For instance, e=0.25: 25% of the area will be road."""
            
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import random
    ez=[]
    for te in range(0,c+1):
        ez.append(te)
    pk=[e]
    pkl=1-e
    pp=pkl/c
    for pr in range(0,c):
        pk.append(pp)
    s=np.random.choice(ez,size=(1,a,a),p=pk)
    #print(s)
    apm=[]
    apm.append(s[0].copy())     
    for gen in range(b):
        randomrow=np.random.choice(a,a,replace=False)
        for row in randomrow:
            randomcol=np.random.choice(a,a,replace=False)
            for col in randomcol:
                if row==a-1 and col!=a-1:
                    n=[]
                    if s[0,row,col]!=0:
                        x=s[0,row,col]
                        n.append(s[0,row,col+1])
                        n.append(s[0,0,col])
                        n.append(s[0,0,col+1])
                        n.append(s[0,row-1,col-1])
                        n.append(s[0,row-1,col])
                        n.append(s[0,row,col-1])
                        n.append(s[0,row-1,col+1])
                        n.append(s[0,0,col-1])
                        unique, counts = np.unique(n, return_counts=True)
                        y=dict(zip(unique, counts))
                        zero=[]
                        zes=0
                        if 0 in y:
                            zero.append(y[0])
                            zes=zero[0]
                            del y[0]
                        po=np.random.choice(8,8,replace=False)
                        poh=0
                        h=2
                        if x in y:
                            if y[x]/(8-zes)<d:
                                while h>1:
                                    z=po[poh]
                                    if (z==0) & (s[0,row,col+1]==0):
                                        s[0,row,col+1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==1) & (s[0,0,col]==0):
                                        s[0,0,col]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==2) & (s[0,0,col+1]==0):
                                        s[0,0,col+1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==3) & (s[0,row-1,col-1]==0):
                                        s[0,row-1,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==4) & (s[0,row-1,col]==0):
                                        s[0,row-1,col]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==5) & (s[0,row,col-1]==0):
                                        s[0,row,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==6) & (s[0,row-1,col+1]==0):
                                        s[0,row-1,col+1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==7) & (s[0,0,col-1]==0):
                                        s[0,0,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif z==7:
                                        h=0
                                    else:
                                        poh=poh+1                                                                                 
                            else:
                                continue
                        else:
                            while h>1:
                                z=po[poh]
                                if (z==0) & (s[0,row,col+1]==0):
                                    s[0,row,col+1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==1) & (s[0,0,col]==0):
                                    s[0,0,col]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==2) & (s[0,0,col+1]==0):
                                    s[0,0,col+1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==3) & (s[0,row-1,col-1]==0):
                                    s[0,row-1,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==4) & (s[0,row-1,col]==0):
                                    s[0,row-1,col]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==5) & (s[0,row,col-1]==0):
                                    s[0,row,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==6) & (s[0,row-1,col+1]==0):
                                    s[0,row-1,col+1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==7) & (s[0,0,col-1]==0):
                                    s[0,0,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif z==7:
                                    h=0
                                else:
                                    poh=poh+1
                    else:
                        continue
                elif col==a-1 and row!=a-1:
                    n=[]
                    if s[0,row,col]!=0:   
                        x=s[0,row,col]
                        n.append(s[0,row,0])
                        n.append(s[0,row+1,col])
                        n.append(s[0,row+1,0])
                        n.append(s[0,row-1,col-1])
                        n.append(s[0,row-1,col])
                        n.append(s[0,row,col-1])
                        n.append(s[0,row-1,0])
                        n.append(s[0,row+1,col-1])
                        unique, counts = np.unique(n, return_counts=True)
                        y=dict(zip(unique, counts))
                        zero=[]
                        zes=0
                        if 0 in y:
                            zero.append(y[0])
                            zes=zero[0]
                            del y[0]
                        po=np.random.choice(8,8,replace=False)
                        poh=0
                        h=2
                        if x in y:
                            if y[x]/(8-zes)<d:
                                while h>1:
                                    z=po[poh]
                                    if (z==0) & (s[0,row,0]==0):
                                        s[0,row,0]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==1) & (s[0,row+1,col]==0):
                                        s[0,row+1,col]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==2) & (s[0,row+1,0]==0):
                                        s[0,row+1,0]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==3) & (s[0,row-1,col-1]==0):
                                        s[0,row-1,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==4) & (s[0,row-1,col]==0):
                                        s[0,row-1,col]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==5) & (s[0,row,col-1]==0):
                                        s[0,row,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==6) & (s[0,row-1,0]==0):
                                        s[0,row-1,0]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==7) & (s[0,row+1,col-1]==0):
                                        s[0,row+1,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif z==7:
                                        h=0
                                    else:
                                        poh=poh+1
                            else:
                                continue
                        else:
                            while h>1:
                                z=po[poh]
                                if (z==0) & (s[0,row,0]==0):
                                    s[0,row,0]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==1) & (s[0,row+1,col]==0):
                                    s[0,row+1,col]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==2) & (s[0,row+1,0]==0):
                                    s[0,row+1,0]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==3) & (s[0,row-1,col-1]==0):
                                    s[0,row-1,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==4) & (s[0,row-1,col]==0):
                                    s[0,row-1,col]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==5) & (s[0,row,col-1]==0):
                                    s[0,row,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==6) & (s[0,row-1,0]==0):
                                    s[0,row-1,0]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==7) & (s[0,row+1,col-1]==0):
                                    s[0,row+1,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif z==7:
                                    h=0
                                else:
                                    poh=poh+1
                    else:
                        continue
                elif col==a-1 and row==a-1:
                    n=[]
                    if s[0,row,col]!=0:   
                        x=s[0,row,col]
                        n.append(s[0,row,0])
                        n.append(s[0,0,col])
                        n.append(s[0,0,0])
                        n.append(s[0,row-1,col-1])
                        n.append(s[0,row-1,col])
                        n.append(s[0,row,col-1])
                        n.append(s[0,row-1,0])
                        n.append(s[0,0,col-1])
                        unique, counts = np.unique(n, return_counts=True)
                        y=dict(zip(unique, counts))
                        zero=[]
                        zes=0
                        if 0 in y:
                            zero.append(y[0])
                            zes=zero[0]
                            del y[0]
                        po=np.random.choice(8,8,replace=False)
                        poh=0
                        h=2
                        if x in y:
                            if y[x]/(8-zes)<d:
                                while h>1:
                                    z=po[poh]
                                    if (z==0) & (s[0,row,0]==0):
                                        s[0,row,0]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==1) & (s[0,0,col]==0):
                                        s[0,0,col]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==2) & (s[0,0,0]==0):
                                        s[0,0,0]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==3) & (s[0,row-1,col-1]==0):
                                        s[0,row-1,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==4) & (s[0,row-1,col]==0):
                                        s[0,row-1,col]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==5) & (s[0,row,col-1]==0):
                                        s[0,row,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==6) & (s[0,row-1,0]==0):
                                        s[0,row-1,0]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==7) & (s[0,0,col-1]==0):
                                        s[0,0,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif z==7:
                                        h=0
                                    else:
                                        poh=poh+1
                            else:
                                continue
                        else:
                            while h>1:
                                z=po[poh]
                                if (z==0) & (s[0,row,0]==0):
                                    s[0,row,0]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==1) & (s[0,0,col]==0):
                                    s[0,0,col]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==2) & (s[0,0,0]==0):
                                    s[0,0,0]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==3) & (s[0,row-1,col-1]==0):
                                    s[0,row-1,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==4) & (s[0,row-1,col]==0):
                                    s[0,row-1,col]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==5) & (s[0,row,col-1]==0):
                                    s[0,row,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==6) & (s[0,row-1,0]==0):
                                    s[0,row-1,0]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==7) & (s[0,0,col-1]==0):
                                    s[0,0,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif z==7:
                                    h=0
                                else:
                                    poh=poh+1
                    else:
                        continue
                elif col!=a-1 and row!=a-1:
                    n=[]
                    if s[0,row,col]!=0:   
                        x=s[0,row,col]
                        n.append(s[0,row,col+1])
                        n.append(s[0,row+1,col])
                        n.append(s[0,row+1,col+1])
                        n.append(s[0,row-1,col-1])
                        n.append(s[0,row-1,col])
                        n.append(s[0,row,col-1])
                        n.append(s[0,row-1,col+1])
                        n.append(s[0,row+1,col-1])
                        unique, counts = np.unique(n, return_counts=True)
                        y=dict(zip(unique, counts))
                        zero=[]
                        zes=0
                        if 0 in y:
                            zero.append(y[0])
                            zes=zero[0]
                            del y[0]
                        po=np.random.choice(8,8,replace=False)
                        poh=0
                        h=2
                        if x in y:
                            if y[x]/(8-zes)<d:
                                while h>1:
                                    z=po[poh]
                                    if (z==0) & (s[0,row,col+1]==0):
                                        s[0,row,col+1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==1) & (s[0,row+1,col]==0):
                                        s[0,row+1,col]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==2) & (s[0,row+1,col+1]==0):
                                        s[0,row+1,col+1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==3) & (s[0,row-1,col-1]==0):
                                        s[0,row-1,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==4) & (s[0,row-1,col]==0):
                                        s[0,row-1,col]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==5) & (s[0,row,col-1]==0):
                                        s[0,row,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==6) & (s[0,row-1,col+1]==0):
                                        s[0,row-1,col+1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif (z==7) & (s[0,row+1,col-1]==0):
                                        s[0,row+1,col-1]=x
                                        s[0,row,col]=0
                                        h=0
                                    elif z==7:
                                        h=0
                                    else:
                                        poh=poh+1
                            else:
                                continue
                        else:
                            while h>1:
                                z=po[poh]
                                if (z==0) & (s[0,row,col+1]==0):
                                    s[0,row,col+1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==1) & (s[0,row+1,col]==0):
                                    s[0,row+1,col]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==2) & (s[0,row+1,col+1]==0):
                                    s[0,row+1,col+1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==3) & (s[0,row-1,col-1]==0):
                                    s[0,row-1,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==4) & (s[0,row-1,col]==0):
                                    s[0,row-1,col]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==5) & (s[0,row,col-1]==0):
                                    s[0,row,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==6) & (s[0,row-1,col+1]==0):
                                    s[0,row-1,col+1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif (z==7) & (s[0,row+1,col-1]==0):
                                    s[0,row+1,col-1]=x
                                    s[0,row,col]=0
                                    h=0
                                elif z==7:
                                    h=0
                                else:
                                    poh=poh+1
                    else:
                        continue
        #print('-----------')
        #print(s)
        apm.append(s[0].copy())
        
        #Assimilation process
        shs=s.copy()
        for arow in range(a):
            for acol in range(a):
                if arow==a-1 and acol!=a-1:
                    if s[0,arow,acol]!=0:
                        aslist=[]
                        asblist=[]
                        aslist.append(s[0,arow,acol+1])
                        aslist.append(s[0,0,acol])
                        aslist.append(s[0,0,acol+1])
                        aslist.append(s[0,arow-1,acol-1])
                        aslist.append(s[0,arow-1,acol])
                        aslist.append(s[0,arow,acol-1])
                        aslist.append(s[0,arow-1,acol+1])
                        aslist.append(s[0,0,acol-1])
                        unique, counts = np.unique(aslist, return_counts=True)
                        y=dict(zip(unique, counts))
                        if 0 in y:
                            del y[0]
                        for eacha in range(c):
                            if eacha in y:
                                asblist.append(eacha)
                        for proba in asblist:
                            if random.random() < y[proba]/10:
                                shs[0,arow,acol]=proba
                                if shs[0,arow,acol]!=s[0,arow,acol]:
                                    break
                    else:
                        continue
                elif acol==a-1 and arow!=a-1:
                    if s[0,arow,acol]!=0:
                        aslist=[]
                        asblist=[]
                        aslist.append(s[0,arow,0])
                        aslist.append(s[0,arow+1,acol])
                        aslist.append(s[0,arow+1,0])
                        aslist.append(s[0,arow-1,acol-1])
                        aslist.append(s[0,arow-1,acol])
                        aslist.append(s[0,arow,acol-1])
                        aslist.append(s[0,arow-1,0])
                        aslist.append(s[0,arow+1,acol-1])
                        unique, counts = np.unique(aslist, return_counts=True)
                        y=dict(zip(unique, counts))
                        if 0 in y:
                            del y[0]
                        for eachb in range(c):
                            if eachb in y:
                                asblist.append(eachb)
                        for probb in asblist:
                            if random.random() < y[probb]/10:
                                shs[0,arow,acol]=probb
                                if shs[0,arow,acol]!=s[0,arow,acol]:
                                    break
                    else:
                        continue
                elif acol==a-1 and arow==a-1:
                    if s[0,arow,acol]!=0:
                        aslist=[]
                        asblist=[]
                        aslist.append(s[0,arow,0])
                        aslist.append(s[0,0,acol])
                        aslist.append(s[0,0,0])
                        aslist.append(s[0,arow-1,acol-1])
                        aslist.append(s[0,arow-1,acol])
                        aslist.append(s[0,arow,acol-1])
                        aslist.append(s[0,arow-1,0])
                        aslist.append(s[0,0,acol-1])
                        unique, counts = np.unique(aslist, return_counts=True)
                        y=dict(zip(unique, counts))
                        if 0 in y:
                            del y[0]
                        for eachc in range(c):
                            if eachc in y:
                                asblist.append(eachc)
                        for probc in asblist:
                            if random.random() < y[probc]/10:
                                shs[0,arow,acol]=probc
                                if shs[0,arow,acol]!=s[0,arow,acol]:
                                    break
                    else:
                        continue
                elif acol!=a-1 and arow!=a-1:
                    if s[0,arow,acol]!=0:
                        aslist=[]
                        asblist=[]
                        aslist.append(s[0,arow,acol+1])
                        aslist.append(s[0,arow+1,acol])
                        aslist.append(s[0,arow+1,acol+1])
                        aslist.append(s[0,arow-1,acol-1])
                        aslist.append(s[0,arow-1,acol])
                        aslist.append(s[0,arow,acol-1])
                        aslist.append(s[0,arow-1,acol+1])
                        aslist.append(s[0,arow+1,acol-1])
                        unique, counts = np.unique(aslist, return_counts=True)
                        y=dict(zip(unique, counts))
                        if 0 in y:
                            del y[0]
                        for eachd in range(c):
                            if eachd in y:
                                asblist.append(eachd)
                        for probd in asblist:
                            if random.random() < y[probd]/10:
                                shs[0,arow,acol]=probd
                                if shs[0,arow,acol]!=s[0,arow,acol]:
                                    break
                    else:
                        continue
        #print('-----------')
        #print(shs)
        s=shs
        apm.append(s[0].copy())
    images = []   
    fig = plt.figure(figsize=(a,a))
    for i in range(0, len(apm)):
        im = plt.imshow(apm[i], cmap='Oranges')
        images.append([im])
    ani = animation.ArtistAnimation(fig, images, interval=500)
    #matplotlib.pyplot.show()
    ani.save('Assimilation Model.gif', dpi=100, writer='imagemagick')





