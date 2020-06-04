from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt

################################################## CREATING CLUSTER COLUMNS AND CALCULATING BAYESIAN NET RATING

clusters = list(set((tuple(tf.p1.unique()) + tuple(tf.p2.unique()) + tuple(tf.p3.unique()) + tuple(tf.p4.unique()) + tuple(tf.p5.unique()))))

clusters.sort()

for i in range(1,len(clusters)+1): 
    tf['c'+str(i)] = 0
    
def stint(p1,p2,p3,p4,p5):
    local_clusters = [p1,p2,p3,p4,p5]
    return local_clusters.count(clusters[i-1])
        
for i in range(1,len(clusters)+1):
    tf['c'+str(i)] = np.vectorize(stint)(tf.p1,tf.p2,tf.p3,tf.p4,tf.p5)
    
tf = tf[['ssn','poss','tm_nrtg','avg_poss','ortg','drtg','nrtg','c1','c2','c3','c4','c5','c6','c7','c8']]
    
def adj_nrtg(tm_nrtg,nrtg,poss,avg_poss):
    return ((avg_poss*tm_nrtg)+(poss*nrtg))/(avg_poss+poss)
tf.nrtg = np.vectorize(adj_nrtg)(tf.tm_nrtg,tf.nrtg,tf.poss,tf.avg_poss)

tf = tf[['c1','c2','c3','c4','c5','c6','c7','c8','nrtg']]
    
################################################## RIDGE REGRESSION

# PARAMETER TUNING

features = ['c1','c2','c3','c4','c5','c6','c7','c8']

msk = np.random.rand(len(tf)) < 0.8
train = tf[msk].reset_index(drop=True)
test = tf[~msk].reset_index(drop=True)

row_list = []

for n in range(0,1001):
    clf = Ridge(alpha=n)
    clf.fit(train[features],train.nrtg)
    score = clf.score(test[features],test.nrtg)
    dict1 = {'alpha':n,'score':score}
    row_list.append(dict1)
    
alpha_df = pd.DataFrame(row_list)

alpha = alpha_df[alpha_df.score == alpha_df.score.max()].alpha.values[0]

# RIDGE REGRESSION

clf = Ridge(alpha=alpha)

clf.fit(tf[features],tf.nrtg)

coefficients = clf.coef_
