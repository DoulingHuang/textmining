import re
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

f = pd.read_csv('desk1.csv', header=0, index_col=0)
print(f)
f = f.fillna(0)
print(f)
f = f.T
print(f)
f = f.values
print(f)

np.random.seed(5)

X = f
model = KMeans(n_clusters=5)
model.fit(X)
labels = model.labels_
print(type(labels))
print("labels", labels, labels.shape)

fig = plt.figure('f0', figsize=(50, 40))
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