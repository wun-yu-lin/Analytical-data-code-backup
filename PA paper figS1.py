# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:19:09 2021

@author: wunyu
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

fig = plt.figure(figsize=(10,10),dpi=2000)
word_dic={"family":"Arial","fontstyle":"italic"}
for x in range(1,5):
    ax = fig.add_subplot(2,2,x)
    if x == 1:
        #Fullscan profiling
        Fullscan = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/Fullscan0.5/metID/data_full0.5_30225.csv")
        Fullscan_mz=Fullscan["mz"]
        Fullscan_rt=Fullscan["rt"]
        plt.scatter(Fullscan_rt,Fullscan_mz,color="forestgreen",label="Full scan",s=4,alpha=1)
        plt.xlabel("RT (sec.)")
        plt.ylabel("m/z",fontdict=word_dic)
        plt.title("Metabolic profiling")
        
    elif x == 2:
        #DIA profiling
        DIA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DIA/metID/ms1.peak.table.csv")
        DIA_mz=DIA["mz"]
        DIA_rt=DIA["rt"]
        plt.scatter(DIA_rt,DIA_mz,color="mediumvioletred",label="DIA",s=4,alpha=1)
        plt.xlabel("RT (sec.)")
        plt.ylabel("m/z",fontdict=word_dic)
        plt.title("Metabolic profiling")
    elif x == 3:
        DDA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DDA/metID/ms1.peak.table_6298.csv")
        DDA_mz=DDA["mz"]
        DDA_rt=DDA["rt"]
        plt.scatter(DDA_rt,DDA_mz,color="sienna",label="DDA",s=4,alpha=1)
        plt.xlabel("RT (sec.)")
        plt.ylabel("m/z",fontdict=word_dic)
        plt.title("Metabolic profiling")
        plt.xlim(0,2500)
    else:
        DDA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DDA/metID/ms1.peak.table_6298.csv")
        DIA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DIA/metID/ms1.peak.table.csv")
        Fullscan = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/Fullscan0.5/metID/data_full0.5_30225.csv")
        DDA_mz=DDA["mz"]
        DIA_mz=DIA["mz"]
        Fullscan_mz=Fullscan["mz"]
        sns.kdeplot(Fullscan_mz,color="forestgreen",label="Full scan",alpha=1)
        sns.kdeplot(DIA_mz,color="mediumvioletred",label="DIA",alpha=1)
        sns.kdeplot(DDA_mz,color="sienna",label="DDA",alpha=1)
        plt.xlabel("m/z",fontdict=word_dic)
        plt.title("Mass distribution density")
        
plt.legend(loc="upper right")  
fig.subplots_adjust(wspace=0.38,hspace=0.38)