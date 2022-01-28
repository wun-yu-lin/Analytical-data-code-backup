# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 18:02:15 2021

@author: wunyu
"""
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel("C:/Users/wunyu/Documents/test/EIC of 197.07.xlsx")

plt.figure(figsize=(4.5,3),dpi=1200)
plt.plot(data["Fullscan_time"],data["Fullscan_int"],label="Full scan",color="forestgreen")
plt.plot(data["DIA_time"],data["DIA_int"],label="DIA",color="mediumvioletred")
plt.plot(data["DDA_time"],data["DDA_int"],label="DDA",color="sienna")
plt.xlim(20,22.5)
plt.ylim(0,10000)
plt.ylabel("Intensity")
plt.xlabel("RT (min.)")
plt.grid(True,alpha=0.3)
plt.legend()
plt.show()