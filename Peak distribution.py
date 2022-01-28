# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:58:30 2021

@author: wunyu
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


DDA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DDA/metID/ms1.peak.table_6298.csv")

DIA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DIA/metID/ms1.peak.table.csv")

Fullscan = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/Fullscan0.5/metID/data_full0.5_30225.csv")
word_dic={"family":"Arial","fontstyle":"italic"}
DDA_mz=DDA["mz"]
DIA_mz=DIA["mz"]
Fullscan_mz=Fullscan["mz"]



bins = list(np.linspace(100,1000,num=200))

# =============================================================================
#seaborn
plt.figure(figsize=(7,5),dpi=1200)
sns.histplot(Fullscan_mz,bins=bins,kde=True,color="forestgreen",label="Full scan",alpha=1,fill=False)
sns.histplot(DIA_mz,bins=bins,kde=True,color="mediumvioletred",label="DIA",alpha=1,fill=False)
sns.histplot(DDA_mz,bins=bins,kde=True,color="chocolate",label="DDA",alpha=1,fill=False)


plt.xlim(100,1000)
plt.ylabel("No. of metabolite' features")
plt.xlabel("m/z",fontdict=word_dic)
plt.grid(True)
plt.legend()