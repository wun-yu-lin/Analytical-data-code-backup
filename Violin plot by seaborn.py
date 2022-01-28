# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:22:02 2021

@author: wunyu
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("C:/Users/wunyu/Documents/violinplot PA paper/RSD in DDA, DIA, Full scan.xlsx")

plt.figure(figsize=(7,5),dpi=1200)
colors=["forestgreen","mediumvioletred","sienna"]
sns.violinplot(data["Mode"],data["RSD"],
                order=["Full scan","DIA","DDA"],
                palette=["forestgreen","mediumvioletred","sienna"],
                bw="silverman",
                gridsize=1000,
                inner="box",
                data=data
                )
plt.ylabel("RSD%")
plt.xlabel(None)
plt.legend()
plt.show()
