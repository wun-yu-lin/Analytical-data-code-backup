# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 20:33:03 2021

@author: wunyu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:18:34 2021

@author: wunyu
"""
# K nearest neighbor (KNN) K最近鄰演算法
# Supervise learning 監督式分類器

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier #KNN套件
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
# =============================================================================
# #建立datasets dx=資料 dy=標籤

data = pd.read_excel("C:/Users/wunyu/Documents/KNN PA/diff.xlsx")

dx = np.array(data.iloc[0:,1:])
dy = []
for x in range(9):
    dy+=[1,1,1,1,1,1,0,0,0,0,0,0,1,1,1]
dy = np.array(dy)
dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std,dy,test_size=0.2,random_state=0)
# =============================================================================


# =============================================================================
# # 建立KNN模型
# 模型 = KNeighborsClassifier(n_neighbor=k值) k值代表選用相近的幾個點進行預測

# 建立模型後，呼叫fit() method對traning data做訓練
# 模型.fit(dx_train,dy_train)  #input測試資料與標籤來進行訊練

# 接著對測試集的特徵資料做出預測
# 測試集特徵預測結果 = model.predict(dx_test)

# 檢視模型對training data and testing data的預測準確性(百分比)
# 模型.score(特徵資料, 標籤資料)
# =============================================================================

score_training_save=[]
score_testing_save=[]
for x in range(1,80):
    knn = KNeighborsClassifier(n_neighbors=x)
    knn.fit(dx_train,dy_train)
    Predictions = knn.predict(dx_test)
    score_training = knn.score(dx_train,dy_train)  # 模型對於training data的準確度
    score_testing = knn.score(dx_test,dy_test)  # 模型對於testing data的準確度
    score_training_save.append([score_training*100])
    score_testing_save.append([score_testing*100])
    
plt.figure(figsize=(10,10))
plt.plot([x for x in range(1,80)],(score_training_save),label="training data",color="b")
plt.plot([x for x in range(1,80)],(score_testing_save),label="testing data",color="r")
plt.grid(True)
plt.legend()
plt.title("K nearest neighbor (KNN)")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.show()









