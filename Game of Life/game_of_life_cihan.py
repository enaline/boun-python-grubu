# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:37:11 2020

@author: Cihan

"""



def gol(a,b):
    """"a is length of the edge
        b is number of the generation """
    import numpy as np
    s=np.random.randint(0,2,size=(1,a,a))
    print(s)
    for gen in range(b):
        n=[]
        for row in range(a):
            for col in range(a):
                if row==a-1 and col!=a-1:
                    if s[0,row,col+1]+s[0,0,col]+s[0,0,col+1]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,col+1]+s[0,0,col-1] < 2:
                            n.append(0)
                    elif s[0,row,col+1]+s[0,0,col]+s[0,0,col+1]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,col+1]+s[0,0,col-1] > 3:
                            n.append(0)
                    elif s[0,row,col+1]+s[0,0,col]+s[0,0,col+1]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,col+1]+s[0,0,col-1] == 2:
                            n.append(s[0,row,col])
                    elif s[0,row,col+1]+s[0,0,col]+s[0,0,col+1]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,col+1]+s[0,0,col-1] == 3:
                            n.append(1)
                elif col==a-1 and row!=a-1:
                    if s[0,row,0]+s[0,row+1,col]+s[0,row+1,0]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,0]+s[0,row+1,col-1] < 2:
                            n.append(0)
                    elif s[0,row,0]+s[0,row+1,col]+s[0,row+1,0]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,0]+s[0,row+1,col-1] > 3:
                            n.append(0)
                    elif s[0,row,0]+s[0,row+1,col]+s[0,row+1,0]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,0]+s[0,row+1,col-1] == 2:
                            n.append(s[0,row,col])
                    elif s[0,row,0]+s[0,row+1,col]+s[0,row+1,0]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,0]+s[0,row+1,col-1] == 3:
                            n.append(1)
                elif col==a-1 and row==a-1:
                    if s[0,row,0]+s[0,0,col]+s[0,0,0]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,0]+s[0,0,col-1] < 2:
                            n.append(0)
                    elif s[0,row,0]+s[0,0,col]+s[0,0,0]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,0]+s[0,0,col-1] > 3:
                            n.append(0)
                    elif s[0,row,0]+s[0,0,col]+s[0,0,0]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,0]+s[0,0,col-1] == 2:
                            n.append(s[0,row,col])
                    elif s[0,row,0]+s[0,0,col]+s[0,0,0]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,0]+s[0,0,col-1] == 3:
                            n.append(1)                    
                elif col!=a-1 and row!=a-1:
                    if s[0,row,col+1]+s[0,row+1,col]+s[0,row+1,col+1]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,col+1]+s[0,row+1,col-1] < 2:
                            n.append(0)
                    elif s[0,row,col+1]+s[0,row+1,col]+s[0,row+1,col+1]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,col+1]+s[0,row+1,col-1] > 3:
                            n.append(0)
                    elif s[0,row,col+1]+s[0,row+1,col]+s[0,row+1,col+1]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,col+1]+s[0,row+1,col-1] == 2:
                            n.append(s[0,row,col])
                    elif s[0,row,col+1]+s[0,row+1,col]+s[0,row+1,col+1]+s[0,row-1,col-1]+s[0,row-1,col]+s[0,row,col-1]+s[0,row-1,col+1]+s[0,row+1,col-1] == 3:
                            n.append(1)
        n=np.array(n)
        n=n.reshape(1,a,a)
        print(n)
        s=n
        
        
