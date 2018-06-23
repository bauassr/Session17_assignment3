# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:17:23 2018

"""

import pandas as pd

possible_combination =["RR","RB","BB","BR"]

Data = pd.DataFrame(possible_combination,columns={"Events"})

def Probablity(event,R,B):
    N=R+B
    p1=[0,0]
    for i  in range(len(event)):
        if event[i]=='R':
            p1[i]=(R/N)
            R=R-1
            N=N-1
        if event[i]=='B':
           p1[i]=(B/N)
           B=B-1
           N=N-1
        
            
    return p1[0]*p1[1]
Pro =[]
for E in possible_combination:
   
    Pro.append(Probablity(E,4,6))

Data['Probablity'] = Pro   
Data.head()    