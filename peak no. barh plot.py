# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 19:01:21 2021

@author: wunyu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 23:24:50 2021

@author: wunyu
"""

import numpy as np
import matplotlib.pyplot as plt


        
x = [1,2,3]
y = [6298, 5893, 30225]
colors=["chocolate","mediumvioletred","forestgreen"]

labels = ["DDA","DIA","Full scan"]
#tick_label為標記x軸標籤
#堆疊bar圖bottom
plt.figure(figsize=(7,3),dpi=600)

plt.barh(x,y,tick_label=labels,color=colors)
plt.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
plt.xlim(0,40000)
#plt.xlabel("No. of metabolite' features")
plt.show()
