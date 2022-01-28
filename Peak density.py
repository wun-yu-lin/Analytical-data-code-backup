# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:28:12 2021

@author: wunyu
"""

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

DDA_mz=DDA["mz"]
DIA_mz=DIA["mz"]
Fullscan_mz=Fullscan["mz"]
word_dic={"family":"Arial","fontstyle":"italic"}


plt.figure(figsize=(7,5),dpi=1200)
sns.kdeplot(Fullscan_mz,color="forestgreen",label="Full scan",alpha=1)
sns.kdeplot(DIA_mz,color="mediumvioletred",label="DIA",alpha=1)
sns.kdeplot(DDA_mz,color="sienna",label="DDA",alpha=1)

plt.xlabel("m/z",fontdict=word_dic)
plt.grid(True)
plt.legend()
plt.xlim(100,1000)
plt.show()
