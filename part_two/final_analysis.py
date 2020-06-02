from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

testdf = df[(df.MPG > 23) & (df.GP > 15)].reset_index(drop=True) # minimum requirements

# PRINCIPAL COMPONENT ANALYSIS

features = [x for x in df.columns if (x != 'PLAYER_NAME') &  (x != 'POSITION') & (x != 'SEASON')]

x = testdf.loc[:, features].values
y = testdf.loc[:,['PLAYER_NAME']].values

x = StandardScaler().fit_transform(x) # standardize all values

pca = PCA(n_components=0.99)
principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data = principalComponents2, columns = ['pc1', 'pc2'])

final = pd.concat([principalDf, testdf[['PLAYER_NAME','SEASON','POSITION','VORP']]], axis=1)

final = final[['PLAYER_NAME','SEASON','POSITION','VORP','pc1','pc2']]
final.columns = ['player','ssn','pos','vorp','pc1','pc2']

# FINDING OPTIMAL NUMBER OF CLUSTERS (K) FOR K-MEANS CLUSTERING

plt.subplot(1,2,1)

wcss = []
for i in range(1, 21):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(principalComponents)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 21), wcss)
plt.scatter(range(1, 21), wcss)
plt.title('elbow method')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
plt.show()

plt.subplot(1,2,1)

score_list = []
for n_clusters in range(1, 21):
    local_score = []
    for n in range(1,10):
        clusterer = KMeans(n_clusters=n_clusters)
        preds = clusterer.fit_predict(principalComponents)
        score = silhouette_score(df, preds)
    score_list.append(sum(local_score)/len(local_score))
plt.plot(range(1, 21), score_list)
plt.scatter(range(1, 21), score_list)
plt.title('silhouette method')
plt.xlabel('number of clusters')
plt.ylabel('silhouette score')
plt.show()

# FINDING OPTIMAL NUMBER OF CLUSTERS (K) FOR GAUSSIAN MIXTURE MODEL

n_components = np.arange(1, 21)
models = [GaussianMixture(n, covariance_type='full', random_state=0).fit(principalComponents)
          for n in n_components]

plt.plot(n_components, [m.bic(principalComponents) for m in models], label='BIC')
plt.scatter(n_components, [m.bic(principalComponents) for m in models])
plt.xlabel('number of clusters')
plt.ylabel('bic')
plt.title('bayesian information criterion (bic) method')
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

# GAUSSIAN MIXTURE MODEL

gmm = GaussianMixture(n_components=8).fit(principalComponents)
labels = gmm.predict(principalComponents)
final['cluster'] = labels
plt.scatter(nx[:, 0], nx[:, 1], c=labels, cmap='viridis', edgecolor='black')
