import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


data=pd.read_csv(r'New_DataV2.csv',header=0)

data = data.drop(['name'], axis=1)
data = data.drop(['Unnamed: 0'], axis = 1)
#print(data)
mu = data.T.sum()
data1 = data.T
data2 = (data1)/(mu)
data3 = data2.T
data3 = data3.fillna(0)
a = data3
print(a)

x = a.values
pca = PCA(3)
pca = pca.fit(x)
x_dr = pca.transform(x)
print(x_dr)

pca_line = PCA().fit(x)
print(pca_line.transform(x))
print(pca_line.transform(x).shape)
print(pca_line.explained_variance_ratio_)

plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], np.cumsum(pca_line.explained_variance_ratio_))
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
plt.xlabel('components')
plt.ylabel('cumulative')
plt.show()


np.random.seed(5)
X = x_dr
model = KMeans(n_clusters=20)
model.fit(X)
labels = model.labels_
print(type(labels))
print("labels", labels, labels.shape)

fig = plt.figure('f0', figsize=(5, 4))
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
new.to_csv("20200729V1.csv", encoding="utf-8")