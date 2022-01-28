# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 14:59:00 2021

@author: wunyu
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:19:09 2021

@author: wunyu
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fig = plt.figure(figsize=(12,7),dpi=300)
word_dic={"family":"Arial","fontstyle":"italic"}
for x in range(1,5):
    ax = fig.add_subplot(4,1,x)
    if x == 1:
        #Fullscan profiling
        Fullscan = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/Integration Full+DDA/metID/ms1.peak.table_fullscan+add.DDA.csv")
        Fullscan_mz=Fullscan["mz"]
        Fullscan_rt=Fullscan["rt"]
        plt.scatter(Fullscan_rt,Fullscan_mz,color="forestgreen",label="IFSDDA",s=4,alpha=1)
        plt.ylabel("m/z",fontdict=word_dic)
        plt.title("Metabolic profiling")
        plt.xlim(0,2500)
        plt.legend(loc="upper right")
        
    elif x == 2:
        #DIA profiling
        DIA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DIA/metID/ms1.peak.table.csv")
        DIA_mz=DIA["mz"]
        DIA_rt=DIA["rt"]
        plt.scatter(DIA_rt,DIA_mz,color="mediumvioletred",label="DIA",s=4,alpha=1)
        plt.ylabel("m/z",fontdict=word_dic)
        plt.xlim(0,2500)
        plt.legend(loc="upper right")
    elif x == 3:
        DDA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DDA/metID/ms1.peak.table_6298.csv")
        DDA_mz=DDA["mz"]
        DDA_rt=DDA["rt"]
        plt.scatter(DDA_rt,DDA_mz,color="sienna",label="DDA",s=4,alpha=1)
        plt.xlabel("RT (sec.)")
        plt.ylabel("m/z",fontdict=word_dic)
        plt.xlim(0,2500)
        plt.legend(loc="upper right")
    else:
        x = [1,2,3]
        y = [6298, 5893, 32830]
        colors=["sienna","mediumvioletred","forestgreen"]
        labels = ["DDA","DIA","IFSDDA"]
        xvalues=[0,10000,20000,30000]
        #tick_label為標記x軸標籤
        #堆疊bar圖bottom
        
        plt.barh(x,y,tick_label=labels,color=colors)
        plt.grid(b = True, color ='grey',
                linestyle ='-.', linewidth = 0.5,
                alpha = 0.2)
        plt.xlim(0,35000)
        plt.xticks(xvalues)
        plt.title("No. of features")
         
fig.subplots_adjust(wspace=0.5,hspace=0.8)