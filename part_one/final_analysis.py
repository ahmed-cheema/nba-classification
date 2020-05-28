from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import scipy.cluster.hierarchy as shc
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

testdf = df[(df.MPG > 23) & (df.GP > 15)].reset_index(drop=True) # minimum requirements

# PRINCIPAL COMPONENT ANALYSIS

features = [x for x in df.columns if (x != 'PLAYER_NAME') &  (x != 'POSITION')]

x = testdf.loc[:, features].values
y = testdf.loc[:,['PLAYER_NAME']].values

x = StandardScaler().fit_transform(x) # standardize all values

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['pc1', 'pc2'])

final = pd.concat([principalDf, testdf[['PLAYER_NAME']]], axis=1)

final = final[['PLAYER_NAME','pc1','pc2']]
final.columns = ['player','pc1','pc2']

# K-MEANS CLUSTERING

nx = final.loc[:,['pc1','pc2']].values

kmeans = KMeans(n_clusters=8)
kmeans.fit(x)
y_kmeans = kmeans.predict(x)

final['cluster'] = y_kmeans

plt.scatter(nx[:, 0], nx[:, 1], c=y_kmeans, s=50, cmap='viridis',edgecolor='black')

# HIERARCHICAL CLUSTERING

plt.figure(figsize=(8,22))
plt.title('NBA Hierarchical Clustering Dendrogram')
dend = shc.dendrogram(shc.linkage(x, method='ward'),labels=list(testdf.PLAYER_NAME),orientation='left')

plt.yticks(fontsize=8)
plt.xlabel('Height')

plt.tight_layout()
