# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 17:16:00 2021

@author: wunyu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:07:40 2021

@author: wunyu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

DDA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DDA/metID/ms1.peak.table_6298.csv")

DIA = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/DIA/metID/ms1.peak.table.csv")

Fullscan = pd.read_csv("G:/我的雲端硬碟/Paper 投稿/Data/development/Fullscan0.5/metID/data_full0.5_30225.csv")

DDA_mz=DDA["mz"]
DDA_rt=DDA["rt"]
DIA_mz=DIA["mz"]
DIA_rt=DIA["rt"]
Fullscan_mz=Fullscan["mz"]
Fullscan_rt=Fullscan["rt"]
word_dic={"family":"Arial","fontstyle":"italic"}
plt.figure(figsize=(7,7),dpi=1200)
plt.scatter(Fullscan_rt,Fullscan_mz,color="yellowgreen",label="Full scan",s=4,alpha=1)
plt.scatter(DDA_rt,DDA_mz,color="sandybrown",label="DDA",s=4,alpha=1)
plt.scatter(DIA_rt,DIA_mz,color="lightcoral",label="DIA",s=4,alpha=1)

plt.legend()
plt.ylim(100,1000)
plt.xlim(0,2400)
plt.xlabel("RT (sec.)")
plt.ylabel("m/z",fontdict=word_dic)
plt.grid(True)
plt.show()

