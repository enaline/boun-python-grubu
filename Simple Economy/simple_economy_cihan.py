# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:11:37 2020

@author: Cihan
"""


def se(a):
    """a is number of thick"""
    import numpy as np
    import random as random
    import matplotlib.pyplot as plt
    n=[100]*500
    sumrichlist=[]
    sumpoorlist=[]
    for i in range(a):
        nop=[] #Not poor 
        for e in n:
            if e>0:
                nop.append(e)
        mp=len(nop) #Money Pool
        n=np.array(n)
        n=np.where(n>0,n-1,n)
        n=list(n)
        for luck in range(mp):
            lucky=random.choice(n)
            n.remove(lucky)
            lucky+=1
            n.append(lucky)
        n.sort()
        sumn=sum(n)
        sumr=sum(n[450:501])
        sump=sum(n[0:251])
        sumrich=sumr/sumn
        sumrichlist.append(sumrich)
        sumpoor=sump/sumn
        sumpoorlist.append(sumpoor)
    plt.figure()
    plt.subplot(2,2,1)
    plt.hist(data=n,x=n[:])
    plt.title("Simple Economy Model in:"+ str(a) +" ticks")
    plt.xlabel("Wealth")
    plt.ylabel("Number of People")
    plt.subplot(2,2,2)
    plt.plot(sumrichlist, label="Rich")
    plt.legend(loc="upper right")
    plt.plot(sumpoorlist, label="Poor")
    plt.legend(loc="upper right")
    plt.xlabel("Number of Ticks")
    plt.ylabel("Percentage")
    plt.tight_layout()    
    plt.savefig('plots.png', dpi=100)
    plt.show()
    print(n)  

