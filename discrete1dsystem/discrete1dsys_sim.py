#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 00:13:32 2021

@author: dilshad
"""
import matplotlib.pyplot as plt
import numpy as np
from discreteNLsys1D import discnonlexmp




set1=discnonlexmp(10,1,0,2,100)
truth=discnonlexmp(10,1,0,2,1)

kt=set1.N*[set1.t]

for k in range(100):
    set1.forward()
    truth.forward()

    kt=set1.N*[set1.t]

    plt.plot(kt,set1.state,'r')
    plt.plot(truth.t,truth.state,'bo-')
    