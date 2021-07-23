#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 03:21:45 2021

@author: dilshad
"""
import numpy as np

from discreteNLsys1D import discnonlexmp



class PF():
    
    def __init__(self,arg):
        
        
        self.samp=arg



    def PFpredict(self):
    
        self.samp.forward()
            
            
    def PFupdate(self,y_true):
       
        self.samp.measure()
        #for i in range(n):
        #    self.w[i]=normpdf(self.samp.obs[k],y_true,self.samp.R)
        #self.w=self.w/sum(self.w)
       
      
         