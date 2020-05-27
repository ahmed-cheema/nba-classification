from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import scipy.cluster.hierarchy as shc
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

testdf = df[(df.MPG > 23) & (df.GP > 15)].reset_index(drop=True) # minimum requirements

# PRINCIPAL COMPONENT ANALYSIS

features = ['AGE','GP','MIN','MPG','FGM','FGA','FG_PCT','FG2M','FG2A','FG2_PCT','FG3M','FG3A','FG3_PCT','FTM','FTA','FT_PCT','OREB','DREB','REB','AST','TOV','STL','BLK','BLKA','PF','PFD','PTS','EFG','C','F','G','PLAYER_HEIGHT_INCHES','PLAYER_WEIGHT','NET_RATING','OREB_PCT','DREB_PCT','USG_PCT','TS_PCT','AST_PCT','AST_TO','CONTESTED_SHOTS','CONTESTED_SHOTS_2PT','CONTESTED_SHOTS_3PT','DEFLECTIONS','CHARGES_DRAWN','SCREEN_ASSISTS','SCREEN_AST_PTS','OFF_LOOSE_BALLS_RECOVERED','DEF_LOOSE_BALLS_RECOVERED','LOOSE_BALLS_RECOVERED','OFF_BOXOUTS','DEF_BOXOUTS','BOX_OUT_PLAYER_TEAM_REBS','BOX_OUT_PLAYER_REBS','BOX_OUTS','PASSES_MADE','PASSES_RECEIVED','FT_AST','SECONDARY_AST','POTENTIAL_AST','AST_PTS_CREATED','DIST_MILES','DIST_MILES_OFF','DIST_MILES_DEF','AVG_SPEED','AVG_SPEED_OFF','AVG_SPEED_DEF','TOUCHES','FRONT_CT_TOUCHES','TIME_OF_POSS','AVG_SEC_PER_TOUCH','AVG_DRIB_PER_TOUCH','PTS_PER_TOUCH','ELBOW_TOUCHES','POST_TOUCHES','DRIVE_PTS','DRIVE_FG_PCT','CATCH_SHOOT_PTS','CATCH_SHOOT_FG_PCT','PULL_UP_PTS','PULL_UP_FG_PCT','PAINT_TOUCH_PTS','PAINT_TOUCH_FG_PCT','POST_TOUCH_PTS','POST_TOUCH_FG_PCT','ELBOW_TOUCH_PTS','ELBOW_TOUCH_FG_PCT','D_FGM','D_FGA','D_FG_PCT','OFF_RATING','DEF_RATING','AST_RATIO','PACE','PTS_OFF_TOV','PTS_2ND_CHANCE','PTS_FB','PTS_PAINT','DEF_WS','FTR','AVG_REB_DIST','REB_CHANCE_PCT','REB_CHANCE_PCT_ADJ','REB_CHANCES','REB_CONTEST_PCT','RAFGM','RAFGA','RAFG_PCT','PFGM','PFGA','PFG_PCT','MRFGM','MRFGA','MRFG_PCT','LCFG3M','LCFG3A','LCFG3_PCT','RCFG3M','RCFG3A','RCFG3_PCT','CFG3M','CFG3A','CFG3_PCT','ABFG3M','ABFG3A','ABFG3_PCT','PCT_FGA_2PT','PCT_FGA_3PT','PCT_PTS_2PT','PCT_PTS_2PT_MR','PCT_PTS_3PT','PCT_PTS_FB','PCT_PTS_FT','PCT_PTS_OFF_TOV','PCT_PTS_PAINT','PCT_AST_2PM','PCT_UAST_2PM','PCT_AST_3PM','PCT_UAST_3PM','PCT_AST_FGM','PCT_UAST_FGM','PIE','PCT_FGM','PCT_FGA','PCT_FG3M','PCT_FG3A','PCT_FTM','PCT_FTA','PCT_OREB','PCT_DREB','PCT_REB','PCT_AST','PCT_TOV','PCT_STL','PCT_BLK','PCT_BLKA','PCT_PF','PCT_PFD','PCT_PTS','OFB_PCT','TIME_OF_POSS_36','ISO_POSS_PCT','ISO_EFG_PCT','ISO_PTS','PRBH_POSS_PCT','PRBH_EFG_PCT','PRBH_PTS','PRRM_POSS_PCT','PRRM_EFG_PCT','PRRM_PTS','SU_POSS_PCT','SU_EFG_PCT','SU_PTS','PCT_PTS_ISO','PCT_PTS_PRBH','PCT_PTS_PRRM','PCT_PTS_SU','PCT_PTS_DRIVES','DRIVES','DRIVE_AST_PCT','DRIVE_PASSES_PCT','PER','OWS','WS','WS/48','OBPM','DBPM','BPM','VORP']

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
