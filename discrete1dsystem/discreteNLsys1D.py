#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 23:52:42 2021

@author: dilshad
"""

import numpy as np
import random

class discnonlexmp():
    
    def __init__(self,Q,R,Mu,P,N=1):
        
        self.Q=Q
        self.R=R
        self.N=N
        self.state=np.random.normal(Mu,np.sqrt(P),N)
        self.t=0
        
    def forward(self):
        
        
        proc_noise=np.random.normal(0,np.sqrt(self.Q),self.N)
        for k in range(self.N):
            self.state[k]=(0.5*self.state[k])+ (25*self.state[k]/(1+(self.state[k])**2))+8*np.cos(1.2*self.t)+proc_noise[k]
        self.t=self.t+1
        
    def measure(self):
        meas_noise=np.random.normal(0,np.sqrt(self.R),self.N)
        for k in range(self.N):
            self.obs[k]=((self.state[k]**2)/20)+meas_noise[k]
            
            
            
