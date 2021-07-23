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
pfob=PF(set1)
truth=discnonlexmp(10,1,0,2,1)
kt=set1.N*[set1.t]

for k in range(20):
    
   

    kt=set1.N*[set1.t]

    plt.plot(kt,pfob.samp.state,'r')
    plt.plot(truth.t,truth.state,'bo-')
    plt.plot(truth.t,np.mean(pfob.samp.state),'g+')
     
    truth.forward()
    pfob.PFpredict()
    
    truth.measure()
    yt=truth.obs
    
    pfob.PFupdate(yt)
    pfob.PFresamp()
    