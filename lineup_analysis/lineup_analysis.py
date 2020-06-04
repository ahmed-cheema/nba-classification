clusters = list(set((tuple(tf.p1.unique()) + tuple(tf.p2.unique()) + tuple(tf.p3.unique()) + tuple(tf.p4.unique()) + tuple(tf.p5.unique()))))

clusters.sort()

for i in range(1,len(clusters)+1): 
    tf['c'+str(i)] = 0
    
def stint(p1,p2,p3,p4,p5):
    local_clusters = [p1,p2,p3,p4,p5]
    return local_clusters.count(clusters[i-1])
        
for i in range(1,len(clusters)+1):
    tf['c'+str(i)] = np.vectorize(stint)(tf.p1,tf.p2,tf.p3,tf.p4,tf.p5)
    
def adj_nrtg(tm_nrtg,nrtg,poss,avg_poss):
    return ((avg_poss*tm_nrtg)+(poss*nrtg))/(avg_poss+poss)
tf.nrtg = np.vectorize(adj_nrtg)(tf.tm_nrtg,tf.nrtg,tf.poss,tf.avg_poss)
    
tf = tf[['ssn','ortg','drtg','poss','nrtg','c1','c2','c3','c4','c5','c6','c7','c8']]
