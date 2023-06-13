import numpy as np

def xorgate(a, b):
    return (a and not b) or (not a and b)

def hamming_distance(train, query):
    binarydistance = 0
    for i in len(query):
        if xorgate(query[i], train[i]):
            binarydistance += 1
            
    return(binarydistance)

def kmeans_cluster(descriptors, k, iteration):
    #generating random cluster centroids
    clusters = [[] for i in range(k)]
    initalcentroids = np.random.choice(descriptors, size = k, replace = False)
    clustersum = initalcentroids
    for j in range(k):
        clusters[j].append(initialcentroid[j])
    
    for descriptor in descriptors:
        hammingdistance = []
        for centroid in clusters:
            hammingdistance.append(hamming_distance(descriptor, centroid))     
        closestcluster = centroid[np.argmin(hammingdistance)]
            
                
        
        