# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:32:17 2021

@author: wunyu
"""

import pandas as pd
import matplotlib.pyplot as plt

peak_list = pd.read_excel("C:/Users/wunyu/Documents/EIC/peak list.xlsx")
peak_mz = [str(x) for x in  (peak_list["mz"])]
peak_rt = list(peak_list["rt"])
peak_name = [str(int(x*100)/100) for x in  (peak_list["mz"])]


fig=plt.figure(figsize=(15,15),dpi=1200)
i=0
RT_range=0.3
for x in peak_name:
    ax = fig.add_subplot(3,3,i+1)
    data = pd.read_excel("C:/Users/wunyu/Documents/EIC/EIC of %s.xlsx"%x)
    Fullscan_time=data["time_fullscan"]
    Fullscan_int=data["int_fullscan"]
    DIA_time=data["time_DIA"]
    DIA_int=data["int_DIA"]
    DDA_time=data["time_DDA"]
    DDA_int=data["int_DDA"]
    plt.plot(Fullscan_time,Fullscan_int,color="forestgreen",label="Full scan")
    plt.plot(DIA_time,DIA_int,label="DIA",color="mediumvioletred")
    plt.plot(DDA_time,DDA_int,label="DDA",color="sienna")
    
    plt.xlim(peak_rt[i]-RT_range,peak_rt[i]+RT_range)
    plt.title("EIC of m/z %s"%x)
    plt.xlabel("RT (min.)")
    plt.ylabel("Intensity")
    plt.legend()
    if i == 1:
        plt.ylim(0,10000)
    elif i == 5:
        plt.ylim(0,25000)
    plt.ticklabel_format(style="sci",scilimits=(-5,4))
    i+=1
fig.subplots_adjust(wspace=0.3,hspace=0.3)
plt.show()
