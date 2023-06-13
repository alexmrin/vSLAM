import numpy as np

def xorgate(a, b):
    return (a and not b) or (not a and b)

def hamming_distance(train, query):
    binarydistance = 0
    for i in len(query):
        if xorgate(query[i], train[i]):
            binarydistance += 1
            
    return(binarydistance)

#returns the mean descriptor of the cluster
def meandescriptor(clustersum):
    mean = [i / clustersum[1] for i in clustersum[0]]
    mean = [round(value) for value in mean]
    return mean

def kmeans_cluster(descriptors, k, iteration):
    #generating random cluster centroids
    clustersums = (np.random.choice(descriptors, size = k, replace = False), 1.0)
    
    for descriptor in descriptors:
        hammingdistance = []
        for clustersum in clustersums:
            #find the mean value of the clustersum
            meanvalue = meandescriptor(clustersum)
            hammingdistance.append(hamming_distance(descriptor, meanvalue))     

        #index of cluster closest cluster to descriptor
        closestIndex = np.argmin(hammingdistance)
        clustersums[closestIndex][0] = [i + j for i, j in zip(clustersums[closestIndex][0], descriptor)]
        clustersums[closestIndex][1] += 1

        



            
                
        
        