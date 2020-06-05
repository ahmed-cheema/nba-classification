from xgboost.sklearn import XGBRegressor
import matplotlib.pyplot as plt
import itertools as it
import pandas as pd
import numpy as np

features = ['c1','c2','c3','c4','c5','c6','c7','c8'] 

# FIT MODEL
    
model = XGBRegressor(learning_rate = 0.1,
                     n_estimators=100,
                     max_depth=3,
                     gamma=0,
                     objective='reg:squarederror')

model.fit(tf[features].values,tf.nrtg.values)

# FEATURE IMPORTANCE

fimp = []
for n in features:
    fimp.append(model.get_booster().get_score(importance_type='gain')[n]) 
data = pd.DataFrame(data=fimp, index=clusters, columns=["score"]).sort_values(by = "score")
data.plot(kind='barh',edgecolor='black',legend=None)
plt.title('feature importance')
plt.xlim(0,400)
plt.tight_layout()

# CREATE ALL POSSIBLE FIVE-MAN LINEUPS

lineups = [i for i in it.product(range(0,6),repeat=8) if sum(i)==5]

df = pd.DataFrame(data=lineups,columns=features)

df['nrtg'] = model.predict(df[features])

# HISTOGRAM OF NET RATING PREDICTIONS

plt.hist(df.nrtg,edgecolor='black',bins=np.linspace(-15,15,31))
plt.xlim(-13,14)
plt.xlabel('predicted lineup net rating')
plt.ylabel('frequency')
plt.title('frequenecy of lineup net rating predictions ')
plt.tight_layout()

# ALL NET RATING DIFF

df_list = []
for n in features:
    df_list.append(df.groupby(n).mean()[['nrtg']])
onoff = pd.concat(df_list, axis=1)
onoff.columns = ['c1','c2','c3','c4','c5','c6','c7','c8']
for n,i in zip(features,range(0,8)):
    plt.plot(onoff.index,onoff[n],label=clusters[i],linewidth=3)
    plt.scatter(onoff.index,onoff[n])
plt.xlim(0,5)
plt.axhline(y=0,c='black',linewidth=1.5)
plt.legend(bbox_to_anchor=(1, 0.75),loc='best',ncol=1)
plt.xlabel('frequency of player classification')
plt.ylabel('avg lineup net rating')
plt.title('lineup net rating vs player freq')
plt.tight_layout()
