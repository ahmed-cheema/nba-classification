from sklearn.preprocessing import StandardScaler
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

# GAUSSIAN MIXTURE MODEL

gmm = GaussianMixture(n_components=8).fit(principalComponents)
labels = gmm.predict(principalComponents)
final['cluster'] = labels
plt.scatter(nx[:, 0], nx[:, 1], c=labels, cmap='viridis', edgecolor='black')
