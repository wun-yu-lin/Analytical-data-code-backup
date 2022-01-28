# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 23:52:56 2021

@author: wunyu
"""
###volcanno plot

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_excel(r"C:/Users/wunyu/Documents/fullscan_PA/NEG/quantitative table/volcanotest_NEG.xlsx")
sns.set_palette(['red', 'blue', 'black'])
plt.figure(figsize=(7,10),dpi = 2500)
sns.scatterplot(data=data, x='log2 (FC)', y=' -log10 (p-value)',
                alpha=1,hue='Significance', size='VIP score' )
plt.legend(loc='upper right', bbox_to_anchor=(1.4, 1));
