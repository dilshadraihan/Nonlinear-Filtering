#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 03:21:45 2021

@author: dilshad
"""
import numpy as np
from scipy.stats import multivariate_normal as gauspdf



class PF():
    
    def __init__(self,arg):
        
        
        self.samp=arg



    def PFpredict(self):
    
        self.samp.forward()
            
            
    def PFupdate(self,y_true):
       
        self.samp.measure()
        
        self.w=gauspdf(self.samp.obs,mean=y_true,cov=self.samp.R)
        self.w=self.w/sum(self.w)
       
    def PFresamp(self):
        
        ranser=np.random.uniform(0,1,self.samp.N)
        cumul_wt=np.cumsum(self.w)
        olstate=self.samp.state
        for k in range(self.N):
            jj=np.where(ranser[k]<cumul_wt)[0][0]
            self.samp.state[i]=olstate[jj]
        self.w=[1/self.N]*self.N    
      
         