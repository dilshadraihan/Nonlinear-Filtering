#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 00:13:32 2021

@author: dilshad
"""
import matplotlib.pyplot as plt
import numpy as np
from discreteNLsys1D import discnonlexmp
from PFclass import PF



set1=discnonlexmp(10,1,0,2,100)

truth=discnonlexmp(10,1,0,2,1)
kt=set1.N*[set1.t]

ax1=plt.plot(kt,set1.state,'r',label="propagated pdf")
ax1=plt.plot(truth.t,truth.state,'bo-',label="true state")

for k in range(10):
    
    plt.xlabel("time")
    plt.ylabel("x")
     
    truth.forward()
    set1.forward()
    kt=set1.N*[set1.t]
    ax1=plt.plot(kt,set1.state,'r')
    ax1=plt.plot(truth.t,truth.state,'bo-')
    
plt.legend(loc="upper right")
   
plt.show()