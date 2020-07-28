import re
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

data=pd.read_csv(r'New_DataV2.csv',header=0, encoding='unicode_escape')
data = data.drop(['name'], axis=1)
data = data.drop(['Unnamed: 0'], axis = 1)
print(data)
mu = data.T.sum()
data1 = data.T
data2 = (data1)/(mu)
data3 = data2.T
data3 = data3.fillna(0)
#data3.to_csv("20200726_V2.csv", encoding='utf-8')
a = data3.values
print(a)

np.random.seed(5)

X = a
model = KMeans(n_clusters=20)
model.fit(X)
labels = model.labels_
print(type(labels))
print("labels", labels, labels.shape)

fig = plt.figure('f0', figsize=(10, 8))
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels.astype(np.float), edgecolors='k')

C = model.cluster_centers_
ax.scatter(C[:, 0], C[:, 1], C[:, 2], c='red', s=100, alpha=0.5)

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

ax.set_xlabel('A', fontproperties="SimSum")
ax.set_ylabel('B', fontproperties="SimSum")
ax.set_zlabel('C', fontproperties="SimSum")
ax.set_title("KM3D")
ax.dist = 12
plt.show()

df = pd.DataFrame(labels)
print(df)
new = pd.concat( [df , data], axis=1 )
print(new)
new.to_csv("20200726_V3.csv", encoding="utf-8")
